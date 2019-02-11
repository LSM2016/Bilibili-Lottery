import time


class Comment:
    def __init__(self, mid, floor, username, gender, ctime, content, likes, rcounts, rpid):
        self.mid = mid
        self.rpid = rpid
        self.floor = floor
        self.username = username
        self.gender = gender
        self.ctime = time.strftime("%Y-%m-%d %H:%M:%S",
                                   time.localtime(ctime))
        self.content = content
        self.likes = likes
        self.rcounts = rcounts
