import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    user: {
      id: '',
      token: '',
      email: '',
      newsletter: false
    }
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
});

export default store;
