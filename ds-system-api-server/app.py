# 导入user
from flask import Flask, jsonify  # 导入依赖
from jsontools.jsontools import format  # 导入方法
from sql.create_table import create_table
# 导入方法
from api.api_user import user  # 导入方法
from api.api_menu import menu  # 导入方法
from api.api_message import message  # 导入方法
from api.api_student import student  # 导入方法
from api.api_gotomessage import gotomessage 
from flask_cors import *  # 跨域
# 创建类的实例
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# 导入各个接口
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(menu, url_prefix='/menus')
app.register_blueprint(message, url_prefix='/message')
app.register_blueprint(student, url_prefix='/student')
app.register_blueprint(gotomessage, url_prefix='/gotomessage')

@app.route('/')
def hello():
    return jsonify(format(True, {}, '这是首页'),)

 # 跨域支持方法


def after_request(response):
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST,DELETE,PUT'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type,Access-Control-Allow-Origin,Authorization, Origin, X-Requested-With, Content-Type, Accept,token,Authentication,Authentication-Token'
    return response


app.after_request(after_request)

CORS(app, supports_credentials=True)
if __name__ == '__main__':
    # print(UserTB.returntoken())
    create_table() #建表
    app.config['JSON_AS_ASCII'] = False  # 是否支持中文
    app.run(debug=True, threaded=True, host='0.0.0.0')
