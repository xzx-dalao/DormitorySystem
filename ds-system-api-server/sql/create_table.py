from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask import Flask
import pymysql
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:xzx123@localhost:3306/test?charset=utf8"
app.config["SECRET_KEY"] = "XZX"  # 创建密匙
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

# 管理员表


class create_usertable(db.Model):  # admin
    __tablename__ = "USERTABLE"
    username = db.Column(db.String(8), nullable=False,
                         primary_key=True, unique=True)
    password = db.Column(db.String(16), nullable=False)
    # gender = db.Column(db.Enum('男','女'),nullable=False)

# 一级菜单表


class create_menus(db.Model):
    __tablename__ = 'menus'
    ps_id = db.Column(db.Integer, primary_key=True, nullable=False)
    ps_pname = db.Column(db.String(20), nullable=False)
   


# 二级菜单表
class create_childrenmenus(db.Model):
    __tablename__ = 'childrenmenus'
    psc_id = db.Column(db.Integer, primary_key=True, nullable=False)
    ps_name = db.Column(db.String(20), nullable=False)
    ps_pid = db.Column(db.Integer, nullable=False, index=True)
    ps_path = db.Column(db.String(20), nullable=False)
   

# 宿舍信息表


class create_dormitory(db.Model):
    __tablename__ = 'dormitory'
    nid = db.Column(db.Integer, primary_key=True, nullable=False, index=True)
    dormitory_id = db.Column(db.Integer, nullable=False)
    ceng_num = db.Column(db.Integer, nullable=False)
    bed_pid = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Enum('1000', '1500', '2000'), nullable=False)
    floor_id = db.Column(db.String(5), nullable=False)
    isfull = db.Column(db.Enum('1', '0') , server_default="0", nullable=False)
    people = db.Column(db.Integer, server_default="0")
# C几楼


class create_house(db.Model):
    __tablename__ = 'house'
    house_id = db.Column(db.String(20), nullable=False, primary_key=True)


# 学生表
class create_student(db.Model):
    __tablename__ = 'student'
    stu_id = db.Column(db.String(25), primary_key=True,
                       nullable=False, index=True)
    stu_name = db.Column(db.String(20), nullable=False)
    stu_gender = db.Column(db.Enum('男', '女'), nullable=False)
    stu_age = db.Column(db.Integer, nullable=False)
    stu_depart = db.Column(db.String(20), nullable=False)
    stu_grade = db.Column(db.String(5), nullable=False)
    stu_phone = db.Column(db.String(22), nullable=False)
    stu_dormitory = db.Column(db.Integer, nullable=False)
    stu_dormitory_id = db.Column(db.String(22), nullable=False)


class create_gotomessage(db.Model):
    __tablename__ = 'gotomessage'
    goto_id = db.Column(db.String(25), primary_key=True,
                        nullable=False, index=True)
    goto_name = db.Column(db.String(10), nullable=False)
    goto_phone = db.Column(db.String(22), nullable=False)
    goto_dormitory = db.Column(db.String(10), nullable=False)
    goto_dormitory_id = db.Column(db.String(10), nullable=False)
    goto_leavetime = db.Column(db.String(25))
    goto_backtime = db.Column(db.String(25))
    goto_reason = db.Column(db.Text)
    goto_islate = db.Column(db.Enum('1', '0'), server_default="0")


# if __name__=='__main__':
def create_table():
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>数据表--创建成功')
    db.drop_all()
    db.create_all()
    # rs1 = create_student(stu_id="201810097078", stu_name="xzx", stu_gender="男", stu_age="18", stu_depart="计算机学院",
    #                      stu_grade="2018", stu_phone="13229019824", stu_dormitory="655", stu_dormitory_id="C1")
    # rs2 = create_student(stu_id="201810097022", stu_name="zff", stu_gender="女", stu_age="20", stu_depart="管理学院",
    #                      stu_grade="2020", stu_phone="13258435247", stu_dormitory="655", stu_dormitory_id="C2")
    # rs3 = create_student(stu_id="201810097075", stu_name="nbb", stu_gender="男", stu_age="19", stu_depart="电气学院",
    #                      stu_grade="2019", stu_phone="13252635147", stu_dormitory="653", stu_dormitory_id="C1")

    role = create_usertable(username="admin", password="123456")  # 默认注册管理员
    r0 = create_dormitory(dormitory_id="655",
                          floor_id="C1", bed_pid='2', price='1500', ceng_num="6")
    r1 = create_dormitory(dormitory_id="653",
                          floor_id="C1", bed_pid='4', price='2000', ceng_num="6")
    r2 = create_dormitory(dormitory_id="412",
                          floor_id="C2", bed_pid='4', price='1000', ceng_num="5")
    r3 = create_dormitory(dormitory_id="522",
                          floor_id="C2", bed_pid='4', price='2000', ceng_num="5")
    r4 = create_dormitory(dormitory_id="651",
                          floor_id="C3", bed_pid='4', price='1500', ceng_num="6")
    r5 = create_dormitory(dormitory_id="658",
                          floor_id="C4", bed_pid='4', price='2000', ceng_num="6")
    r6 = create_dormitory(dormitory_id="512",
                          floor_id="C5", bed_pid='4', price='1000', ceng_num="5")
    r7 = create_dormitory(dormitory_id="520",
                          floor_id="C5", bed_pid='4', price='2000', ceng_num="5")
    r8 = create_dormitory(dormitory_id="525",
                          floor_id="C5", bed_pid='4', price='2000', ceng_num="5")
    r9 = create_dormitory(dormitory_id="655",
                          floor_id="C2", bed_pid='3', price='2000', ceng_num="5")
    r10 = create_dormitory(dormitory_id="655",
                           floor_id="C3", bed_pid='4', price='1500', ceng_num="5")
    r11 = create_dormitory(dormitory_id="554",
                           floor_id="C3", bed_pid='3', price='2000', ceng_num="5")
    r12 = create_dormitory(dormitory_id="852",
                           floor_id="C3", bed_pid='4', price='2000', ceng_num="5")

    role1 = create_menus(ps_id="101", ps_pname="宿舍管理", ps_level='1')
    role2 = create_menus(ps_id="102", ps_pname="学生管理", ps_level='1')
    role3 = create_menus(ps_id="103", ps_pname="出入管理", ps_level='1')
    # role4 = create_menus(ps_id="104", ps_pname="学校管理", ps_level='1')
    rol1 = create_childrenmenus(
        psc_id="1", ps_name="宿舍信息", ps_level='1', ps_pid='101', ps_path='dormitory')
    rol2 = create_childrenmenus(
        psc_id="2", ps_name="学生信息", ps_level='1', ps_pid='102', ps_path='message')
    rol3 = create_childrenmenus(
        psc_id="3", ps_name="出入信息", ps_level='1', ps_pid='103', ps_path='gotomessage')
    # rol4 = create_childrenmenus(
    #     psc_id="4", ps_name="学校信息", ps_level='1', ps_pid='104', ps_path='school')

    rh1 = create_house(house_id="C1")
    rh2 = create_house(house_id="C2")
    rh3 = create_house(house_id="C3")
    rh4 = create_house(house_id="C4")
    rh5 = create_house(house_id="C5")

    '''在Flask-SQLAlchemy中，插入、修改、删除操作，均由数据库会话管理。会话用db.session表示'''
    '''session 记录对象任务 '''
    db.session.add_all([role, r0, r1, role1,
                        role2, role3, rol1, rol2, rol3, rh1, rh2, rh3, rh4, rh5, r2, r3, r5, r6, r7, r8, r9, r10, r11, r12
                        ])
    '''提交任务到数据库中'''
    db.session.commit()
