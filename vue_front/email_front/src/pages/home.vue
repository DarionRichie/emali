<template>
  <div class="home" style="height: 100%">
    <!-- <el-container>
      <el-aside width="200px" class="aside"
        ><ul v-for="(email, index) in email_list" :key="index">
          <li>{{ email }}</li>
        </ul></el-aside
      >
      <el-main>Main</el-main>
    </el-container> -->

    <el-container style="height: 720px">
      <el-aside width="450px">
        <el-row class="tac" style="margin-left: 0px; width: 400px">
          <el-col :span="12">
            <el-menu
              class="el-menu-vertical-demo"
              @open="handleOpen"
              @close="handleClose"
              style="margin-left: 0px; width: 400px;background-color: #2c3e50;border:none;border-radius:10px;"
            >
              <el-submenu index="1">
                <template slot="title">
                  <i class="el-icon-loading"></i>
                  <span style="color:#ffffff" class="mmmm">未读邮箱</span>
                </template>
                <el-menu-item-group
                  v-for="(email, index) in email_list"
                  :key="index"
                  class="aside"
                >
                  <el-menu-item
                    :index="String(index)"
                    class="aside1 mmmm"
                    style="color: #b3aeae;"
                    @click="getMoreInfo(email.num)"
                    :class="{ lj: isActive(email.num) }"
                    
                    >{{ first_str(email.text) }}</el-menu-item
                  >
                </el-menu-item-group>
              </el-submenu>
              <el-submenu index="2">
                <template slot="title"
                  ><i class="el-icon-check mmmm" ></i><span class="mmmm">已发邮件</span></template
                >
                <el-menu-item-group
                  v-for="(email, index) in email_send"
                  :key="index * 100"
                  class="aside"
                >
                  <el-menu-item
                    :index="String(index)"
                    class="aside1 mmmm"
                    @click="getMoreInfo2(email.num)"
                    >{{ first_str(email.text) }}</el-menu-item
                  >
                </el-menu-item-group>
              </el-submenu>
              <el-submenu index="3">
                <template slot="title"
                  ><i class="el-icon-delete-solid mmmm"></i><span class="mmmm">垃圾邮箱</span></template
                >
                <el-menu-item-group
                  v-for="(email, index) in lj_item"
                  :key="index * 10000"
                  class="aside"
                >
                  <el-menu-item
                    :index="String(index)"
                    @click="getMoreInfo(email.num)"
                    class="aside1 mmmm"
                    :class="{ lj: isActive(email.num) }"
                    
                    >{{ first_str(email.text) }}</el-menu-item
                    
                  >
                </el-menu-item-group>
              </el-submenu>
              <el-menu-item index="4">
                <i class="el-icon-setting mmmm"></i>
                <span slot="title" class="mmmm">所有邮箱</span>
              </el-menu-item>
            </el-menu>
          </el-col>
        </el-row>
      </el-aside>
      <el-main id="box"
        ><div v-html="email_wen">
          <!-- {{email_wen}} -->
        </div>
        <div>
          <ul v-for="(att, index) in attachlist" :key="index">
            <li>
              {{ att }}
            </li>
          </ul>
        </div>
        <div style="">
          <el-tooltip
            class="item"
            effect="dark"
            content="标记为垃圾邮件，自动加入联邦学习训练数据内部"
            placement="top-end"
            
          >
            <el-button type="danger" @click="open1">标记为垃圾邮件</el-button>
          </el-tooltip>
        </div>
      </el-main>
    </el-container>
  </div>
</template>
// 这里主要用作邮件的编写部分，甚至可以加入一个附件模块部分
<script scoped>
import { Loading } from "element-ui";
export default {
  created() {
    this.updateAll();
    this.updateAll_send();
  },
  data() {
    return {
      email_list: [],
      email_wen: "",
      attachlist: [],
      email_send: [],
      lj_list: [],
      lj_item: [],
    };
  },
  methods: {
    updateAll() {
      //这边做垃圾邮件的模拟处理，随机一部分成为对应的垃圾邮件
      let loadingInstance = Loading.service({text:"拼命获取邮件信息",background:"rgba(0, 0, 0, 0.8)"});
      // let loadingInstance = Loading.service({ text: "拼命获取邮件信息" });

      console.log("发起后端邮件请求部分");
      this.$axios.get("http://localhost:5000/getInfo").then((data) => {
        console.log(data.data);

        for (let i = 0; i < data.data.data.length; i++) {
          if (Math.random() > 0.5) {
            this.lj_list.push(String(data.data.key_info[i]));
            this.lj_item.push({
              text: data.data.data[i],
              num: data.data.key_info[i],
            });
          }

          this.email_list.push({
            text: data.data.data[i],
            num: data.data.key_info[i],
          });
        }

        this.$axios
          .get(
            "http://localhost:5000/getDetailInfo?num=" + data.data.key_info[1]
          )
          .then((data) => {
            console.log(data);
            this.email_wen = data.data.html;
            console.log(data.data);
            this.attachlist = data.data.attachments;
            loadingInstance.close();
          })
          .catch(() => {
            loadingInstance.close();
            this.email_wen = "<p><h1>出现错误拉</h1></p>";
          });

        loadingInstance.close();
      });
    },
    isActive(num) {
      return this.lj_list.indexOf(num) > -1;
    },
    updateAll_send() {
      // let loadingInstance = Loading.service({text:"拼命获取邮件信息"});

      console.log("发起后端已经发送邮件请求部分");
      this.$axios.get("http://localhost:5000/getSend").then((data) => {
        console.log(data.data);

        for (let i = 0; i < data.data.data.length; i++) {
          this.email_send.push({
            text: data.data.data[i],
            num: data.data.key_info[i],
          });
        }
      });
    },
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    first_str(str) {
      //   return `${this.firstName} ${this.lastName}`
      str = String(str);
      if (str.length <= 8) {
        return str;
      } else {
        return str.slice(0, 8) + "....";
      }
    },
    getMoreInfo(id) {
      console.log(id);
      let loadingInstance = Loading.service({ text: "拼命获取邮件具体信息" });
      this.$axios
        .get("http://localhost:5000/getDetailInfo?num=" + id)
        .then((data) => {
          console.log(data);
          this.email_wen = data.data.html;
          loadingInstance.close();
        })
        .catch(() => {
          loadingInstance.close();
          this.email_wen = "<p><h1>出现错误拉</h1></p>";
        });
    },
    getMoreInfo2(id) {
      console.log(id);
      let loadingInstance = Loading.service({ text: "拼命获取邮件具体信息" });
      this.$axios
        .get("http://localhost:5000/getDetailInfo_send?num=" + id)
        .then((data) => {
          console.log(data);
          this.email_wen = data.data.html;
          loadingInstance.close();
        })
        .catch(() => {
          loadingInstance.close();
          this.email_wen = "<p><h1>出现错误拉</h1></p>";
        });
    },
    open1() {
        const h = this.$createElement;

        this.$notify({
          title: '拉黑成功',
          message: h('i', { style: 'color: teal'}, '加载进入到本地联邦学习模型路径，优化体验')
        });
      },
  },
  computed: {},
};
</script>

<style scoped>
.home{
  background-color: #2c3e50;
  border:10px 10px 10px 10px solid #2c3e50;
  border-radius: 10px;
  
}
.aside {
  background-color: #2c3e50;
  color: #b3aeae;
}
.aside1 {
  background-color: #2c3e50;
  /* border-top:1px solid #a5c7e9; */
  margin-left: 50px;
  margin-right: 50px;
  color: #b3aeae;
}
.mmmm{
  color:#ffffff;
}

@keyframes animated-border {
  0% {
    box-shadow: 0 0 0 0 #2c3e50;
  }
  100% {
    box-shadow: 0 0 0 2px #2c3e50;
  }
}
#box {
  animation: animated-border 1.5s infinite;
  font-family: Arial;
  font-size: 18px;
  line-height: 30px;
  font-weight: bold;
  color: #1c233d;
  border: 2px solid #2c3e50;
  border-radius: 10px;
  padding: 15px;
  margin-right: 20px;
  background-image: url("https://img-blog.csdnimg.cn/20210617001204489.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDYwNzUyMQ==,size_16,color_FFFFFF,t_70");
}
.lj {
  /* color: red; */
  color: #b3aeae;
}

span:hover{
  color: #000000;
}
</style>
