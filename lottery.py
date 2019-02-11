import math
import time
import random

import dbhelper
from comment import *


def print_comment(comm):
    print("[楼层]:", comm[0], "|[B站ID]:", comm[1], "|[昵称]:", comm[2], "|[评论ID]:", comm[3], "|[性别]:",
          comm[4], "|[评论内容]:", comm[5], "|[评论时间]:", comm[6], "|[点赞数]:", comm[7], "|[回复数]:", comm[8])


def check_user_exist(comm, comm_list):
    existed = False
    for item in comm_list:
        # print(comm[1], item[1])
        if comm[1] == item[1]:
            #print(comm[1], item[1])
            existed = True
    return existed


conn, c = dbhelper.connect_db()

comments = dbhelper.get_all_comments(c)
comments_list = []


for comm in comments:
    comments_list.append(comm)

comment_list = []
print("   一共", len(comments_list), "条评论...")
time.sleep(3)
print("   正在清理重复评论的楼层，确保中奖概率相同... ")
for comm in comments_list:
    if not check_user_exist(comm, comment_list):
        comment_list.append(comm)

chars = ['-', '\\', '|', '/']
time.sleep(3)
print("   清理掉了", len(comments_list) - len(comment_list), "条评论...")

time.sleep(3)


for i in range(10):
    time.sleep(0.3)
    print("\r" + str(chars[i % 4]) + "   正在打乱楼层... ".format(i), end="")
    random.shuffle(comment_list)
print("\n")
for i in range(10):
    time.sleep(0.3)
    print("\r" + str(chars[i % 4]) + "   抽奖中... ".format(i), end="")

print("\n")

bingo = []
print("================开奖================")
for i in range(5):
    tmp_rand = random.randint(0, len(comment_list))
    print(tmp_rand)
    while tmp_rand in bingo:
        print(tmp_rand)
        tmp_rand = random.randint(0, len(comment_list))
    bingo.append(tmp_rand)

for i in bingo:
    print_comment(comment_list[i])
