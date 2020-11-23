from mysql_config import func


# 定义外出表类
class LeaveTB:
    # 查询外出信息
    # def __init__(self):
    #     pass
    def select_leavemsg():
        sql = "SELECT * From gotomessage"
        re = func(sql)
        result = []
        for i in re:
            relist = {}
            relist['goto_id'] = str(i[0])
            relist['goto_name'] = str(i[1])
            relist['goto_phone'] = str(i[2])
            relist['goto_dormitory'] = str(i[3])
            relist['goto_dormitory_id'] = str(i[4])
            relist['goto_leavetime'] = str(i[5])
            relist['goto_backtime'] = str(i[6])
            relist['goto_reason'] = str(i[7])
            relist['goto_islate'] = str(i[8])
            result.append(relist)
        return result


class DeletegotomsgTB:

    def __init__(self, num):
        self.num = num

    def delete_gotomessage(self):
        sql = "delete from gotomessage where goto_id = '%s'" % (self.num)
        result = func(sql)
        return result


class selectgotomsgTB:

    def __init__(self, num):
        self.num = num

    def select_gotomessage(self):  # 删除后查询用的
        sql = "select * from gotomessage where goto_id = '%s'" % (self.num)
        result = func(sql)
        return result


    # 模糊搜索用


    def selectgotomessage_btn(self):
        args = '%'+self.num+'%'
        sql = "SELECT * FROM gotomessage s where concat(s.goto_id,s.goto_name,s.goto_phone,s.goto_dormitory,s.goto_dormitory_id,s.goto_leavetime,s.goto_backtime,s.goto_reason,s.goto_islate) LIKE '%s'" % args
        re = func(sql)
        result = []
        for i in re:
            relist = {}
            relist['goto_id'] = str(i[0])
            relist['goto_name'] = str(i[1])
            relist['goto_phone'] = str(i[2])
            relist['goto_dormitory'] = str(i[3])
            relist['goto_dormitory_id'] = str(i[4])
            relist['goto_leavetime'] = str(i[5])
            relist['goto_backtime'] = str(i[6])
            relist['goto_reason'] = str(i[7])
            relist['goto_islate'] = str(i[8])
            result.append(relist)
        # print(result)
        return result
    # 编辑功能获取信息用

    def select_gotomsg(self):
        sql = "select * from gotomessage where goto_id = '%s'" % (self.num)
        re = func(sql)
        result = []
        for i in re:
            relist = {}
            relist['goto_id'] = str(i[0])
            relist['goto_name'] = str(i[1])
            relist['goto_phone'] = str(i[2])
            relist['goto_dormitory'] = str(i[3])
            relist['goto_dormitory_id'] = str(i[4])
            relist['goto_leavetime'] = str(i[5])
            relist['goto_backtime'] = str(i[6])
            relist['goto_reason'] = str(i[7])
            result.append(relist)
        return result


class InsertgotomsgTB:

    def __init__(self, goto_id, goto_name, goto_phone, goto_dormitory_id, goto_dormitory, goto_leavetime, goto_backtime, goto_reason):
        self.goto_id = goto_id
        self.goto_name = goto_name
        self.goto_phone = goto_phone
        self.goto_dormitory = goto_dormitory
        self.goto_dormitory_id = goto_dormitory_id
        self.goto_leavetime = goto_leavetime
        self.goto_backtime = goto_backtime
        self. goto_reason = goto_reason

    def insertgotomsg(self):
        # print('i:',self.goto_id, self.goto_name, self.goto_phone, self.goto_dormitory, self.goto_dormitory_id, self.goto_leavetime,  self.goto_backtime,self.goto_reason )
        sql = "INSERT into gotomessage( goto_id, goto_name, goto_phone, goto_dormitory_id, goto_dormitory, goto_leavetime, goto_backtime, goto_reason) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" % (
            self.goto_id, self.goto_name, self.goto_phone, self.goto_dormitory, self.goto_dormitory_id, self.goto_leavetime, self.goto_backtime, self. goto_reason)
        result = func(sql)
        return result


class updatestateTB:
    def __init__(self, goto_id, goto_islate):
        self.goto_id = goto_id
        self.goto_islate = goto_islate

    def updatestate(self):
        sql = "UPDATE gotomessage SET goto_islate='%s' where goto_id='%s'" % (
            self.goto_islate, self.goto_id)
        result = func(sql)
        return result


class UpdategotomsgTB:
    def __init__(self, goto_id, goto_name, goto_phone, goto_dormitory, goto_dormitory_id, goto_leavetime, goto_backtime, goto_reason):
        self.goto_id = goto_id
        self.goto_name = goto_name
        self.goto_phone = goto_phone
        self.goto_dormitory = goto_dormitory
        self.goto_dormitory_id = goto_dormitory_id
        self.goto_leavetime = goto_leavetime
        self.goto_backtime = goto_backtime
        self.goto_reason =goto_reason

    def updatgotomsg(self):
        sql = "UPDATE gotomessage SET  goto_name='%s' ,goto_phone='%s', goto_dormitory='%s', goto_dormitory_id='%s' ,goto_leavetime='%s',goto_backtime='%s',goto_reason='%s' where goto_id='%s'" % (
            self.goto_name, self.goto_phone, self.goto_dormitory, self.goto_dormitory_id, self.goto_leavetime, self.goto_backtime, self.goto_reason,  self.goto_id)
        result = func(sql)
        return result