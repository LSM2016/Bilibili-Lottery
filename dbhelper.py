import mysql.connector
from comment import *

host = "localhost"
user = "username"
passwd = "********"
database = "databaseName"


# 连接到数据库
def connect_db():
    conn = mysql.connector.connect(
        host=host,
        user=user,
        passwd=passwd,
        database=database)

    c = conn.cursor()
    return conn, c


# 数据库相关配置
comment_tablename = "Comments"


# 获得满足条件的表内数据
def get_all_by_condition(c, tablename, condition_name, condition):
    sql = "SELECT * FROM " + tablename + " WHERE " + condition_name + " =" + condition
    c.execute(sql)
    return c.fetchall()


# 获取相应表内所有数据
def get_all(c, tablename):
    sql = "SELECT * FROM " + tablename
    c.execute(sql)
    return c.fetchall()


# 获取所有的Comments
def get_all_comments(c):
    sql = "SELECT floor, mid, username, rpid, gender, content, ctime, likes, rcount FROM " + \
        str(comment_tablename)
    c.execute(sql)
    return c.fetchall()


# 往数据库中插入相应的Comment信息
def insert_comment(c, conn, comment):
    sql = "INSERT INTO " + comment_tablename + \
        " (floor, mid, username, rpid, gender, content, ctime, likes, rcount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    c.execute(sql, (comment.floor, comment.mid, comment.username, comment.rpid,
                    comment.gender, comment.content, comment.ctime, comment.likes, comment.rcounts))
    conn.commit()


def get_comment_by_id(c, rpid):
    sql = "SELECT floor, mid, username, rpid, gender, content, ctime, likes, rcount FROM " + \
        str(comment_tablename) + ' WHERE rpid = %s'
    c.execute(sql, (rpid,))
    return c.fetchall()
