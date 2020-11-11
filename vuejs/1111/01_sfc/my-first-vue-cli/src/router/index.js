import Vue from 'vue'
import VueRouter from 'vue-router'
import Lunch from '../components/Lunch.vue'
import Lotto from '@/components/Lotto.vue'
// @는 src부터 시작하는 뜻 ..
Vue.use(VueRouter)

const routes = [
  {
    path : '/lunch',
    name : 'lunch',
    component : Lunch, // 
  },

  {
    //lotto
    path : '/lotto'
    , name : 'lotto'
    , component : Lotto
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
