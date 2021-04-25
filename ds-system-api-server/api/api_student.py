from flask import Blueprint, Flask, request, jsonify, g
from jsontools.jsontools import format, format_false, format_full, format_nofind, format_iscunzai
from sql.message.sql_message import MessageTB, selectdormitorymsgTB, DeletemsgTB, updatestateTB, InsertmsgTB, updatepeopleTB
from sql.student.sql_student import StudentTB, InsertstudentmsgTB, UpdatastudentTB, SelectmsgTB
student = Blueprint('student', __name__)

# 获取-获取学生的基本信息


@student.route('/info')
def getstudent():
    if request.method == 'GET':
        try:
            studentlist = StudentTB.selectstudent()
            if studentlist == ():
                content = jsonify(format_false(False, None, "学生息请求失败"))
            else:
                content = jsonify(format(True, studentlist, "学生信息请求成功"))
        except:
            content = jsonify(format_false(False, None, '可能是代码错误'))
    else:
        content = jsonify(format_false(False, None, '101'))
    return content

# 模糊查询


@student.route('/getstumessage', methods=['POST'])
def getstumessage_all():
    if request.method == 'POST':
        param = request.form.to_dict()
        num = param.get('num')
        if num == None:
            return jsonify(format_false(False, None, "学生num为空"))
        else:
            messagelis = SelectmsgTB(num).selectstudent_btn()
            if messagelis == ():
                content = jsonify(format_false(False, None, "任意查询——学生信息请求失败"))
            else:
                content = jsonify(format(True, messagelis, "任意查询——学生信息请求成功"))
    else:
        content = jsonify(format_false(False, None, '101'))
    return content

# 获取-宿舍详情点击按钮-联合查询


@student.route('/get_student_dormitory', methods=['POST'])
def getstud_message_all():
    if request.method == 'POST':
        param = request.form.to_dict()
        num = param.get('num')
        if num == None:
            return jsonify(format_false(False, None, "联合查询-num为空"))
        else:
            messagelist = SelectmsgTB(num).select_student_dormitory()
            if messagelist == ():
                content = jsonify(format_false(
                    False, None, "联合查询-学生信息和宿舍信息请求失败"))
            else:
                content = jsonify(
                    format(True, messagelist, "联合查询-学生信息和宿舍信息请求成功"))
    else:
        content = jsonify(format_false(False, None, '101'))
    return content

# 添加-点击学生按钮


@student.route('/addstumsg', methods=['POST'])
def post_addstumsg():
    if request.method == 'POST':
        param = request.form.to_dict()
        stu_id = param.get('num[stu_id]')
        stu_name = param.get('num[stu_name]')
        stu_gender = param.get('num[stu_gender]')
        stu_age = param.get('num[stu_age]')
        stu_depart = param.get('num[stu_depart]')
        stu_grade = param.get('num[stu_grade]')
        stu_phone = param.get('num[stu_phone]')
        stu_dormitory = param.get('num[stu_dormitory]')
        stu_dormitory_id = param.get('num[stu_dormitory_id]')
        if not all([stu_id, stu_name, stu_gender, stu_age, stu_depart, stu_grade, stu_phone, stu_dormitory, stu_dormitory_id]):
            return jsonify(format_false(False, None, "表单有空的"))
        else:
            # 先判断学生的id是否存在
            isnull = SelectmsgTB(stu_id).select_student()
            if isnull == ():
                count = InsertstudentmsgTB(stu_id, stu_name, stu_gender, stu_age, stu_depart,
                                           stu_grade, stu_phone, stu_dormitory, stu_dormitory_id).selectstudent()

                bed = selectdormitorymsgTB(
                    stu_dormitory, stu_dormitory_id).selectdormitorylist()
                # count是从0开始的, count<4 0,1,2,3
                if count < bed:
                    num = InsertstudentmsgTB(stu_id, stu_name, stu_gender, stu_age, stu_depart,
                                           stu_grade, stu_phone, stu_dormitory, stu_dormitory_id).insertstudent()
                    count = InsertstudentmsgTB(stu_id, stu_name, stu_gender, stu_age, stu_depart,
                                               stu_grade, stu_phone, stu_dormitory, stu_dormitory_id).selectstudent()
                    bed = selectdormitorymsgTB(
                        stu_dormitory, stu_dormitory_id).selectdormitorylist()
                    if count == bed:
                        state = updatestateTB(
                            stu_dormitory, stu_dormitory_id, '1').updatestate()
                        if state == ():
                            content = jsonify(
                                format(True, state, '更新状态功能--宿舍是否满人状态更新成功'))
                    if num == ():
                        updatepeopleTB(
                            stu_dormitory, stu_dormitory_id, count).updatepeople()
                        content = jsonify(format(
                            True, count, "<-当前人数-添加-学生信息成功"))
                    else:
                        content = jsonify(format_false(
                            False, num, '添加-学生信息失败'))
                else:
                    # 更改状态
                    content = jsonify(format_full(
                        False, None, '宿舍成员已经满了'))  # 状态码202
            else:
                content = jsonify(format_iscunzai(
                    False, isnull, "学生添加功能-学生id已经存在"))

    else:
        content = jsonify(format_false(False, None, "101"))
    return content



# 实现删除按钮
@student.route('/deletenum/<num>', methods=['PUT'])
def delete_student(num):
    if request.method == 'PUT':
        if num == None:
            return jsonify(format_false(False, None, "num为空"))
        else:
            try:
                DeletemsgTB(num).delete_student_msg()
                DeletemsgTB(num).delete_student()
                num_n = SelectmsgTB(num).select_student()
                if num_n == ():
                    content = jsonify(format(True, num_n, '学生删除功能-学生删除成功'))
                else:
                    content = jsonify(format_false(
                        False, num_n, "学生删除功能-学生删除失败"))
            except:
                content = jsonify(format_false(False, None, '学生删除功能-可能是代码错误'))
    else:
        content = jsonify(format_false(False, None, "101"))
    return content


# 获取——编辑学生信息
results = None


@student.route('/editnum/<num>', methods=['POST'])
def edit_student(num):
    if request.method == 'POST':
        if num == None:
            return jsonify(format_false(False, None, "num为空"))
        else:
            try:
                global results
                num_n = SelectmsgTB(num).select_studentmsg()
                results = num_n
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

# 提交——编辑学生信息


@student.route('/commiteditnum', methods=['POST'])
def edit_student_editnum_commit():
    if request.method == 'POST':
        param = request.form.to_dict()
        stu_id = param.get('num[stu_id]')
        stu_name = param.get('num[stu_name]')
        stu_gender = param.get('num[stu_gender]')
        stu_age = param.get('num[stu_age]')
        stu_depart = param.get('num[stu_depart]')
        stu_grade = param.get('num[stu_grade]')
        stu_phone = param.get('num[stu_phone]')
        stu_dormitory = param.get('num[stu_dormitory]')
        stu_dormitory_id = param.get('num[stu_dormitory_id]')
        if not all([stu_id, stu_name, stu_gender, stu_age, stu_depart, stu_grade, stu_phone, stu_dormitory, stu_dormitory_id]):
            return jsonify(format_false(False, None, "表单有空的"))
        else:
            cunzai = selectdormitorymsgTB(
                stu_dormitory, stu_dormitory_id).selectdormitory()
            if cunzai ==():
                content = jsonify(format_nofind(False, None, "学生信息更新失败"))
            else:
                bed = selectdormitorymsgTB(
                stu_dormitory, stu_dormitory_id).selectdormitorylist()
                count = InsertstudentmsgTB(stu_id, stu_name, stu_gender, stu_age, stu_depart,
                                           stu_grade, stu_phone, stu_dormitory, stu_dormitory_id).selectstudent()
                # try:
                dict1 = results[0]
                # print(dict1['stu_dormitory_id'], dict1['stu_dormitory'])
                # count是从0开始的, count<4 0,1,2,3
                # print(count,bed)
                if count <= bed:
                    num_n = UpdatastudentTB(stu_id, stu_name, stu_gender, stu_age, stu_depart,
                                            stu_grade, stu_phone, stu_dormitory, stu_dormitory_id).updatestudent()
                    selectdormitorymsgTB(dict1['stu_dormitory'], dict1['stu_dormitory_id']).updatecount()
                    bed = selectdormitorymsgTB(
                        stu_dormitory, stu_dormitory_id).selectdormitorylist()
                    count = InsertstudentmsgTB(stu_id, stu_name, stu_gender, stu_age, stu_depart,
                                           stu_grade, stu_phone, stu_dormitory, stu_dormitory_id).selectstudent()
                    if count > bed:
                        num_n = UpdatastudentTB(dict1['stu_id'],  dict1['stu_name'],  dict1['stu_gender'],  dict1['stu_age'],  dict1['stu_depart'], 
                                            dict1['stu_grade'], dict1['stu_phone'], dict1['stu_dormitory'], dict1['stu_dormitory_id']).updatestudent()
                        content = jsonify(format_false(False, None, "学生信息更新失败"))

                    else:
                        content = jsonify(format(True, num_n, "学生信息更新成功"))
                else:
                    content = jsonify(format_full(
                        False, None, '宿舍成员已经满了'))  # 状态码202
                # except:
                #     content = jsonify(format_false(False, None, '宿舍更新--成功失败，重复提交'))

    else:
        content = jsonify(format_false(False, None, "101"))
    return content
