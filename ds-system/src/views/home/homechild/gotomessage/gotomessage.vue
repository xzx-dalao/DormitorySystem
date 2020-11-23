<template>
  <div>
    <!-- 面包屑导航区 -->
    <el-card>
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>出入管理</el-breadcrumb-item>
        <el-breadcrumb-item>出入信息</el-breadcrumb-item>
      </el-breadcrumb>
      <el-row :gutter="20">
        <el-col :span="8">
          <el-input placeholder="请输入内容" v-model="querystu" clearable>
            <el-button slot="append" icon="el-icon-search" @click="getsearch"
              >模糊搜索</el-button
            >
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button type="primary" @click="add_goto_DialogVisible = true"
            >添加外出信息</el-button
          >
        </el-col>
      </el-row>
    </el-card>
    <el-card>
      <!-- 添加外出信息对话框 -->
      <el-dialog
        title="添加宿舍"
        :visible.sync="add_goto_DialogVisible"
        width="40%"
        @close="addgotoDialogClose"
      >
        <el-form
          :model="addgotoForm"
          ref="addgotoFormRef"
          label-width="70px"
          :rules="goto_stu_FormRules"
        >
          <el-form-item label="出入时间">
            <el-date-picker
              v-model="addgotoForm.goto_leavetime"
              type="datetime"
              placeholder="选择出门日期时间"
            >
            </el-date-picker>
            <el-date-picker
              v-model="addgotoForm.goto_backtime"
              type="datetime"
              placeholder="选择归来日期时间"
            >
            </el-date-picker>
          </el-form-item>
          <el-form-item label="学号" prop="goto_id">
            <el-input v-model="addgotoForm.goto_id"></el-input>
          </el-form-item>
          <el-form-item label="出行人" prop="goto_name">
            <el-input v-model="addgotoForm.goto_name"></el-input>
          </el-form-item>
          <el-form-item label="电话" prop="goto_phone">
            <el-input
              v-model="addgotoForm.goto_phone"
              maxlength="11"
            ></el-input>
          </el-form-item>
          <el-form-item label="宿舍楼" prop="goto_dormitory">
            <el-select
              v-model="addgotoForm.goto_dormitory"
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
          <el-form-item label="宿舍" prop="goto_dormitory_id">
            <el-select
              v-model="addgotoForm.goto_dormitory_id"
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
          <el-form-item label="备注">
            <el-input
              type="textarea"
              v-model="addgotoForm.goto_reason"
            ></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="add_goto_DialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="add_goto_msg">确 定</el-button>
        </span>
      </el-dialog>
      <!-- 编辑外出信息对话框 -->
      <el-dialog
        title="编辑外出信息"
        :visible.sync="edit_goto_DialogVisible"
        width="40%"
        @close="editgotoDialogClose"
      >
        <el-form
          :model="editgotoForm"
          ref="editgotoFormRef"
          label-width="70px"
          :rules="goto_stu_FormRules"
        >
          <el-form-item label="出入时间">
            <el-date-picker
              v-model="editgotoForm.goto_leavetime"
              type="datetime"
              placeholder="选择出门日期时间"
            >
            </el-date-picker>
            <el-date-picker
              v-model="editgotoForm.goto_backtime"
              type="datetime"
              placeholder="选择归来日期时间"
            >
            </el-date-picker>
          </el-form-item>
          <el-form-item label="学号" prop="goto_id">
            <el-input v-model="editgotoForm.goto_id" disabled></el-input>
          </el-form-item>
          <el-form-item label="出行人" prop="goto_name">
            <el-input v-model="editgotoForm.goto_name"></el-input>
          </el-form-item>
          <el-form-item label="电话" prop="goto_phone">
            <el-input
              v-model="editgotoForm.goto_phone"
              maxlength="11"
            ></el-input>
          </el-form-item>
          <el-form-item label="宿舍楼" prop="goto_dormitory_id">
            <el-select
              v-model="editgotoForm.goto_dormitory_id"
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
          <el-form-item label="宿舍" prop="goto_dormitory">
            <el-select
              v-model="editgotoForm.goto_dormitory"
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
          <el-form-item label="备注">
            <el-input
              type="textarea"
              v-model="editgotoForm.goto_reason"
            ></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="edit_goto_DialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="btn_edit_goto_msg">确 定</el-button>
        </span>
      </el-dialog>
      <!-- 表格 -->
      <el-table :data="isshow ? gotolist : searchlist" border stripe>
        <el-table-column label="Id" sortable type="index"></el-table-column>
        <el-table-column label="学号" sortable prop="goto_id"></el-table-column>
        <el-table-column
          label="姓名"
          sortable
          prop="goto_name"
        ></el-table-column>
        <el-table-column
          label="电话"
          sortable
          prop="goto_phone"
        ></el-table-column>
        <el-table-column
          label="宿舍楼"
          sortable
          prop="goto_dormitory_id"
        ></el-table-column>
        <el-table-column
          label="宿舍"
          sortable
          width="180px"
          prop="goto_dormitory"
        >
        </el-table-column>
        <el-table-column
          label="出外时间"
          sortable
          width="180px"
          prop="goto_leavetime"
        >
        </el-table-column>
        <el-table-column
          label="返回时间"
          sortable
          width="180px"
          prop="goto_backtime"
        >
        </el-table-column>
        <el-table-column
          label="离开原因"
          sortable
          width="180px"
          prop="goto_reason"
        >
        </el-table-column>
        <el-table-column label="是否晚归">
          <template v-slot="scope">
            <el-switch
              v-model="scope.row.goto_islate"
              active-color="#13ce66"
              inactive-color="#ff4949"
              active-value="0"
              inactive-value="1"
              active-text="否0"
              inactive-text="是1"
              @change="userStateChanged(scope.row)"
            >
            </el-switch>
          </template>
        </el-table-column>
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
                @click="edit_goto_msg(scope.row.goto_id)"
              ></el-button>
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
                @click="delete_goto_msg(scope.row.goto_id)"
              ></el-button>
            </el-tooltip>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script>
import {checkMobile,checkName} from '../../../../utils/check'
export default {
  name: "gotomessage",
  data() {

    return {
      addgotoForm: {
        goto_id: "",
        goto_name: "",
        goto_phone: "",
        goto_dormitory: "",
        goto_dormitory_id: "",
        goto_leavetime: "",
        goto_backtime: "",
        goto_reason: "",
      },
      gotolist: [],
      add_goto_DialogVisible: false,
      edit_goto_DialogVisible: false,
      editgotoForm: {},
      querystu: "",
      isshow: true,
      searchlist: [],
      loulist: [],
      dormitorylist: [],
      goto_stu_FormRules: {
        goto_name: [
          { required: true, message: "请输入名字", trigger: "blur" },
          { min: 1, max: 5, message: "长度在 1 到 5 个字符", trigger: "blur" },
           { validator: checkName, trigger: "blur" },
        ],
        goto_id: [
          { required: true, message: "请输入学号", trigger: "blur" },
          {
            min: 1,
            max: 12,
            message: "长度在 1 到 12 个字符",
            trigger: "blur",
          },
        ],
        goto_phone: [
          { required: true, message: "请输入手机号", trigger: "blur" },
          { validator: checkMobile, trigger: "blur" },
        ],
        goto_dormitory_id: [
          { required: true, message: "宿舍不能为空", trigger: "blur" },
        ],
        goto_dormitory: [
          { required: true, message: "宿舍楼不能为空", trigger: "blur" },
        ],
      },
    };
  },
  components: {},
  //生命周期 - 创建完成（访问当前this实例）
  created() {},
  //生命周期 - 挂载完成（访问DOM元素）
  mounted() {
    this.get_gotomsg();
    this.getloulist(); //获取C.x宿舍楼信息
  },
  methods: {
    //得到c.x的
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
    //得到c.x的楼下的宿舍
    get_dormitory_id(index) {
      this.btn_index = index;
      this.$http.post(`message/getmsg/${index}`).then((res) => {
        if (res.data.meta.status !== 200)
          return this.$message.error("每一个宿舍楼的宿舍的信息请求失败");
        this.dormitorylist = res.data.data;
        this.$notify.success("每一个宿舍楼的宿舍的信息请求成功");
      });
    },
    userStateChanged(userInfo) {
      this.$http
        .put(`gotomessage/${userInfo.goto_id}/state/${userInfo.goto_islate}`)
        .then((res) => {
          // console.log(res.data);
          if (res.data.meta.status !== 200) {
            return this.$message.error("用户状态更新失败");
          }
          this.$message.success("用户状态更新成功");
        });
    },
    //默认获取列表
    get_gotomsg() {
      this.$http.get("gotomessage/info").then((res) => {
        if (res.data.meta.status != 200)
          return this.$message.error("尚未搜索到任何信息");
        if (res.data.data == "")
          return this.$message("尚未搜索到数据，请添加数据");
        this.gotolist = res.data.data;
        this.$notify.success("外出信息请求成功");
      });
    },
    delete_goto_msg(id) {
      this.$confirm("此操作将永久删除该外出信息, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then((res) => {
          this.$http.put(`gotomessage/deletenum/${id}`).then((res) => {
            // console.log(res.data);
            if (res.data.meta.status !== 200) {
              return this.$message.error("删除外出信息失败！");
            }
            // this.$router.go(0);
            this.getsearch();
            this.$notify.success("删除外出信息成功！");
          });
        })
        .catch((err) => {
          this.$message.info("已取消删除");
        });
    },
    edit_goto_msg(id) {
      this.$http.post(`gotomessage/editnum/${id}`).then((res) => {
        // console.log(res);
        if (res.data.meta.status !== 200) {
          return this.$message.error("编辑宿舍信息获取失败！");
        }
        this.editgotoForm = res.data.data[0];
        this.edit_goto_DialogVisible = true;
        this.$notify.success("编辑宿舍信息获取成功！");
      });
    },
    btn_edit_goto_msg() {
      this.$refs.editgotoFormRef.validate((valid) => {
          // console.log(this.editgotoForm);
        if (!valid) return;
        this.$http
          .post(
            "gotomessage/commiteditnum",
            this.$qs.stringify({
              num: this.editgotoForm,
            })
          )
          .then((res) => {
            // console.log(res.data);
            if (res.data.meta.status == 203) {
              return this.$message.error("输入信息有误！");
            }
            if (res.data.meta.status != 200) {
              return this.$message.error("添加学生失败！");
            }
            this.edit_goto_DialogVisible = false;
            this.getsearch();
            this.$notify.success("提交编辑学生信息成功！");
          });
      });
    },
    editgotoDialogClose() {
      this.$refs.editgotoFormRef.resetFields();
    },
    addgotoDialogClose() {
      this.$refs.addgotoFormRef.resetFields();
    },
    add_goto_msg() {
      this.$refs.addgotoFormRef.validate((valid) => {
        if (!valid) return;
        this.$http
          .post(
            "gotomessage/addstumsg",
            this.$qs.stringify({
              num: this.addgotoForm,
            })
          )
          .then((res) => {
            // console.log(res.data);
            if (res.data.meta.status != 200) {
              return this.$message.error("添加外出信息失败！");
            }
            this.add_goto_DialogVisible = false;
            this.getsearch();
            this.$notify.success("添加外出成功！");
          });
      });
    },
    getsearch() {
      this.$http
        .post(
          "gotomessage/getmessage",
          this.$qs.stringify({
            num: this.querystu,
          })
        )
        .then((res) => {
          // console.log(res.data);
           if (res.data.meta.status !== 200)
            return this.$message.error("模糊查询-外出的信息请求失败");
          this.searchlist = res.data.data;
          this.isshow = false;
          this.$notify.success("模糊查询-外出的信息请求成功");
        });
    },
  },
};
</script>
