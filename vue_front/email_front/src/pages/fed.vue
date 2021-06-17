<template>
  <div>
      <div><el-progress type="circle" :percentage="100" status="success" style="margin-top:40px;">
          
      </el-progress>
      <div>
      <el-button type="primary" style="margin-top:40px;">联邦学习同步进度</el-button>

      </div>
      </div>
      <div><el-progress type="circle" :percentage="80" status="success" style="margin-top:40px;"></el-progress>
      <div>
      <el-button type="primary" style="margin-top:40px;">本地训练进度</el-button>

      </div>
      </div>
      <div style="margin-top:30px;">
          <el-button type="danger" style="margin-top:40px;">本次参与训练列表</el-button>
          <el-table
      :data="tableData"
      style="width: 60%;margin: auto">
      <el-table-column
        prop="date"
        label="日期"
        width="400">
      </el-table-column>
      <el-table-column
        prop="name"
        label="来源"
        width="400">
      </el-table-column>
      <el-table-column
        prop="address"
        label="标题">
      </el-table-column>
    </el-table>
      </div>

      
  </div>
</template>
// 这里主要用作邮件的编写部分，甚至可以加入一个附件模块部分
<script scoped>
// 引入 wangEditor
export default {
  data() {
    return {
     tableData: [{
            date: '2021-05-02',
            name: 'do-not-reply@stackoverflow.email',
            address: 'new token ,blockchain'
          }, {
            date: '2021-05-16',
            name: 'support@codepen.io',
            address: 'The codepan spark'
          }, {
            date: '2021-05-18',
            name: '32x9@7t71.cn',
            address: '有各行业多余 (普票)  (专票) 等其他类票据，'
          }, {
            date: '2021-05-25',
            name: 'xiaoyuan@mail.wisdomore.net',
            address: '尊敬的王同学【智联推荐】【保利成都2021年暑期实习保送生招聘】'
          }]
    };
  },
  
  methods: {
    
  },
  
  
};
</script>

<style scoped>

</style>