import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import TheLunch from '../views/Thelunch.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home', // name => app name 처럼 {name: 'Home'} 
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path : '/lunch',
    name: 'TheLunch',
    component : TheLunch,

  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
