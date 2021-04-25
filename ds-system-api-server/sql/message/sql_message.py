from mysql_config import func


class MessageTB:
    # 添加学生按钮对话框的宿舍楼信息
    def selectdormitory():
        sql = "SELECT distinct dormitory_id From dormitory order by dormitory_id asc"
        re = func(sql)
        result = []
        for i in re:
            relist = {}
            relist['dormitory_id'] = str(i[0])
            result.append(relist)
        return result

    def selecthouse():
        sql = "SELECT * From house"
        re = func(sql)
        result = []
        for i in re:
            relist = {}
            relist['house_id'] = str(i[0])
            result.append(relist)
        return result


class InsertmsgTB:

    def __init__(self, num):
        self.num = num
    # 添加楼宇

    def inserthouse(self):
        sql = "INSERT house (house_id) VALUES ('%s')" % (self.num)
        result = func(sql)
        return result


class updatepeopleTB:

    def __init__(self, dormitory_id, floor_id, num):
        self.dormitory_id = dormitory_id
        self.floor_id = floor_id
        self.num = num

    def updatepeople(self):
        sql = "UPDATE dormitory SET people=%s  where dormitory_id=%s and floor_id='%s'" % (
            self.num, self.dormitory_id, self.floor_id)
        result = func(sql)
        return result


class InsertdormitorymsgTB:
    def __init__(self, dormitory_id, ceng_num, bed_pid, price, floor_id):
        self.dormitory_id = dormitory_id
        self.ceng_num = ceng_num
        self.bed_pid = bed_pid
        self.price = price
        self.floor_id = floor_id

    def selectdormitory(self):
        # print('insert:',self.dormitory_id, self.ceng_num, self.bed_pid, self.price, self.floor_id)
        sql = "INSERT into dormitory (dormitory_id, ceng_num, bed_pid, price, floor_id)VALUES (%s,%s,%s,'%s','%s')" % (
            self.dormitory_id, self.ceng_num, self.bed_pid, self.price, self.floor_id)
        result = func(sql)
        return result

    def insertdormitory(self):
        # print('insert:', self.dormitory_id, self.ceng_num,
        #       self.bed_pid, self.price, self.floor_id)
        sql = "INSERT into dormitory (dormitory_id, ceng_num, bed_pid, price, floor_id)VALUES (%s,%s,%s,'%s','%s')" % (
            self.dormitory_id, self.ceng_num, self.bed_pid, self.price, self.floor_id)
        result = func(sql)
        return result


class selectdormitorymsgTB:
    def __init__(self, dormitory_id, floor_id):
        self.dormitory_id = dormitory_id
        self.floor_id = floor_id
        # print(self.dormitory_id,self.floor_id)

    def selectdormitory(self):
        sql = "SELECT * From dormitory where dormitory_id= '%s' and floor_id='%s'" % (
            self.dormitory_id, self.floor_id)
        result = func(sql)
        return result

    def selectdormitorylist(self):

        sql = "SELECT * From dormitory where dormitory_id= '%s' and floor_id='%s'" % (
            self.dormitory_id, self.floor_id)
        re = func(sql)
        result = []
        for i in re:
            result.append(i[3])
        # print('床位',result)
        return result[0]

    def selectdormitory_edit(self):
        sql = "SELECT count(*) FROM student s, dormitory d where d.floor_id = s.stu_dormitory_id and d.dormitory_id = s.stu_dormitory and dormitory_id='%s'  and floor_id='%s'" % (
            self.dormitory_id, self.floor_id)
        re = func(sql)
        result = []
        for i in re:
            result.append(i[0])
        return result[0]

    def selectdormitory_edit(self):
        sql = "SELECT count(*) FROM student s, dormitory d where d.floor_id = s.stu_dormitory_id and d.dormitory_id = s.stu_dormitory and dormitory_id='%s'  and floor_id='%s'" % (
            self.dormitory_id, self.floor_id)
        re = func(sql)
        result = []
        for i in re:
            result.append(i[0])
        return result[0]

    def updatecount(self):
        sql = "UPDATE dormitory SET people=people-1 where dormitory_id= '%s' and floor_id='%s'" % (
            self.dormitory_id, self.floor_id)
        result = func(sql)
        # print(result)
        return result
        # 更改宿舍当前的宿舍人数

    def update_nofull():
        sql = "UPDATE dormitory SET isfull='0' where people < bed_pid"
        result = func(sql)
        return result

    def update_isfull():
        sql = "UPDATE dormitory SET isfull='1' where people = bed_pid"
        result = func(sql)
        return result
    def Student_ifnull():
        sql = "UPDATE dormitory SET people=0"
        result = func(sql)
        return result

    def selectcount():
        sql = "select stu_dormitory_id,stu_dormitory,count(*) from student group by stu_dormitory,stu_dormitory_id"
        re = func(sql)
        if re==():#student为空的数据,更新数据
            print('student为空了')
            selectdormitorymsgTB.Student_ifnull()
            selectdormitorymsgTB.update_isfull()
            selectdormitorymsgTB.update_nofull()
        else:
            result = []
            for i in re:
                relist = {}
                relist['stu_dormitory_id'] = str(i[0])
                relist['stu_dormitory'] = str(i[1])
                relist['count'] = str(i[2])
                Reupdate(str(i[2]), str(i[0]), str(i[1])).select_update_count()
                selectdormitorymsgTB.update_isfull()
                selectdormitorymsgTB.update_nofull()
                result.append(relist)
            return result


# 更新状态用的


class Reupdate:
    def __init__(self, count, stu_dormitory_id, stu_dormitory):
        self.count = count
        self.stu_dormitory_id = stu_dormitory_id
        self.stu_dormitory = stu_dormitory
    def select_update_count(self):
        sql = "UPDATE dormitory SET people=%s where floor_id='%s' and dormitory_id ='%s'" % (
            self.count, self.stu_dormitory_id, self.stu_dormitory)
        result = func(sql)
        print('更新数据')
        return result


class UpdatedormitorymsgTB:
    def __init__(self, ceng_num, bed_pid, price, dormitory_id, floor_id):
        self.dormitory_id = dormitory_id
        self.ceng_num = ceng_num
        self.bed_pid = bed_pid
        self.price = price
        self.floor_id = floor_id

    def updatedormitory(self):
        # print('update:', self.dormitory_id, self.ceng_num,
        #       self.bed_pid, self.price, self.floor_id)
        sql = "UPDATE dormitory SET ceng_num=%s, bed_pid=%s, price='%s'  where dormitory_id=%s and floor_id='%s'" % (
            self.ceng_num, self.bed_pid, self.price, self.dormitory_id, self.floor_id)
        result = func(sql)
        return result


class DeletemsgTB:

    def __init__(self, num):
        self.num = num

    def deletehouse(self):
        sql = "delete from house where house_id = '%s'" % (self.num)
        result = func(sql)
        return result

    def delete_floor_id(self):
        sql = "DELETE from dormitory where floor_id= '%s'" % (self.num)
        result = func(sql)
        return result

    def delete_dormitory(self):
        sql = "delete from dormitory where nid = '%s'" % (self.num)
        result = func(sql)
        return result

    def delete_student(self):
        sql = "delete from student where stu_id = '%s'" % (self.num)
        result = func(sql)
        return result

    def delete_student_msg(self):
        sql = "select * from student where stu_id = '%s'" % (self.num)
        re = func(sql)
        result = []
        for i in re:
            relist = {}
            relist['stu_dormitory'] = str(i[7])
            relist['stu_dormitory_id'] = str(i[8])
            selectdormitorymsgTB(str(i[7]),str(i[8])).updatecount()
            result.append(relist)
        return result

 # 更新住满状态用的


class updatestateTB:
    def __init__(self, dormitory_id, floor_id, num):
        self.dormitory_id = dormitory_id
        self.floor_id = floor_id
        self.num = num

    def updatestate(self):
        sql = "UPDATE dormitory SET isfull='%s' where floor_id='%s' and dormitory_id='%s'" % (
            self.num, self.floor_id, self.dormitory_id)
        result = func(sql)
        return result


class SelectmsgTB:

    def __init__(self, num):
        self.num = num

    def selecthouse_parameter(self):
        sql = "SELECT * FROM house h, dormitory d where d.floor_id = h.house_id and house_id='%s'  and floor_id='%s'" % (
            self.num, self.num)
        result = func(sql)
        return result

    def select_dormitory(self):
        sql = "select * from dormitory where nid = '%s'" % (self.num)
        re = func(sql)
        result = []
        for i in re:
            relist = {}
            relist['dormitory_id'] = str(i[1])
            relist['ceng_num'] = str(i[2])
            relist['bed_pid'] = str(i[3])
            relist['price'] = str(i[4])
            relist['floor_id'] = str(i[5])
            result.append(relist)
        return result

    def check_dormitory(self):  # 宿舍功能区删除按钮删除后查询用的
        sql = "select * from dormitory where nid = '%s'" % (self.num)
        result = func(sql)
        return result

    def selectdormitory_parameter(self):
        sql = "SELECT * From dormitory where floor_id ='%s'" % (self.num)
        re = func(sql)
        result = []
        for i in re:
            relist = {}
            relist['nid'] = str(i[0])
            relist['dormitory_id'] = str(i[1])
            relist['ceng_num'] = str(i[2])
            relist['bed_pid'] = str(i[3])
            relist['price'] = str(i[4])
            relist['floor_id'] = str(i[5])
            relist['isfull'] = str(i[6])
            relist['people'] = str(i[7])
            result.append(relist)
        return result

 # 模糊查询
    def selectdormitory_btn(self):
        args = '%'+self.num+'%'
        sql = "SELECT * FROM dormitory d where concat(d.price,d.ceng_num,d.floor_id,d.dormitory_id,d.bed_pid) LIKE '%s'" % args
        re = func(sql)
        result = []
        for i in re:
            relist = {}
            relist['nid'] = str(i[0])
            relist['dormitory_id'] = str(i[1])
            relist['ceng_num'] = str(i[2])
            relist['bed_pid'] = str(i[3])
            relist['price'] = str(i[4])
            relist['floor_id'] = str(i[5])
            relist['isfull'] = str(i[6])
            relist['people'] = str(i[7])
            result.append(relist)
        return result
