<template>
  <div class="w">
    <h1>欢迎来到学生宿舍管理系统</h1>
    <el-carousel :interval="2000" type="card">
      <el-carousel-item v-for="item in list" :key="item.id" class="autoimg">
        <img :src="item.url" alt="" />
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
export default {
  data() {
    return {
      list: [
        { url: require("../../../assets/banner1.png") },
        { url: require("../../../assets/banner2.png") },
        { url: require("../../../assets/banner3.jpg") },
      ],
    };
  },
};
</script>
<style scoped lang="less">
/* @import url(); 引入css类 */
.w{
    text-align: center;
    h1{
        font-size: 20px;
        color: #fff;

    }
}
.autoimg {
  img {
    width: 100%;
    height: 100%;
  }
}

</style>