from flask import Blueprint, Flask, request, jsonify
from jsontools.jsontools import format, format_false
from sql.user.sql_user import UserTB

user = Blueprint('user', __name__)


@user.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # request.form获得所有post参数放在一个类似dict类中,to_dict()是字典化
        param = request.form.to_dict()
        username = param.get('username')
        password = param.get('password')
        radio = param.get('radio')
        if not all([username, password]):
            return jsonify(format_false(False, None, "密码或者账号为空"))
        else:
            if username != None and password != None:  # 判断二者不为空
                user = UserTB(username,
                          password,radio).selectUser()  # 传3个参数
            if user == None:  # 如果用户名为空
                content = jsonify(format_false(False, None, "用户名不存在"))
            else:  # 如果用户名不为空
                userPwd = UserTB(username,
                                 password,radio).selectUserPwd() # 查账号和密码
                if userPwd == None:
                    content = jsonify(format_false(
                        False, None, "用户名密码不正确"))
                else:
                    content = jsonify(format(True, userPwd, "登录成功"))

            
          
    else:
        content = jsonify(format_false(False, None, "101"))
    return content
