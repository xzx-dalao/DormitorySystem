from flask import Blueprint, Flask, request, jsonify
from jsontools.jsontools import format, format_false
from sql.user.sql_user import UserTB
user = Blueprint('user', __name__)


# @user.route('/reg', methods=['post'])
# def reg():
#     if request.method == 'POST':
#         # request.form获得所有post参数放在一个类似dict类中,to_dict()是字典化
#         # 单个参数可以通过request.form.to_dict().get("xxx","")获得
#         param = request.form.to_dict()
#         username = param.get('username')
#         password = param.get('password')
#         if not all([username, password]):
#             return jsonify(format_false(False, None, "密码或者账号为空"))
#         else:
#             if param.get("username") != "" and len(param.get("username")) < 8 and param.get("password") != "" and len(param.get("password")) < 16:
#                 user = UserTB(param.get('username'), param.get('password'))
#                 user = user.selectUser()
#                 if user != ():
#                     content = jsonify(format_false(False, None, '用户名存在'))
#                 else:
#                     try:
#                         insetintouser = UserTB(param.get("username"), param.get("password")).insetinto()
#                         if insetintouser == ():
#                             content = jsonify(format(True, None, '用户创建成功'))
#                         else:
#                             content = jsonify(
#                                 format_false(False, None, '用户创建失败'))
#                     except:
#                         content = jsonify(format_false(
#                             False, None, '用户创建失败，可能用户名过长'))
#             else:
#                 content = jsonify(format_false(False, None, '用户名密码为空或者过长'))

#     else:
#         content = jsonify(format_false(False, None, '方法请求错误'))

#     return content



@user.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # POST、GET:
        # request.form获得所有post参数放在一个类似dict类中,to_dict()是字典化
        # 单个参数可以通过request.form.to_dict().get("xxx","")获得
        param = request.form.to_dict()
        username = param.get('username')
        password = param.get('password')
        if not all([username, password]):
            return jsonify(format_false(False, None, "密码或者账号为空"))
        else:
            if param.get("username") != None and param.get("password") != None:  # 判断二者不为空
                user = UserTB(param.get("username"),
                              param.get("password"))  # 传两个参数
                user = user.selectUser()  # 先查用户名
                if user == None:  # 如果用户名为空
                    content = jsonify(format_false(False, None, "用户名不存在"))
                else:  # 如果用户名不为空
            
                    userPwd = UserTB(username,
                                     password).selectUserPwd() # 查账号和密码
                    if userPwd == None:
                        content = jsonify(format_false(
                            False, None, "用户名密码不正确"))
                    else:
                        content = jsonify(format(True, userPwd, "登录成功"))
    else:
        content = jsonify(format_false(False, None, "101"))
    return content
