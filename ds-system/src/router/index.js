import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const login = () => import('../components/login')
const home = () => import('../views/home/home')
const welcome = () => import('../views/home/homechild/welcome')
const dormitory = () => import('../views/home/homechild/dormitory/dormitory')
const gotomessage = () => import('../views/home/homechild/gotomessage/gotomessage')
const message = () => import('../views/home/homechild/stumessage/stumessage')


const routes = [{
  path: '',
  redirect: '/login'
},
{
  path: '/login',
  component: login
},

{
  path: '/home',
  component: home,
  redirect: '/welcome',
  children: [
    {
      path: '/welcome',
      component: welcome,

    },
    {
      path: '/dormitory',
      component: dormitory,

    },
    {
      path: '/gotomessage',
      component: gotomessage,

    },
    {
      path: '/message',
      component: message,

    },
  ]
},

]

const router = new VueRouter({
  // mode: 'history',
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, form, next) => {
  // console.log(window.sessionStorage.getItem('token')===store.state.token)
  if (to.path === '/login') return next();
  if (!window.sessionStorage.getItem('token')) return next('/login')
  else next()

})

export default router
