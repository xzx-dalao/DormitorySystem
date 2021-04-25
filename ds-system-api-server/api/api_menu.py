from flask import Blueprint, Flask, request, jsonify
from jsontools.jsontools import format,format_false
from sql.menu.sql_menu import MenuTB
menu = Blueprint('menu', __name__)

@menu.route('/info')
def getmenu():
    if request.method == 'GET':
        try:
            menulist = MenuTB.selectmenu()  # 查左侧菜单
            if menulist == ():
                content = jsonify(format_false(False, None, "菜单请求失败"))
            else:
                content =  jsonify(format(True,menulist,'菜单请求成功'))
        except:
            content = jsonify(format_false(False,None, '可能是代码错误'))
    else:
        content = jsonify(format_false(False, None, '101'))
    return content

@menu.route('/stuinfo')
def getstumenu():
    if request.method == 'GET':
        try:
            menulist = MenuTB.selectmenu_stu()  # 查左侧菜单
            if menulist == ():
                content = jsonify(format_false(False, None, "菜单请求失败"))
            else:
                content =  jsonify(format(True,menulist,'菜单请求成功'))
        except:
            content = jsonify(format_false(False,None, '可能是代码错误'))
    else:
        content = jsonify(format_false(False, None, '101'))
    return content
