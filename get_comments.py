import requests
import json
import time
import math

import dbhelper

from comment import *


def fetch_url(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        print(r.url)
        return r.text
    except requests.HTTPError as e:
        print(e)
        print("HTTPError")
    except requests.RequestException as e:
        print(e)
    except:
        print("Unknown Error !")


def parse_html(html):
    s = json.loads(html)

    # print(str(s['data']['page']['count']))
    reply_list = []
    reply_list = s['data']['replies']
    return reply_list


def form_url(oid, page):
    base_url = 'https://api.bilibili.com/x/v2/reply?type=1&'
    return base_url + 'oid=' + str(oid) + '&pn=' + str(page)


def get_pages(oid):
    base_url = 'https://api.bilibili.com/x/v2/reply?type=1&oid='
    html = fetch_url(base_url + str(oid))
    data = json.loads(html)['data']
    pages = math.ceil(data['page']['count'] / data['page']['size'])
    return pages


def check_exist_comment(comm, comms):
    existed = False
    for item in comms:
        if item.rpid == comm.rpid:
            existed = True
    return existed


# 连接到数据库
def connect_to_db():
    conn, c = dbhelper.connect_db()
    return conn, c


if __name__ == '__main__':
    conn, c = connect_to_db()

    oid = 此处是视频ID
    url = 'https://api.bilibili.com/x/v2/reply?type=1&oid=此处是视频ID'
    html = fetch_url(url)

    pages = get_pages(oid)

    replies = []

    print(pages)

    for i in range(pages):
        replies_cur_page = parse_html(fetch_url(form_url(oid=oid, page=i)))
        for reply in replies_cur_page:
            replies.append(reply)

    comments = []
    for reply in replies:
        # mid, floor, username, gender, ctime, content, likes, rcounts, rpid
        comment = Comment(mid=reply['mid'], floor=reply['floor'], username=reply['member']
                          ['uname'], gender=reply['member']['sex'], ctime=reply['ctime'],
                          content=reply['content']['message'], likes=reply['like'],
                          rcounts=reply['rcount'], rpid=reply['rpid'])
        comments.append(comment)
        if reply['rcount'] > 0:
            for item in reply['replies']:
                comment = Comment(mid=item['mid'], floor=item['floor'], username=item['member']
                                  ['uname'], gender=item['member']['sex'], ctime=item['ctime'],
                                  content=item['content']['message'], likes=item['like'],
                                  rcounts=item['rcount'], rpid=item['rpid'])
                comments.append(comment)

    for item in comments:
        if dbhelper.get_comment_by_id(c, item.rpid) == []:
            dbhelper.insert_comment(c, conn, item)
