import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import edit from '@/pages/edit'
import home from '@/pages/home'
import fed from '@/pages/fed.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },
    {
      path: '/edit',
      name: 'edit',
      component: edit
    },
    {
      path: '/fed',
      name: 'fed',
      component: fed
    }
  ]
})
