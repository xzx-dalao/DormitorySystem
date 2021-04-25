from mysql_config import func
import base64
import random
import time

# 定义用户表类
class UserTB:
    ''' 用户增加、查询 '''

    def __init__(self, user, pwd,radio):
        self.user = user
        self.pwd = pwd
        self.radio = radio

    # 查询用户名
    def selectUser(self):
        sql = "select * from usertable where username = '%s' and radio='%s'" % (self.user,self.radio)
        result = func(sql)
        return result

    def get_token(self):
        token = base64.b64encode((":".join([str(self), str(
        random.random()), str(time.time()+7200)])).encode("utf-8")).decode("utf-8")
        return token

    # 查询用户名密码
    def selectUserPwd(self):   
        sql = "select * from usertable where username = '%s' and password = '%s' and radio='%s'" % (
            self.user, self.pwd,  self.radio)
        re = func(sql)
        result = []
        for i in re:
            relist = {}
            relist['username'] = str(i[0])
            relist['password'] = str(i[1])
            relist['radio'] = str(i[2])
            relist['token']=UserTB.get_token(i[0])
            result.append(relist)
        return result

