from mysql_config import func
import base64
import random
import time
import hmac
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
    # def get_token(self):
    #     expiration = 10
    #     ss = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration) 
    #     token = base64.b64encode((":".join([str(self), str(ss)])).encode()).decode()
    #     return token, expiration

    def generate_token(key, expire=10):
        '''
            @Args:
                key: str (用户给定的key，需要用户保存以便之后验证token,每次产生token时的key 都可以是同一个key)
                expire: int(最大有效时间，单位为s)
            @Return:
                state: str
        '''
        ts_str = str(time.time() + expire)
        ts_byte = ts_str.encode("utf-8")
        sha1_tshexstr  = hmac.new(key.encode("utf-8"),ts_byte,'sha1').hexdigest() 
        token = ts_str+':'+sha1_tshexstr
        b64_token = base64.urlsafe_b64encode(token.encode("utf-8")).decode("utf-8")
        return b64_token



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
            relist['token']=UserTB.generate_token(i[0])
            # UserTB.generate_token(i[0])
            # UserTB.certify_token(i[0],UserTB.generate_token(i[0]))
            result.append(relist)
        return result
    # 插入

    def insetinto(self):
        sql = "INSERT INTO usertable (username,password) VALUES ('%s','%s')" % (
            self.user, self.pwd)
        result = func(sql)
        return result

    # def returntoken():
    #     return (UserTB.generate_token('admin'))