/*import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:5000/', 'http://localhost:5001/', 'http://localhost:5002/';
axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('token');*/

import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:5000/';
axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('token');

// Add a request interceptor
axios.interceptors.request.use((config) => {
  if (config.baseURL === 'http://localhost:5001'){
    config.baseURL = 'http://localhost:5001/';
  }
  if (config.baseURL === 'http://localhost:5002') {
    config.baseURL = 'http://localhost:5002/';
  }
  return config;
});