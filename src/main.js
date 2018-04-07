import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import App from './App.vue'

import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap/dist/css/bootstrap.css'
import './assets/font-awesome-4.7.0/css/font-awesome.min.css'

Vue.use(BootstrapVue)

new Vue({
  el: '#app',
  render: h => h(App)
})
