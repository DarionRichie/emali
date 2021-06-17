<template>
  <div class="home">
    <div>
      <h3>发送给谁</h3>
      <el-input v-model="to_addrr"></el-input>
      <h3>主体内容</h3>
      <el-input v-model="subject"></el-input>
    </div>
    <h3>编写邮件主体部分</h3>
    <div id="demo1"></div>
    <button type="button" class="btn" @click="getEditorData">
      获取邮件html
    </button>
    <h3>内容预览</h3>
    <textarea
      name=""
      id=""
      cols="170"
      rows="20"
      readonly
      v-model="editorData"
      style="width: 1180px"
    ></textarea>
    <el-button type="primary" @click="send_email">发送邮件</el-button>
  </div>
</template>
// 这里主要用作邮件的编写部分，甚至可以加入一个附件模块部分
<script scoped>
// 引入 wangEditor
import wangEditor from "wangeditor";
export default {
  data() {
    return {
      editor: null,
      editorData: "",
      to_addrr: "",
      subject:""
    };
  },
  mounted() {
    const editor = new wangEditor(`#demo1`);
    // 配置 onchange 回调函数，将数据同步到 vue 中
    editor.config.onchange = (newHtml) => {
      this.editorData = newHtml;
    };
    // 创建编辑器
    editor.create();
    this.editor = editor;
  },
  methods: {
    getEditorData() {
      // 通过代码获取编辑器内容
      let data = this.editor.txt.html();
      alert(data);
    },
    send_email(){
      alert("发送邮件！！！")
      let data = {
          editorData:this.editorData,
          to_addrr:this.to_addrr,
          subject:this.subject
      }
      this.$axios.post("http://localhost:5000/send_email",data = data).then((data)=>{
          console.log(data)
      })
  }
  },
  beforeDestroy() {
    // 调用销毁 API 对当前编辑器实例进行销毁
    this.editor.destroy();
    this.editor = null;
  },
  
};
</script>

<style scoped>
.home {
  width: 1200px;
  margin: auto;
  position: relative;
}
.btn {
  position: absolute;
  right: 0;
  top: 0;
  padding: 5px 10px;
  cursor: pointer;
}
h3 {
  margin: 30px 0 15px;
}
</style>