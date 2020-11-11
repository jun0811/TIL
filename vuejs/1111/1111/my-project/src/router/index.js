import Vue from 'vue'
import VueRouter from 'vue-router'
import Lunch from '@/components/Lunch.vue'
import Lotto from '@/components/Lotto'

Vue.use(VueRouter)

const routes = [
  {
    path:'/',
    name : 'lunch',
    component: Lunch
  },
  {
    path:'/lotto',
    name : 'lotto',
    component :Lotto
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
