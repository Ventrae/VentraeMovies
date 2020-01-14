import '@fortawesome/fontawesome-free/css/all.min.css'
import 'bootstrap-css-only/css/bootstrap.min.css'
import 'mdbvue/lib/css/mdb.min.css'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './assets/scss/styles.scss';

// Material-Design-Bootstrap (mdb)
import Vue2TouchEvents from 'vue2-touch-events';
Vue.use(Vue2TouchEvents);
// @ts-ignore
import * as mdbvue from 'mdbvue'
for (const component in mdbvue) {
  Vue.component(component, mdbvue[component])
}


// VueResource
import VueResource from 'vue-resource';
Vue.use(VueResource);



Vue.config.productionTip = false;
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
