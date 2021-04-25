import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: '',
    radio: '',
  },
  mutations: {
    set_token(state, token) {
      state.token = token
      window.sessionStorage.token = token //设置浏览器的token
    },
    set_radio(state, radio) {
      state.radio = radio
    },
    del_token(state) {
      state.token = ''
      window.sessionStorage.removeItem('token')
    }
  },
  actions: {
  },
  modules: {
  }
})
