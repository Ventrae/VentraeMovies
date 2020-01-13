import Vue from 'vue';
import VueRouter from 'vue-router';
import store from '../store/index';

import navbar from '@/components/general/navbar.vue';

import Index from '@/views/Index.vue';
import indexFooter from '@/components/index/indexFooter.vue';

import Movie from '@/views/Movie.vue';

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
    components: {
      default: Browse,
      navbar: navbar
    },
    /*beforeEnter(to: any, from: any, next: { (): void; (arg0: { name: string; }): void; }){
      if(store.state.user.token != ''){
        next();
      }
      else {
        next({name: 'index'});
      }
    }*/
  },
  {
    path: '/reviewed',
    name: 'reviewed',
    components: {
      default: Reviewed,
      navbar: navbar
    },
    /*beforeEnter(to: any, from: any, next: { (): void; (arg0: { name: string; }): void; }){
      if(store.state.user.token != ''){
        next();
      }
      else {
        next({name: 'index'});
      }
    }*/
  },
  {
    path: '/account',
    name: 'account',
    components: {
      default: Account,
      navbar: navbar
    },
    /*beforeEnter(to: any, from: any, next: { (): void; (arg0: { name: string; }): void; }){
      if(store.state.user.token != ''){
        next();
      }
      else {
        next({name: 'index'});
      }
    }*/
  },
  {
    path: '/movie/:id',
    name: 'movie',
    components: {
      default: Movie,
      navbar: navbar
    },
    /*beforeEnter(to: any, from: any, next: { (): void; (arg0: { name: string; }): void; }){
      if(store.state.user.token != ''){
        next();
      }
      else {
        next({name: 'index'});
      }
    }*/
  }
];

// @ts-ignore
const router = new VueRouter({
  routes
});

export default router
