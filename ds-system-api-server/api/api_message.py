from flask import Blueprint, Flask, request, jsonify
from jsontools.jsontools import format, format_false, format_full
from sql.message.sql_message import MessageTB, InsertmsgTB, DeletemsgTB, SelectmsgTB, InsertdormitorymsgTB, UpdatedormitorymsgTB, selectdormitorymsgTB, updatestateTB, updatepeopleTB
message = Blueprint('message', __name__)


# 更新宿舍表的实时人数用的
@message.route('/update', methods=['GET'])
def getmessage_update():
    if request.method == 'GET':
        try:
            countlist = selectdormitorymsgTB.selectcount()
            if countlist == ():
                content = jsonify(format_false(False, None, "更新宿舍表的人数信息请求失败"))
            else:
                content = jsonify(format(True, countlist, "更新宿舍表的人数信息请求成功"))
        except:
            content = jsonify(format_false(False, None, '更新宿舍表的人数-可能是代码错误'))
    else:
        content = jsonify(format_false(False, None, '101'))
    return content

# 获取-模糊搜索用的
@message.route('/getmessage', methods=['POST'])
def getmessage_all():
    if request.method == 'POST':
        param = request.form.to_dict()
        num = param.get('num')
        if num == None:
            return jsonify(format_false(False, None, "num为空"))
        else:
            messagelis = SelectmsgTB(num).selectdormitory_btn()
            if messagelis == ():
                content = jsonify(format_false(False, None, "任意查询——楼信息请求失败"))
            else:
                content = jsonify(format(True, messagelis, "任意查询——楼信息请求成功"))
    else:
        content = jsonify(format_false(False, None, '101'))
    return content


# 获取-点击楼宇按钮C.X发送
@message.route('/getmsg/<num>', methods=['POST'])
def getmessage(num):
    if request.method == 'POST':
        if num == None:
            return jsonify(format_false(False, None, "num为空"))
        else:
            try:
                messagelist = SelectmsgTB(
                    num).selectdormitory_parameter()
                if messagelist == ():
                    content = jsonify(format_false(False, None, "楼宇按钮楼信息请求失败"))
                else:
                    content = jsonify(format(True, messagelist, "楼宇按钮楼信息请求成功"))
            except:
                content = jsonify(format_false(False, None, '可能是代码错误'))
    else:
        content = jsonify(format_false(False, None, '101'))
    return content


# 添加-实现楼宇的添加按钮


@message.route('/addnum', methods=['POST'])
def post_addnum():
    if request.method == 'POST':
        param = request.form.to_dict()
        num = param.get('num')
        if num == None:
            return jsonify(format_false(False, None, "num为空"))
        else:
            try:
                num_n = InsertmsgTB(num).inserthouse()
                if num_n == ():
                    content = jsonify(format(True, num_n, "增加成功"))
                else:
                    content = jsonify(format_false(False, None, '增加失败'))
            except:
                content = jsonify(format_false(False, None, '增加成功失败，重复提交'))
    else:
        content = jsonify(format_false(False, None, "101"))
    return content


# 获取--楼宇的数量
@message.route('/getnum')
def get_addnum():
    if request.method == 'GET':
        try:
            houselist = MessageTB.selecthouse()
            if houselist == ():
                content = jsonify(format_false(False, None, "楼的数量信息请求失败"))
            else:
                content = jsonify(format(True, houselist, "楼的数量信息请求成功"))
        except:
            content = jsonify(format_false(False, None, '楼的数量信息-可能是代码错误'))
    else:
        content = jsonify(format_false(False, None, '101'))
    return content


# 删除-删除楼宇功能按钮
@message.route('/addnum/<num>', methods=['PUT'])
def delete_addnum(num):
    if request.method == 'PUT':
        if num == None:
            return jsonify(format_false(False, None, "num为空"))
        else:
            try:
                DeletemsgTB(num).deletehouse()
                DeletemsgTB(num).delete_floor_id()
                num_n = SelectmsgTB(num).selecthouse_parameter()
                if num_n == ():
                    content = jsonify(format(True, num_n, '删除成功'))
                else:
                    content = jsonify(format_false(False, num_n, "删除失败"))
            except:
                content = jsonify(format_false(False, None, '可能是代码错误'))
    else:
        content = jsonify(format_false(False, None, "101"))
    return content


# 获取——编辑宿舍信息
@message.route('/editnum/<num>', methods=['POST'])
def edit_editnum(num):
    if request.method == 'POST':
        if num == None:
            return jsonify(format_false(False, None, "num为空"))
        else:
            try:
                num_n = SelectmsgTB(num).select_dormitory()
                if num_n == ():
                    content = jsonify(format_false(False, num_n, "编辑-信息获取失败"))
                else:
                    content = jsonify(format(True, num_n, '编辑-信息获取成功'))
            except:
                content = jsonify(format_false(False, None, '编辑-可能是代码错误'))
    else:
        content = jsonify(format_false(False, None, "101"))
    return content
# 提交---编辑提交宿舍信息


@message.route('/commiteditnum', methods=['POST'])
def edit_editnum_commit():
    if request.method == 'POST':
        param = request.form.to_dict()
        dormitory_id = param.get('num[dormitory_id]')
        ceng_num = param.get('num[ceng_num]')
        bed_pid = param.get('num[bed_pid]')
        price = param.get('num[price]')
        floor_id = param.get('num[floor_id]')
        if not all([dormitory_id, ceng_num, bed_pid, price, floor_id]):
            return jsonify(format_false(False, None, "表单有空的"))
        else:
            try:
                bed_pid = int(bed_pid)
                bed = selectdormitorymsgTB(
                    dormitory_id, floor_id).selectdormitory_edit()  # 实际人数
                # print(type(bed_pid))
                # print(type(bed))
                if bed <= bed_pid:  # 实际人数要小于等于你选择的床位数目
                    content = jsonify(format_full(
                        False, None, '人多床少'))  # 状态码202
                    num_n = UpdatedormitorymsgTB(
                        ceng_num, bed_pid, price, dormitory_id, floor_id).updatedormitory()
                    updatestateTB(dormitory_id, floor_id,
                                  '0').updatestate()  # 默认是床多，状态为宿舍不满人
                    if bed == bed_pid:  # 如果床位于人数相等就改状态为宿舍满人
                        state = updatestateTB(
                            dormitory_id, floor_id, '1').updatestate()
                        if state == ():
                            content = jsonify(
                                format(True, state, '更新状态功能-宿舍是否满人状态更新成功'))
                    if num_n == ():
                        updatepeopleTB(dormitory_id, floor_id,
                                       bed).updatepeople()
                        content = jsonify(format(True, bed, "<-当前人数-宿舍更新成功"))
                    else:
                        content = jsonify(format_false(False, None, '宿舍更新失败'))
                else:
                    content = jsonify(format_full(False, None, '人多床少'))
            except:
                content = jsonify(format_false(False, None, '宿舍更新--成功失败，重复提交'))

    else:
        content = jsonify(format_false(False, None, "101"))
    return content

# 查看学生信息


@message.route('/stumsg')
def get_stumsg():
    if request.method == 'GET':
        try:
            houselist = MessageTB.selectstumsg()  # 查左侧菜单
            if houselist == ():
                content = jsonify(format_false(False, None, "楼层和学生信息请求失败"))
            else:
                content = jsonify(format(True, houselist, "学生信息和楼层信息请求成功"))
        except:
            content = jsonify(format_false(False, None, '可能是代码错误'))
    else:
        content = jsonify(format_false(False, None, '101'))
    return content

# 删除宿舍的某一条信息


@message.route('/deletenum/<num>', methods=['PUT'])
def delete_num(num):
    if request.method == 'PUT':
        if num == None:
            return jsonify(format_false(False, None, "num为空"))
        else:
            try:
                DeletemsgTB(num).delete_dormitory()
                num_n = SelectmsgTB(num).check_dormitory()
                if num_n == ():
                    content = jsonify(format(True, num_n, '删除成功'))
                else:
                    content = jsonify(format_false(False, num_n, "删除失败"))
            except:
                content = jsonify(format_false(False, None, '可能是代码错误'))
    else:
        content = jsonify(format_false(False, None, "101"))
    return content

# 添加宿舍信息


@message.route('/addmsg', methods=['POST'])
def post_addmsg():
    if request.method == 'POST':
        param = request.form.to_dict()
        dormitory_id = param.get('num[dormitory_id]')
        ceng_num = param.get('num[ceng_num]')
        bed_pid = param.get('num[bed_pid]')
        price = param.get('num[price]')
        floor_id = 'C' + param.get('num[floor_id]')
        if not all([dormitory_id, ceng_num, bed_pid, price, floor_id]):
            return jsonify(format_false(False, None, "表单有空的"))
        else:
            try:
                num_n = selectdormitorymsgTB(
                    dormitory_id, floor_id).selectdormitory()
                if num_n == ():
                    num_n1 = InsertdormitorymsgTB(
                        dormitory_id, ceng_num, bed_pid, price, floor_id).insertdormitory()
                    content = jsonify(format(True, num_n1, "增加成功"))
                else:

                    content = jsonify(format_false(False, None, '增加失败'))
            except:
                content = jsonify(format_false(False, None, '增加成功失败，重复提交'))

    else:
        content = jsonify(format_false(False, None, "101"))
    return content
