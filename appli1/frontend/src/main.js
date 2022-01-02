import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

// 今後axiosのような別の非同期通信ライブラリに切り替えたくなった場合、この部分を書き換える
Vue.prototype.$http = (url, opts) => fetch(url, opts)

// APIのURLを変更したくなった場合はこの部分を書き換える
Vue.prototype.$httpPosts = 'http://127.0.0.1:8000/appli1/api/posts/'
Vue.prototype.$httpCategories = 'http://127.0.0.1:8000/appli1/api/categories/'

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
