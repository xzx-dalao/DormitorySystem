from mysql_config import func
import base64
import random
import time
from flask import Flask, jsonify,  current_app, request
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# 定义用户表类
class UserTB:
    ''' 用户增加、查询 '''

    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    # 查询用户名
    def selectUser(self):
        sql = "select * from usertable where username = '%s'" % self.user
        result = func(sql)
        return result

    # def get_token(self):
    #     token = base64.b64encode((":".join([str(self), str(
    #     random.random()), str(time.time()+7200)])).encode()).decode()
    #     return token
    def get_token(self):
        expiration = 10
        ss = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration) 
        token = base64.b64encode((":".join([str(self), str(ss)])).encode()).decode()
        return token, expiration

    # 查询用户名密码
    def selectUserPwd(self):
        sql = "select * from usertable where username = '%s' and password = '%s' limit 1" % (
            self.user, self.pwd)
        re = func(sql)
        result = []
        for i in re:
            relist = {}
            relist['username'] = str(i[0])
            relist['password'] = str(i[1])
            relist['token']=UserTB.get_token(i[0])
            result.append(relist)
        return result
    # 插入

    def insetinto(self):
        sql = "INSERT INTO usertable (username,password) VALUES ('%s','%s')" % (
            self.user, self.pwd)
        result = func(sql)
        return result
