# Bilibili-Lottery
自动爬取B站某个视频的评论并抽奖
# 使用方法
再dbhelper.py内修改你的MySQL相关参数
```
host = "localhost"
user = "username"
passwd = "********"
database = "databaseName"
```
使用python3 get_comments.py来获得B站评论，视频ID在文件内修改。
使用python3 lottery.py来抽奖