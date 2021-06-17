<template>
  <div id="app">

    <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
  
        style="width:100%;background-color: #2c3e50;;margin-top:0px;color:#FFFFFF;"
        @select="handleSelect"
      >
        <el-menu-item index="1"><router-link to="/" style="text-decoration:none">查看邮件</router-link></el-menu-item>
        <el-submenu index="2">
          <template slot="title">编写邮件</template>
          <el-menu-item index="2-1"><router-link to="/edit">写html邮件</router-link></el-menu-item>
          <el-menu-item index="2-2"><router-link to="/edit">编写plain文本邮件</router-link></el-menu-item>
        </el-submenu>
        <el-menu-item index="3"><a href="https://v.xiumi.us/board/v5/5cGk9/296602630" target="_blank"
            >平台介绍</a
          ></el-menu-item>
        <el-menu-item index="4"
          ><router-link to="/fed">联邦学习流程</router-link></el-menu-item
        >
      </el-menu>
      
    <!-- <img src="./assets/logo.png"> -->
    <router-view />
  </div>
</template>

<script>

export default {
  name: "App",
  data() {
      return {
        activeIndex: '1',
        activeIndex2: '1'
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.link {
  color: #409eff;
  font-size: 45px;
}
.title{}
</style>
