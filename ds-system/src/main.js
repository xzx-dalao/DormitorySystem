import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'element-ui/lib/theme-chalk/index.css'
import './assets/css/global.css'
import qs from 'qs' 
Vue.config.productionTip = false 
import ElementUI from 'element-ui';
Vue.use(ElementUI);
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:5000/'
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
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
