<template>
  <div>
    <!-- 面包屑导航区 -->
    <el-card>
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>宿舍管理</el-breadcrumb-item>
        <el-breadcrumb-item>宿舍列表</el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 添加楼宇按钮和删除楼宇按钮 -->
      <div class="btn">
        <el-button type="primary" @click="addDialogVisible = true"
          >添加楼宇</el-button
        >
        <div v-for="(item, index) in loulist" :key="index">
          <el-button @click="gettext(item.house_id)">{{
            item.house_id
          }}</el-button>
        </div>
        <el-button type="danger" @click="deleteDialogVisible = true"
          >删除楼宇</el-button
        >
      </div>
    </el-card>
    <!-- 添加楼宇对话框 -->
    <el-dialog
      title="添加楼宇"
      :visible.sync="addDialogVisible"
      width="30%"
      @close="addDialogClose"
    >
      <el-form
        :model="addForm"
        :rules="addFormRules"
        ref="addFormRef"
        label-width="70px"
      >
        <el-form-item label="楼宇" prop="housename">
          <!-- <el-input v-model="addForm.housename" maxlength="3"></el-input> -->
          <el-input-number
            v-model="addForm.housename"
            :min="1"
            :max="20"
            label="楼宇号"
            size="medium"
          ></el-input-number>
          <p>{{ "C" + addForm.housename }}</p>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="addDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addhousenum">确 定</el-button>
      </span>
    </el-dialog>
    <!-- 编辑楼宇对话框 -->
    <el-dialog
      title="添加楼宇"
      :visible.sync="editDialogVisible"
      width="30%"
      @close="editDialogClose"
    >
      <el-form
        :model="editForm"
        :rules="deleteFormRules"
        ref="editFormRef"
        label-width="70px"
      >
        <el-form-item label="宿舍号" prop="dormitory_id">
          <el-input v-model="editForm.dormitory_id" disabled></el-input>
        </el-form-item>
        <el-form-item label="宿舍楼">
          <el-input v-model="editForm.floor_id" disabled></el-input>
        </el-form-item>
        <el-form-item label="楼层" prop="ceng_num">
          <el-radio-group v-model="editForm.ceng_num">
            <el-radio-button label="1"></el-radio-button>
            <el-radio-button label="2"></el-radio-button>
            <el-radio-button label="3"></el-radio-button>
            <el-radio-button label="4"></el-radio-button>
            <el-radio-button label="5"></el-radio-button>
            <el-radio-button label="6"></el-radio-button>
            <el-radio-button label="7"></el-radio-button>
            <el-radio-button label="8"></el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="床位">
          <el-radio-group v-model="editForm.bed_pid">
            <el-radio-button label="1"></el-radio-button>
            <el-radio-button label="2"></el-radio-button>
            <el-radio-button label="3"></el-radio-button>
            <el-radio-button label="4"></el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="价格">
          <el-radio-group v-model="editForm.price">
            <el-radio-button label="1000"></el-radio-button>
            <el-radio-button label="1500"></el-radio-button>
            <el-radio-button label="2000"></el-radio-button>
          </el-radio-group>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="editDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="btn_edit_dormitory_msg"
          >确 定</el-button
        >
      </span>
    </el-dialog>
    <!-- 删除楼宇对话框 -->
    <el-dialog
      title="删除楼宇"
      :visible.sync="deleteDialogVisible"
      width="50%"
      @close="deleteDialogClose"
    >
      <el-form
        :model="deleteForm"
        :rules="deleteFormRules"
        ref="deleteFormRef"
        label-width="70px"
      >
        <el-form-item label="楼层" prop="housename">
          <el-radio-group v-model="deleteForm.housename">
            <el-radio-button
              v-for="item in loulist"
              :key="item.id"
              :label="item.house_id"
            ></el-radio-button>
          </el-radio-group>
        </el-form-item>
        <p>{{ deleteForm.housename }}</p>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="deleteDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="deletehouse">确 定</el-button>
      </span>
    </el-dialog>
    <!-- 添加宿舍信息对话框 -->
    <el-dialog
      title="添加宿舍"
      :visible.sync="addmsgDialogVisible"
      width="45%"
      @close="addmsgDialogClose"
    >
      <el-form
        :model="addmsgForm"
        :rules="addmsgFormRules"
        ref="addmsgFormRef"
        label-width="70px"
      >
        <el-form-item label="宿舍号" prop="dormitory_id">
          <el-input v-model="addmsgForm.dormitory_id" maxlength="3"></el-input>
        </el-form-item>
        <el-form-item label="楼层" prop="ceng_num">
          <el-radio-group v-model="addmsgForm.ceng_num">
            <el-radio-button label="1"></el-radio-button>
            <el-radio-button label="2"></el-radio-button>
            <el-radio-button label="3"></el-radio-button>
            <el-radio-button label="4"></el-radio-button>
            <el-radio-button label="5"></el-radio-button>
            <el-radio-button label="6"></el-radio-button>
            <el-radio-button label="7"></el-radio-button>
            <el-radio-button label="8"></el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="床位" prop="bed_pid">
          <el-radio-group v-model="addmsgForm.bed_pid">
            <el-radio-button label="1"></el-radio-button>
            <el-radio-button label="2"></el-radio-button>
            <el-radio-button label="3"></el-radio-button>
            <el-radio-button label="4"></el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="价格" prop="price">
          <el-radio-group v-model="addmsgForm.price">
            <el-radio-button label="1000"></el-radio-button>
            <el-radio-button label="1500"></el-radio-button>
            <el-radio-button label="2000"></el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="宿舍楼" prop="floor_id">
          <el-select
            v-model="addmsgForm.floor_id"
            clearable
            placeholder="请选择"
          >
            <el-option
              v-for="(item, index) in loulist"
              :key="index"
              :label="item.house_id"
              :value="index + 1"
            >
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="addmsgDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="add_dormitory_msg">确 定</el-button>
      </span>
    </el-dialog>
    <!-- 分配宿舍对话框 -->
    <el-dialog
      title="宿舍详情"
      :visible.sync="addstuDialogVisible"
      width="45%"
      @close="addstuDialogClose"
    >
      <el-form :model="addstuForm" ref="addstuFormRef" label-width="70px">
        <el-table :data="choicehouselist" border stripe>
          <el-table-column
            label="学号"
            sortable
            prop="stu_id"
          ></el-table-column>
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
          <el-table-column
            label="电话"
            sortable
            prop="stu_phone"
          ></el-table-column>
          <el-table-column
            label="年级"
            sortable
            prop="stu_grader"
          ></el-table-column>
          <el-table-column
            label="学院"
            sortable
            prop="stu_depart"
          ></el-table-column>
        </el-table>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="addstuDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addstuDialogVisible = false"
          >确 定</el-button
        >
      </span>
    </el-dialog>
    <el-card>
      <!-- 搜索添加区 -->
      <el-row :gutter="20">
        <el-col :span="8">
          <el-input placeholder="请输入内容" v-model="query" clearable>
            <el-button slot="append" icon="el-icon-search" @click="getsearch"
              >模糊搜索</el-button
            >
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button type="primary" @click="addmsgDialogVisible = true"
            >添加宿舍</el-button
          >
        </el-col>
      </el-row>
      <!-- 表格区 -->
      <el-table :data="isshow ? textlist : searchlist" border stripe>
        <el-table-column label="Id" sortable type="index"></el-table-column>
        <el-table-column
          label="宿舍号"
          sortable
          prop="dormitory_id"
        ></el-table-column>
        <el-table-column
          label="宿舍楼"
          sortable
          prop="floor_id"
        ></el-table-column>
        <el-table-column
          label="楼层"
          sortable
          prop="ceng_num"
        ></el-table-column>
        <el-table-column label="价格" sortable prop="price"></el-table-column>
        <el-table-column label="床位" sortable>
          <template v-slot="scope">
            <el-tag effect="dark">{{ scope.row.bed_pid }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="实际人数" sortable>
          <template v-slot="scope">
            <el-tag type="success" effect="dark">{{ scope.row.people }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="是否满人" sortable>
          <template v-slot="scope">
            <el-switch
              v-model="scope.row.isfull"
              active-color="#13ce66"
              inactive-color="#ff4949"
              active-value="1"
              inactive-value="0"
              active-text="是1"
              inactive-text="否0"
              disabled
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
                @click="edit_dormitory_msg(scope.row.nid)"
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
                @click="delete_dormitory_msg(scope.row.nid)"
              >
              </el-button>
            </el-tooltip>
            <el-tooltip
              effect="dark"
              content="宿舍详情"
              placement="top"
              :enterable="false"
            >
              <el-button
                type="danger"
                icon="el-icon-setting"
                size="mini"
                @click="choicehouse(scope.row.nid)"
              >
              </el-button>
            </el-tooltip>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "dormitory",
  data() {
    return {
      query: "", //input绑定
      searchlist: [],
      newListLength: "",
      info1: {},
      loulist: [],
      textlist: [],
      stulist: [],
      choicehouselist: [],
      addDialogVisible: false,
      deleteDialogVisible: false,
      editDialogVisible: false,
      addmsgDialogVisible: false,
      addstuDialogVisible: false,
      addForm: {
        housename: "",
      },
      addmsgForm: {
        dormitory_id: "",
        ceng_num: "",
        bed_pid: "",
        price: "",
        floor_id: "",
      },
      addstuForm: {},
      editForm: {},
      deleteForm: {
        housename: "",
      },
      addFormRules: {
        housename: [{ required: true, message: "请输入C几", trigger: "blur" }],
      },
      deleteFormRules: {
        housename: [{ required: true, message: "请输入C几", trigger: "blur" }],
      },
      addmsgFormRules: {
        dormitory_id: [
          { required: true, message: "请输入宿舍号", trigger: "blur" },
        ],
        ceng_num: [
          { required: true, message: "请输入楼层数", trigger: "blur" },
        ],
        bed_pid: [{ required: true, message: "请输入床位", trigger: "blur" }],
        price: [{ required: true, message: "请输入价格", trigger: "blur" }],
        floor_id: [{ required: true, message: "请输入C几", trigger: "blur" }],
      },
      isshow: true,
      btn_index: "",
    };
  },
  components: {},
  //生命周期 - 创建完成（访问当前this实例）
  created() {},
  //生命周期 - 挂载完成（访问DOM元素）
  mounted() {
    this.getsearch();
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
    getsearch() {
      this.$http
        .post(
          "message/getmessage",
          this.$qs.stringify({
            num: this.query,
          })
        )
        .then((res) => {
          // console.log(res.data);
          if (res.data.meta.status !== 200)
            return this.$message.error("模糊查询-楼的信息请求失败");
          this.searchlist = res.data.data;
          // console.log(res.data.data)
          this.$notify.success("模糊查询-楼的信息请求成功");
          this.update_count()
          this.isshow = false; //默认先点击搜索框
          this.btn_index = ""; //当这个index不为空时，防止在模糊搜索时候跳转到index里
        });
    },
    getloulist() {
      this.$http.get("message/getnum").then((res) => {
        // console.log(res.data);
        if (res.data.meta.status !== 200)
          return this.$message.error("C1-C.X请求失败");
        this.loulist = res.data.data;
        // this.$bus.$emit("loudata",this.loulist)
          this.update_count()
        this.$notify.success("C1-C.X信息请求成功");
      });
    },

    gettext(index) {
      if (index === "") {
        console.log("index为空");
        this.getsearch(); //解决了未点击楼宇时，在模糊搜索里不会跳转
        return;
      } else {
        this.btn_index = index;
        this.$http.post(`message/getmsg/${index}`).then((res) => {
          if (res.data.meta.status !== 200 || res.data.data == "")
            return this.$message.error("尚未查询到当前宿舍楼的信息");
          this.isshow = true;
          this.textlist = res.data.data;
            this.update_count()
          this.$notify.success("每一个宿舍楼的宿舍的信息请求成功");
        });
      }
    },
    addDialogClose() {
      this.$refs.addFormRef.resetFields();
    },
    addhousenum() {
      this.$refs.addFormRef.validate((valid) => {
        if (!valid) return;
        this.$http
          .post(
            "message/addnum",
            this.$qs.stringify({
              num: "C" + this.addForm.housename,
            })
          )
          .then((res) => {
            if (res.data.meta.status !== 200) {
              return this.$message.error("添加楼宇失败！");
            }
            this.$notify.success("添加楼宇成功！");
            this.addDialogVisible = false;
            this.getloulist();
          });
      });
    },
    deleteDialogClose() {
      this.$refs.deleteFormRef.resetFields();
    },
    deletehouse() {
      this.$refs.deleteFormRef.validate((valid) => {
        if (!valid) return;
        this.$http
          .put(`message/addnum/${this.deleteForm.housename}`)
          .then((res) => {
            console.log(res.data)
            if (res.data.meta.status !== 200) {
              return this.$message.error("删除楼宇失败！");
            }
            this.$notify.success("删除楼宇成功！");
            this.deleteDialogVisible = false;
            this.getloulist();
          });
      });
    },
    getsutlist() {
      this.$http.get("student/info").then((res) => {
        this.stulist = res.data.data;
      });
    },
    delete_dormitory_msg(id) {
      this.$confirm("此操作将永久删除该宿舍信息, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then((res) => {
          this.$http.put(`message/deletenum/${id}`).then((res) => {
            if (res.data.meta.status !== 200) {
              return this.$message.error("删除宿舍信息失败！");
            }
            this.$notify.success("删除宿舍信息成功！");
            this.gettext(this.btn_index);
          });
        })
        .catch((err) => {
          this.$message.info("已取消删除");
        });
    },
    edit_dormitory_msg(id) {
      this.$http.post(`message/editnum/${id}`).then((res) => {
        if (res.data.meta.status !== 200) {
          return this.$message.error("编辑宿舍信息失败！");
        }
        this.editForm = res.data.data[0];
        this.editDialogVisible = true;
        this.$notify.success("编辑宿舍信息获取成功！");
      });
    },

    //点击分配宿舍按钮
    choicehouse(id) {
      this.$http
        .post(
          "student/get_student_dormitory",
          this.$qs.stringify({
            num: id,
          })
        )
        .then((res) => {
          if (res.data.meta.status !== 200) {
            return this.$message.error("联合查询获取信息失败！");
          }
          this.choicehouselist = res.data.data;
          this.addstuDialogVisible = true;
          this.$notify.success("联合查询信息获取成功！");
        });
    },
    btn_edit_dormitory_msg() {
      this.$refs.editFormRef.validate((valid) => {
        if (!valid) return;
        this.$http
          .post(
            "message/commiteditnum",
            this.$qs.stringify({
              num: this.editForm,
            })
          )
          .then((res) => {
            if (res.data.meta.status == 202) {
              return this.$message.error("提交失败：人多床少！");
            }
            if (res.data.meta.status !== 200) {
              return this.$message.error("提交编辑宿舍信息失败！");
            }
                      this.update_count()
            this.gettext(this.btn_index); //点击楼宇时候得到id值才执行的，防止跳转，如果没点楼宇就不执行
            this.editDialogVisible = false;
            this.$notify.success("提交编辑宿舍信息成功！");
          });
      });
    },
    editDialogClose() {
      this.$refs.editFormRef.resetFields();
    },
    addmsgDialogClose() {
      this.$refs.addmsgFormRef.resetFields();
    },
    add_dormitory_msg() {
      this.$refs.addmsgFormRef.validate((valid) => {
        if (!valid) return;
        this.$http
          .post(
            "message/addmsg",
            this.$qs.stringify({
              num: this.addmsgForm,
            })
          )
          .then((res) => {
            if (res.data.meta.status !== 200) {
              return this.$message.error("添加新的宿舍失败！");
            }
            this.gettext(this.btn_index);
            this.addmsgDialogVisible = false;
            this.$notify.success("添加新的宿舍成功！");
          });
      });
    },
    addstuDialogClose() {
      this.$refs.addstuFormRef.resetFields();
    },
  },
};
</script>
<style lang="less" scoped>
/* @import url(); 引入css类 */
.btn {
  margin-block-end: 15px;

  .el-button {
    margin: 0px 6px;
  }

  div {
    display: inline-flex;
  }
}
</style>