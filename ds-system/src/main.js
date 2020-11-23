import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'element-ui/lib/theme-chalk/index.css'
import './assets/css/global.css'
import qs from 'qs'
// import vueSwiper from 'vue-awesome-swiper' 
Vue.config.productionTip = false 
// import 'swiper/swiper-bundle.css'
import ElementUI from 'element-ui';
Vue.use(ElementUI);
// Vue.use(vueSwiper)
import axios from 'axios'
axios.defaults.baseURL = 'http://8.129.133.10:5660'
// axios.defaults.baseURL = 'http://127.0.0.1:5000/'
// axios.interceptors.request.use(
//   config=>{
//       if(store.state.token){
//         config.headers['Authorization'] = store.state.token
//       }
//       return config
//   }
// )   
Vue.prototype.$http = axios
Vue.prototype.$qs = qs
// Vue.prototype.$bus = new Vue();
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
