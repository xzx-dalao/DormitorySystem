from mysql_config import func


data = [{
    "id": 101,
    "authName": "宿舍管理",
    "path": '',
    "children": [
                {
                    "id": 104,
                    "authName": "宿舍列表",
                    "path": 'dormitory',
                    "children": []
                }
    ]
}, {
    "id": 102,
    "authName": "学生管理",
    "path": '',
    "children": [
                {
                    "id": 105,
                    "authName": "学生列表",
                    "path": 'message',
                    "children": []
                }
    ]
}, {
    "id": 103,
    "authName": "外出管理",
    "path": '',
    "children": [
                {
                    "id": 106,
                    "authName": "外出信息",
                    "path": 'gotomessage',
                    "children": []
                },

    ]
}
]

# 定义菜单表类


class MenuTB:
    ''' 用户增加、查询 '''
    # 查询菜单
    # def __init__(self):
    #     pass

    def selectmenu():
        sql = "SELECT ps_id,ps_pname,ps_name,ps_path From menus m,childrenmenus s where m.ps_id = s.ps_pid"
        re = func(sql)
        result=[]
        for i in re:
            relist={}
            children={}
            rechild=[]
            relist['id']=str(i[0])
            relist['authName'] = str(i[1])
            children['authName'] =str(i[2])
            children['path'] =str(i[3])
            rechild.append(children)
            #嵌套
            relist['children'] =rechild
            result.append(relist)
        return result

    # def selectmenu():
    #     return data
