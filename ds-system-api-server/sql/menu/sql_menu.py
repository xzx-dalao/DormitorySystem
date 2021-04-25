from mysql_config import func


# 定义菜单表类


class MenuTB:

    # 查询菜单
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

    def selectmenu_stu():
        sql = "SELECT ps_id,ps_pname,ps_name,ps_path From menus m,childrenmenus s where m.ps_id = s.ps_pid and ps_id=103"
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


