from mysql_config import func

class StudentTB:
    #获取学生功能区的默认表单
    def selectstudent():
        sql = "SELECT * From student"
        re = func(sql)
        result = []
        for i in re:
            relist = {}
            relist['stu_id'] = str(i[0])
            relist['stu_name'] = str(i[1])
            relist['stu_gender'] = str(i[2])
            relist['stu_age'] = str(i[3])
            relist['stu_depart'] = str(i[4])
            relist['stu_grade'] = str(i[5])
            relist['stu_phone'] = str(i[6])
            relist['stu_dormitory'] = str(i[7])
            relist['stu_dormitory_id'] = str(i[8])
            result.append(relist)
        return result



class InsertstudentmsgTB:
    def __init__(self, stu_id, stu_name, stu_gender, stu_age, stu_depart, stu_grade, stu_phone, stu_dormitory, stu_dormitory_id):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_gender = stu_gender
        self.stu_age = stu_age
        self.stu_depart = stu_depart
        self.stu_grade = stu_grade
        self.stu_phone = stu_phone
        self.stu_dormitory = stu_dormitory
        self.stu_dormitory_id = stu_dormitory_id
    # 查询当前是否满宿舍

    def selectstudent(self):
        # print(self.stu_dormitory, self.stu_dormitory_id)
        sql = "select count(*) from student where stu_dormitory='%s' and stu_dormitory_id='%s'" % (
            self.stu_dormitory, self.stu_dormitory_id)
        re = func(sql)
        result = []
        for i in re:
            result.append(i[0])
        # print('人数',result)
        return result[0]

    # 加入学生信息及其宿舍
    def insertstudent(self):
        sql = "INSERT into student (stu_id,stu_name,stu_gender,stu_age,stu_depart,stu_grade,stu_phone,stu_dormitory,stu_dormitory_id) VALUES ('%s','%s','%s',%s,'%s','%s','%s','%s','%s')" % (
            self.stu_id, self.stu_name, self.stu_gender, self.stu_age, self.stu_depart, self.stu_grade, self.stu_phone, self.stu_dormitory, self.stu_dormitory_id)
        result = func(sql)
        return result

    #删除学生信息
    def deletestudent(self):
        sql = "DELETE FROM student WHERE stu_id = '%s'" % (self.stu_id)
        result = func(sql)
        return result


class UpdatastudentTB:
    def __init__(self, stu_id, stu_name, stu_gender, stu_age, stu_depart, stu_grade, stu_phone, stu_dormitory, stu_dormitory_id):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_gender = stu_gender
        self.stu_age = stu_age
        self.stu_depart = stu_depart
        self.stu_grade = stu_grade
        self.stu_phone = stu_phone
        self.stu_dormitory = stu_dormitory
        self.stu_dormitory_id = stu_dormitory_id
    #更新学生信息
    def updatestudent(self):
        sql = "UPDATE student SET  stu_name='%s', stu_gender='%s' ,stu_age=%s, stu_depart='%s', stu_grade='%s' ,stu_phone='%s',stu_dormitory=%s,stu_dormitory_id='%s' where stu_id=%s" % (
            self.stu_name, self.stu_gender, self.stu_age, self.stu_depart, self.stu_grade, self.stu_phone, self.stu_dormitory, self.stu_dormitory_id, self.stu_id)
        result = func(sql)
        return result




class SelectmsgTB:

    def __init__(self, num):
        self.num = num

    def select_student(self):  # 宿舍功能区删除按钮删除后查询用的
                                #学生功能区添加按钮用来判断学生的id是否存在
        sql = "select * from student where stu_id = '%s'" % (self.num)
        result = func(sql)
        return result

    def select_studentmsg(self):  # 学生功能区编辑按钮获取信息用
        sql = "select * from student where stu_id = '%s'" % (self.num)
        re = func(sql)
        result = []
        for i in re:
            relist = {}
            relist['stu_id'] = str(i[0])
            relist['stu_name'] = str(i[1])
            relist['stu_gender'] = str(i[2])
            relist['stu_age'] = str(i[3])
            relist['stu_depart'] = str(i[4])
            relist['stu_grade'] = str(i[5])
            relist['stu_phone'] = str(i[6])
            relist['stu_dormitory'] = str(i[7])
            relist['stu_dormitory_id'] = str(i[8])
            result.append(relist)
        return result


    # 模糊查询

    def selectstudent_btn(self):
        args = '%'+self.num+'%'
        sql = "SELECT * FROM student s where concat(s.stu_id,s.stu_name,s.stu_gender,s.stu_age,s.stu_depart,s.stu_grade,s.stu_phone,s.stu_dormitory,s.stu_dormitory_id) LIKE '%s'" % args
        re = func(sql)
        result = []
        for i in re:
            relist = {}
            relist['stu_id'] = str(i[0])
            relist['stu_name'] = str(i[1])
            relist['stu_gender'] = str(i[2])
            relist['stu_age'] = str(i[3])
            relist['stu_depart'] = str(i[4])
            relist['stu_grade'] = str(i[5])
            relist['stu_phone'] = str(i[6])
            relist['stu_dormitory'] = str(i[7])
            relist['stu_dormitory_id'] = str(i[8])
            result.append(relist)
        return result

    
        # 联合查询

    def select_student_dormitory(self):
        sql = "SELECT * FROM student s, dormitory d where d.floor_id = s.stu_dormitory_id and d.dormitory_id = s.stu_dormitory and nid in (select nid from dormitory where nid = '%s')" % (
            self.num)
        re = func(sql)
        result = []
        for i in re:
            relist = {}
            relist['stu_id'] = str(i[0])
            relist['stu_name'] = str(i[1])
            relist['stu_gender'] = str(i[2])
            relist['stu_age'] = str(i[3])
            relist['stu_depart'] = str(i[4])
            relist['stu_grader'] = str(i[5])
            relist['stu_phone'] = str(i[6])
            relist['stu_dormitory'] = str(i[7])
            relist['stu_dormitory_id'] = str(i[8])
            relist['nid'] = str(i[9])
            relist['dormitory_id'] = str(i[10])
            relist['ceng_num'] = str(i[11])
            relist['bed_pid'] = str(i[12])
            relist['price'] = str(i[13])
            relist['floor_id'] = str(i[14])
            result.append(relist)
        return result