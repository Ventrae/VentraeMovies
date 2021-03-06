import Vue from 'vue';
import VueRouter from 'vue-router';
import store from '../store/index';

import navbar from '@/components/general/navbar.vue';

import Index from '@/views/Index.vue';
import indexFooter from '@/components/index/indexFooter.vue';

import Movie from '@/views/Movie.vue';
import Browse from '@/views/Browse.vue';
import SearchResults from '@/views/SearchResutls.vue';
import Recommendations from '@/views/Recommendations.vue';
import Account from '@/views/Account.vue';
import Reviews from '@/views/Reviews.vue';

Vue.use(VueRouter);

let enableGuards = true;

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
    beforeEnter(to: any, from: any, next: { (): void; (arg0: { name: string; }): void; }){
      if(enableGuards){
        if(store.state.user.token != ''){
          next();
        }
        else {
          next({name: 'index'});
        }
      }
      else next();
    }
  },
  {
    path: '/search',
    name: 'search',
    components: {
      default: SearchResults,
      navbar: navbar
    },
    beforeEnter(to: any, from: any, next: { (): void; (arg0: { name: string; }): void; }){
      if(enableGuards){
        if(store.state.user.token != ''){
          next();
        }
        else {
          next({name: 'index'});
        }
      }
      else next();
    }
  },
  {
    path: '/recommendations',
    name: 'recommendations',
    components: {
      default: Recommendations,
      navbar: navbar
    },
    beforeEnter(to: any, from: any, next: { (): void; (arg0: { name: string; }): void; }){
      if(enableGuards){
        if(store.state.user.token != ''){
          next();
        }
        else {
          next({name: 'index'});
        }
      }
      else next();
    }
  },
  {
    path: '/reviewed',
    name: 'reviewed',
    components: {
      default: Reviews,
      navbar: navbar
    },
    beforeEnter(to: any, from: any, next: { (): void; (arg0: { name: string; }): void; }){
      if(enableGuards){
        if(store.state.user.token != ''){
          next();
        }
        else {
          next({name: 'index'});
        }
      }
      else next();
    }
  },
  {
    path: '/account',
    name: 'account',
    components: {
      default: Account,
      navbar: navbar
    },
    beforeEnter(to: any, from: any, next: { (): void; (arg0: { name: string; }): void; }){
      if(enableGuards){
        if(store.state.user.token != ''){
          next();
        }
        else {
          next({name: 'index'});
        }
      }
      else next();
    }
  },
  {
    path: '/movie/:id',
    name: 'movie',
    components: {
      default: Movie,
      navbar: navbar
    },
    beforeEnter(to: any, from: any, next: { (): void; (arg0: { name: string; }): void; }){
      if(enableGuards){
        if(store.state.user.token != ''){
          next();
        }
        else {
          next({name: 'index'});
        }
      }
      else next();
    }
  }
];

// @ts-ignore
const router = new VueRouter({
  routes
});

export default router
