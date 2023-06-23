import Vue from 'vue';
import { createStore } from 'vuex';
import axios from 'axios';

const state = {
  user: null,
  weather: null
};

export default createStore({
  state,
  getters: {
    user: (state) => {
      return state.user;
    },
    weather: (state) => {
      return state.weather;
    }
  },
  actions: {
    user(context, user) {
      context.commit('user', user);
    },
    setWeather(context, weather) {
      context.commit('setWeather', weather);
    },
  },
  mutations: {
    user(state, user) {
      state.user = user;
    },
    setWeather(state, weather) {
      state.weather = weather;
    }
  }
});

/*const store = new Vuex.Store({
  state,
  getters: {
    user: (state) => {
      return state.user;
    }
  },
  actions: {
    user(context, user) {
      context.commit('user', user);
    }
  },
  mutations: {
    user(state, user) {
      state.user = user;
    }
  }
});


export default store;*/
