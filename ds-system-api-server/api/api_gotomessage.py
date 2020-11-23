from flask import Blueprint, Flask, request, jsonify
from jsontools.jsontools import format, format_false, format_full, format_nofind
from sql.gotomessage.sql_gotomessage import LeaveTB, DeletegotomsgTB, selectgotomsgTB, InsertgotomsgTB, updatestateTB,UpdategotomsgTB
gotomessage = Blueprint('gotomessage', __name__)


@gotomessage.route('/info')
def get_gotomessage():
    if request.method == 'GET':
        try:
            menulist = LeaveTB.select_leavemsg()
            if menulist == ():
                content = jsonify(format_false(False, None, "外出信息请求失败"))
            else:
                content = jsonify(format(True, menulist, '外出信息请求成功'))
        except:
            content = jsonify(format_false(False, None, '可能是代码错误'))
    else:
        content = jsonify(format_false(False, None, '101'))
    return content


# 删除功能
@gotomessage.route('/deletenum/<id>', methods=['PUT'])
def delete_gotomessage(id):
    if request.method == 'PUT':
        if id == None:
            return jsonify(format_false(False, None, "num为空"))
        else:
            try:
                DeletegotomsgTB(id).delete_gotomessage()
                num_n = selectgotomsgTB(id).select_gotomessage()
                if num_n == ():
                    content = jsonify(format(True, num_n, '外出删除功能-外出删除成功'))
                else:
                    content = jsonify(format_false(
                        False, num_n, "外出删除功能-外出删除失败"))
            except:
                content = jsonify(format_false(False, None, '外出删除功能-可能是代码错误'))
    else:
        content = jsonify(format_false(False, None, "101"))
    return content


# 添加功能
@gotomessage.route('/addstumsg', methods=['POST'])
def post_addstumsg():
    if request.method == 'POST':
        param = request.form.to_dict()
        goto_id = param.get('num[goto_id]')
        goto_name = param.get('num[goto_name]')
        goto_phone = param.get('num[goto_phone]')
        goto_reason = param.get('num[goto_reason]')
        goto_leavetime = param.get('num[goto_leavetime]')
        goto_backtime = param.get('num[goto_backtime]')
        goto_dormitory = param.get('num[goto_dormitory]')
        goto_dormitory_id = param.get('num[goto_dormitory_id]')
        if not all([goto_id, goto_name, goto_phone, goto_dormitory, goto_dormitory_id]):
            return jsonify(format_false(False, None, "必要信息有空的"))
        else:
            try:
                num = InsertgotomsgTB(goto_id, goto_name, goto_phone, goto_dormitory_id,
                                      goto_dormitory, goto_leavetime, goto_backtime, goto_reason).insertgotomsg()
                if num == ():
                    content = jsonify(format(True, num, "增加成功"))
                else:
                    content = jsonify(format_false(False, None, '增加失败'))
            except:
                content = jsonify(format_false(False, None, '增加成功失败，重复提交'))
    else:
        content = jsonify(format_false(False, None, "101"))
    return content


# 更新状态
@gotomessage.route('/<goto_id>/state/<goto_islate>', methods=['PUT'])
def get_gotomessage1(goto_id, goto_islate):
    if request.method == 'PUT':
        if not all([goto_id, goto_islate]):
            return jsonify(format_false(False, None, "某一项为空"))
        else:
            try:
                num_n = updatestateTB(goto_id, goto_islate).updatestate()
                if num_n == ():
                    content = jsonify(format(True, num_n, '更新状态功能-晚归状态更新成功'))
                else:
                    content = jsonify(format_false(
                        False, num_n, "更新状态功能-晚归状态更新失败"))
            except:
                content = jsonify(format_false(False, None, '更新状态功能-可能是代码错误'))
    else:
        content = jsonify(format_false(False, None, "101"))
    return content


# 模糊查询
@gotomessage.route('/getmessage', methods=['POST'])
def getmessaged_all():
    param = request.form.to_dict()
    num = param.get('num')
    if request.method == 'POST':
        if num == None:
            return jsonify(format_false(False, None, "num为空"))
        else:
            messagelist = selectgotomsgTB(num).selectgotomessage_btn()
            if messagelist == ():
                content = jsonify(format_false(False, None, "任意查询——外出信息请求失败"))
            else:
                content = jsonify(format(True, messagelist, "任意查询——外出信息请求成功"))
    else:
        content = jsonify(format_false(False, None, '101'))
    return content


# 获取——编辑外出信息


@gotomessage.route('/editnum/<num>', methods=['POST'])
def edit_gotomessage(num):
    if request.method == 'POST':
        if num == None:
            return jsonify(format_false(False, None, "num为空"))
        else:
            try:
                num_n = selectgotomsgTB(num).select_gotomsg()
                if num_n == ():
                    content = jsonify(format_false(
                        False, num_n, "编辑-学生信息获取失败"))
                else:
                    content = jsonify(format(True, num_n, '编辑-学生信息获取成功'))
            except:
                content = jsonify(format_false(False, None, '编辑-可能是代码错误'))
    else:
        content = jsonify(format_false(False, None, "101"))
    return content


# 提交---编辑提交外出信息


@gotomessage.route('/commiteditnum', methods=['POST'])
def edit_editgotonum_commit():
    if request.method == 'POST':
        param = request.form.to_dict()
        goto_id = param.get('num[goto_id]')
        goto_name = param.get('num[goto_name]')
        goto_phone = param.get('num[goto_phone]')
        goto_reason = param.get('num[goto_reason]')
        goto_leavetime = param.get('num[goto_leavetime]')
        goto_backtime = param.get('num[goto_backtime]')
        goto_dormitory = param.get('num[goto_dormitory]')
        goto_dormitory_id = param.get('num[goto_dormitory_id]')
        if not all([goto_id, goto_name, goto_phone, goto_dormitory, goto_dormitory_id]):
            return jsonify(format_false(False, None, "必要信息有空的"))
        else:
            try:
                num_n = UpdategotomsgTB(
                    goto_id, goto_name, goto_phone, goto_dormitory, goto_dormitory_id, goto_leavetime, goto_backtime, goto_reason).updatgotomsg()
                if num_n == ():
                    content = jsonify(format(True, num_n, "外出信息更新成功"))
                else:
                    content = jsonify(format_false(False, None, '外出信息更新失败'))
            except:
                content = jsonify(format_false(False, None, '外出信息--更新失败，重复提交'))

    else:
        content = jsonify(format_false(False, None, "101"))
    return content
