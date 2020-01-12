import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '@/views/Index.vue';
  import indexFooter from '@/components/index/indexFooter.vue';
import Browse from '@/views/Browse.vue';
import Reviewed from '@/views/Reviewed.vue';
import Account from '@/views/Account.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'index',
    components:{
      default: Index,
      footer: indexFooter
    }
  },
  {
    path: '/browse',
    name: 'browse',
    component: Browse
  },
  {
    path: '/reviewed',
    name: 'reviewed',
    component: Reviewed
  },
  {
    path: '/account',
    name: 'account',
    component: Account
  }
];

const router = new VueRouter({
  routes
});

export default router
