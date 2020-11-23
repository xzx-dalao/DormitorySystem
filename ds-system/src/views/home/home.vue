<template>
<div class="home">
    <el-container class="home-container">
        <el-header>
            <div>
                <img src="../../assets/logo.png" alt="" />
                <span class="title">垃圾管理系统</span>
            </div>
            <!-- 顶栏 -->
            <el-button type="info" @click="logout">退出</el-button>
        </el-header>
        <el-container>
            <!-- 侧边栏 -->
            <el-aside :width="iscollapse ? '64px' : '200px'">
                <!-- 折叠 -->
                <div class="toggle-button" @click="toggle">《《《</div>
                <el-menu background-color="#333744" text-color="#fff" active-text-color="#ffd04b" :collapse="iscollapse" :collapse-transition="false" router :unique-opened="true" :default-active="this.$route.path">
                    <!-- router	是否使用 vue-router 的模式，启用该模式会在激活导航时以 index 作为 path 进行路由跳转 -->
                    <!-- 一级菜单 -->
                    <!-- :index是要传字符串 -->
                    <el-submenu :index="String(item.id)" v-for="(item,index) in menulist" :key="index">
                        <template slot="title">
                            <i class="el-icon-location"></i>
                            <span>{{ item.authName }}</span>
                        </template>
                        <!-- 二级菜单 -->

                        <el-menu-item :index="String('/' + subitem.path)" v-for="(subitem,indexs) in item.children" :key="indexs">
                            <template slot="title">
                                <i class="el-icon-menu"></i>
                                <span>{{ subitem.authName }}</span>
                            </template>
                        </el-menu-item>
                    </el-submenu>
                </el-menu>
            </el-aside>
            <el-main>
                <router-view></router-view>
            </el-main>
        </el-container>
    </el-container>
</div>
</template>

<script>
export default {
    name: "home",
    data() {
        return {
            menulist: [],
            iscollapse: false,
        };
    },
    components: {},
    //生命周期 - 创建完成（访问当前this实例）
    created() {},
    //生命周期 - 挂载完成（访问DOM元素）
    mounted() {
        this.getmenulist();
    },
    methods: {
        logout() {
            this.$store.commit('del_token');
            this.$router.push("/login");
        },
        getmenulist() {
            this.$http.get("menus/info").then((res) => {
                if (res.data.meta.status != 200)
                    return this.$message.error('获取菜单栏失败');
                this.menulist = res.data.data;
                this.$notify.success("获取菜单栏成功");
                // console.log(res.data);
            });
        },
        //按钮折叠和展开
        toggle() {
            this.iscollapse = !this.iscollapse;
        },
    },
};
</script>

<style lang="less" scoped>
.title {
    font-size: 30px;
    color: #fff;
}

.home {
    height: 100vh;
}

/* @import url(); 引入css类 */
.home-container {
    height: 100vh;
}

.el-header {
    opacity: 0.9;
    background-color: #373d41;
    display: flex;
    justify-content: space-between;
    padding-left: 0;
    align-items: center;
    font-size: 20px;

    >div {
        display: flex;
        align-items: center;

        img {
            width: 55px;
        }

        span {
            margin-left: 15px;
        }
    }
}

.el-aside {
    background-color: #333744;
    opacity: 0.9;

    .el-menu {
        border-right: none;
    }
}

.el-main {
    background-color: #fff;
    background-image: url("../../assets/1.webp");
    background-size: cover;
}

.toggle-button {
    background-color: #4a5064;
    font-size: 10px;
    line-height: 24px;
    color: #fff;
    text-align: center;
    letter-spacing: 0.2;
    cursor: pointer;
}
</style>
