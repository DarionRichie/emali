// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from "axios"
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.config.productionTip = false
Vue.prototype.$axios = axios
Vue.use(ElementUI);
//全局进行挂载啊
/* eslint-disable no-new */
router.beforeEach((to, from, next) => {
  // ...
  console.log(to)
  console.log(from)
  
  next()
  
})
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
