<template>
  <div>
    <!-- 面包屑导航区 -->
    <el-card>
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>学生管理</el-breadcrumb-item>
        <el-breadcrumb-item>学生信息</el-breadcrumb-item>
      </el-breadcrumb>

      <!-- 搜索区 -->
      <el-row :gutter="20">
        <el-col :span="8">
          <el-input placeholder="请输入内容" v-model="querystu" clearable>
            <el-button slot="append" icon="el-icon-search" @click="getsearch"
              >模糊搜索</el-button
            >
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button type="primary" @click="add_stu_DialogVisible = true"
            >添加学生</el-button
          >
        </el-col>
      </el-row>
    </el-card>
    <el-card>
      <!--表格区 -->
      <el-table :data="isshow ? stulist : searchlist" border stripe>
        <el-table-column label="Id" sortable type="index"></el-table-column>
        <el-table-column label="学号" sortable prop="stu_id"></el-table-column>
        <el-table-column
          label="姓名"
          sortable
          prop="stu_name"
        ></el-table-column>
        <el-table-column
          label="性别"
          sortable
          prop="stu_gender"
        ></el-table-column>
        <el-table-column label="年龄" sortable prop="stu_age"></el-table-column>
        <el-table-column
          label="电话"
          sortable
          prop="stu_phone"
        ></el-table-column>
        <el-table-column
          label="年级"
          sortable
          prop="stu_grade"
        ></el-table-column>
        <el-table-column
          label="学院"
          sortable
          prop="stu_depart"
        ></el-table-column>
        <el-table-column
          label="宿舍楼"
          sortable
          prop="stu_dormitory_id"
        ></el-table-column>
        <el-table-column
          label="宿舍"
          sortable
          prop="stu_dormitory"
        ></el-table-column>
        <el-table-column label="操作" width="180px">
          <template v-slot="scope">
            <el-tooltip
              effect="dark"
              content="编辑"
              placement="top"
              :enterable="false"
            >
              <el-button
                type="primary"
                icon="el-icon-edit"
                size="mini"
                @click="edit_student_msg(scope.row.stu_id)"
              >
              </el-button>
            </el-tooltip>
            <el-tooltip
              effect="dark"
              content="删除"
              placement="top"
              :enterable="false"
            >
              <el-button
                type="danger"
                icon="el-icon-delete"
                size="mini"
                @click="delete_student_msg(scope.row.stu_id)"
              >
              </el-button>
            </el-tooltip>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
    <!-- 添加学生信息对话框 -->
    <el-dialog
      title="添加学生"
      :visible.sync="add_stu_DialogVisible"
      width="30%"
      @close="add_stu_DialogClose"
    >
      <el-form
        :model="addstuForm"
        ref="addstuFormRef"
        :rules="add_stu_FormRules"
        label-width="70px"
      >
        <el-form-item label="学号" prop="stu_id">
          <el-input
            v-model="addstuForm.stu_id"
            :min="1"
            :max="20"
            size="medium"
          ></el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="stu_name">
          <el-input v-model="addstuForm.stu_name" size="medium"></el-input>
        </el-form-item>
        <el-form-item label="性别" prop="stu_gender">
          <el-radio-group v-model="addstuForm.stu_gender">
            <el-radio-button label="男"></el-radio-button>
            <el-radio-button label="女"></el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="年龄" prop="stu_age">
          <el-input
            v-model.number="addstuForm.stu_age"
            size="medium"
          ></el-input>
        </el-form-item>
        <el-form-item label="电话" prop="stu_phone">
          <el-input
            v-model="addstuForm.stu_phone"
            maxlength="11"
            size="medium"
          ></el-input>
        </el-form-item>
        <el-form-item label="年级" prop="stu_grade">
          <el-radio-group v-model="addstuForm.stu_grade">
            <el-radio-button label="2018"></el-radio-button>
            <el-radio-button label="2019"></el-radio-button>
            <el-radio-button label="2020"></el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="学院" prop="stu_depart">
          <el-radio-group v-model="addstuForm.stu_depart">
            <el-radio-button label="计算机学院"></el-radio-button>
            <el-radio-button label="电气学院"></el-radio-button>
            <el-radio-button label="管理学院"></el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="宿舍楼" prop="stu_dormitory_id">
          <el-select
            v-model="addstuForm.stu_dormitory_id"
            clearable
            placeholder="请选择"
          >
            <el-option
              v-for="(item, index) in loulist"
              :key="index"
              :label="item.house_id"
              :value="item.house_id"
              @click.native="get_dormitory_id(item.house_id)"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="宿舍" prop="stu_dormitory">
          <el-select
            v-model="addstuForm.stu_dormitory"
            clearable
            placeholder="请选择"
          >
            <el-option
              v-for="(item, index) in dormitorylist"
              :key="index"
              :label="item.dormitory_id"
              :value="item.dormitory_id"
            >
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="add_stu_DialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="add_stumag">确 定</el-button>
      </span>
    </el-dialog>
    <!-- 编辑学生信息对话框 -->
    <el-dialog
      title="编辑学生"
      :visible.sync="editstudentDialogVisible"
      width="30%"
      @close="editstudentDialogClose"
    >
      <el-form
        :model="editstuForm"
        :rules="add_stu_FormRules"
        ref="editstuFormRef"
        label-width="70px"
      >
        <el-form-item label="学号">
          <el-input v-model="editstuForm.stu_id" disabled></el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="stu_name">
          <el-input v-model="editstuForm.stu_name"></el-input>
        </el-form-item>
        <el-form-item label="性别" prop="stu_gender">
          <el-radio-group v-model="editstuForm.stu_gender">
            <el-radio-button label="男"></el-radio-button>
            <el-radio-button label="女"></el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="年龄" prop="stu_age">
          <el-input v-model="editstuForm.stu_age"></el-input>
        </el-form-item>
        <el-form-item label="电话" prop="stu_phone">
          <el-input v-model="editstuForm.stu_phone" maxlength="11"></el-input>
        </el-form-item>
        <el-form-item label="年级" prop="stu_grade">
          <el-radio-group v-model="editstuForm.stu_grade">
            <el-radio-button label="2018"></el-radio-button>
            <el-radio-button label="2019"></el-radio-button>
            <el-radio-button label="2020"></el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="学院" prop="stu_depart">
          <el-radio-group v-model="editstuForm.stu_depart">
            <el-radio-button label="计算机学院"></el-radio-button>
            <el-radio-button label="电气学院"></el-radio-button>
            <el-radio-button label="管理学院"></el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="宿舍楼" prop="stu_dormitory_id">
          <el-select
            v-model="editstuForm.stu_dormitory_id"
            clearable
            placeholder="请选择"
          >
            <el-option
              v-for="(item, index) in loulist"
              :key="index"
              :label="item.house_id"
              :value="item.house_id"
              @click.native="get_dormitory_id(item.house_id)"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="宿舍" prop="stu_dormitory">
          <el-select
            v-model="editstuForm.stu_dormitory"
            clearable
            placeholder="请选择"
          >
            <el-option
              v-for="(item, index) in dormitorylist"
              :key="index"
              :label="item.dormitory_id"
              :value="item.dormitory_id"
            >
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="editstudentDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="btn_edit_student_msg"
          >确 定</el-button
        >
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { checkMobile, checkName, checkAge } from "../../../../utils/check";
export default {
  name: "message",
  data() {
    return {
      stulist: [],
      addstuForm: {
        stu_name: "",
        stu_id: "",
        stu_age: "",
        stu_phone: "",
        stu_gender: "",
        stu_depart: "",
        stu_grade: "",
        stu_dormitory: "",
        stu_dormitory_id: "",
      },
      querystu: "", //input搜索框
      searchlist: [],
      loulist: [],
      dormitorylist: [],
      add_stu_DialogVisible: false,
      add_stu_FormRules: {
        stu_name: [
          { required: true, message: "请输入名字", trigger: "blur" },
          { min: 1, max: 5, message: "长度在 1 到 5 个字符", trigger: "blur" },
          { validator: checkName, trigger: "blur" },
        ],
        stu_id: [
          { required: true, message: "请输入学号", trigger: "blur" },
          {
            min: 1,
            max: 12,
            message: "长度在 1 到 12 个字符",
            trigger: "blur",
          },
        ],
        stu_gender: [
          { required: true, message: "性别不能为空", trigger: "blur" },
        ],
        stu_age: [
          { required: true, message: "年龄不能为空", trigger: "blur" },
          { validator: checkAge, trigger: "blur" },
        ],
        stu_phone: [
          { required: true, message: "请输入手机号", trigger: "blur" },
          { validator: checkMobile, trigger: "blur" },
        ],
        stu_grade: [
          { required: true, message: "年级不能为空", trigger: "blur" },
        ],
        stu_depart: [
          { required: true, message: "学院不能为空", trigger: "blur" },
        ],
        stu_dormitory_id: [
          { required: true, message: "宿舍楼不能为空", trigger: "blur" },
        ],
        stu_dormitory: [
          { required: true, message: "宿舍不能为空", trigger: "blur" },
        ],
      },
      editstudentDialogVisible: false,
      editstuForm: {},
      isshow: true,
    };
  },
  components: {},
  //生命周期 - 创建完成（访问当前this实例）
  created() {},
  //生命周期 - 挂载完成（访问DOM元素）
  mounted() {
    this.getsutlist();
    this.getloulist();
  },
  methods: {
    update_count() {
      this.$http.get("message/update").then((res) => {
        // console.log(res.data);
        if (res.data.meta.status !== 200)
          return this.$message.error("更新人数失败");
        this.$notify.success("更新人数成功");
      });
    },
    getloulist() {
      this.$http.get("message/getnum").then((res) => {
        // console.log(res.data);
        if (res.data.meta.status !== 200)
          return this.$message.error("C1-C.X请求失败");
        this.loulist = res.data.data;
        // this.$bus.$emit("loudata",this.loulist)
        this.$notify.success("C1-C.X信息请求成功");
      });
    },
    get_dormitory_id(index) {
      this.btn_index = index;
      this.$http.post(`message/getmsg/${index}`).then((res) => {
        if (res.data.meta.status !== 200)
          return this.$message.error("每一个宿舍楼的宿舍的信息请求失败");
        this.dormitorylist = res.data.data;
        this.$notify.success("每一个宿舍楼的宿舍的信息请求成功");
      });
    },
    //默认获取列表
    getsutlist() {
      this.$http.get("student/info").then((res) => {
        if (res.data.meta.status != 200)
          return this.$message.error("外出信息请求失败");
        if (res.data.data == "")
          return this.$message("尚未搜索到数据，请添加数据");
        this.stulist = res.data.data;
        this.$notify.success("外出信息请求成功");
      });
    },
    getsearch() {
      this.$http
        .post(
          "student/getstumessage",
          this.$qs.stringify({
            num: this.querystu,
          })
        )
        .then((res) => {
          if (res.data.meta.status !== 200)
            return this.$message.error("模糊查询-学生的信息请求失败");
          this.searchlist = res.data.data;
          this.isshow = false;
          this.$notify.success("模糊查询-学生的信息请求成功");
        });
    },
    add_stu_DialogClose() {
      this.$refs.addstuFormRef.resetFields();
    },
    add_stumag() {
      this.$refs.addstuFormRef.validate((valid) => {
        if (!valid) return;
        // console.log(this.addstuForm)
        this.$http
          .post(
            "student/addstumsg",
            this.$qs.stringify({
              num: this.addstuForm,
            })
          )
          .then((res) => {
            if (res.data.meta.status == 202) {
              return this.$message.error("宿舍已经满了！");
            }
            if (res.data.meta.status == 203) {
              return this.$message.error("输入信息有误！");
            }
            if (res.data.meta.status == 204) {
              return this.$message.error("学生的id已经存在！");
            }
            if (res.data.meta.status != 200) {
              return this.$message.error("添加学生失败！");
            }
            this.add_stu_DialogVisible = false;
            this.getsearch();
            this.$notify.success("添加学生成功！");
          });
      });
    },
    edit_student_msg(id) {
      this.$http.post(`student/editnum/${id}`).then((res) => {
        // console.log(res);
        if (res.data.meta.status !== 200) {
          return this.$message.error("编辑宿舍信息获取失败！");
        }
        this.editstuForm = res.data.data[0];
        this.editstudentDialogVisible = true;
        this.$notify.success("编辑宿舍信息获取成功！");
      });
    },
    editstudentDialogClose() {
      this.$refs.editstuFormRef.resetFields();
    },
    btn_edit_student_msg() {
      this.$refs.editstuFormRef.validate((valid) => {
        if (!valid) return;
        this.$http
          .post(
            "student/commiteditnum",
            this.$qs.stringify({
              num: this.editstuForm,
            })
          )
          .then((res) => {
            console.log(res.data);
            if (res.data.meta.status == 202) {
              return this.$message.error("宿舍已经满了！");
            }
            if (res.data.meta.status == 203) {
              return this.$message.error("输入信息有误！");
            }
            if (res.data.meta.status != 200) {
              return this.$message.error("添加学生失败！");
            }
            this.editstudentDialogVisible = false;
                    this.update_count();
            this.getsearch();
    
            this.$notify.success("提交编辑学生信息成功！");
          });
      });
    },
    delete_student_msg(id) {
      this.$confirm("此操作将永久删除该学生信息, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then((res) => {
          this.$http.put(`student/deletenum/${id}`).then((res) => {
            if (res.data.meta.status !== 200) {
              return this.$message.error("删除学生信息失败！");
            }
                        this.update_count();
            this.getsearch();
            this.$notify.success("删除学生信息成功！");
          });
        })
        .catch((err) => {
          this.$message.info("已取消删除");
        });
    },
  },
};
</script>
