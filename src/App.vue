<template>
  <div id="app">
    <Nav />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import Nav from './components/Nav.vue'
import axios from 'axios'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    Nav,
    Footer
  },

  async created() {
    const res = await axios.get('user');

    this.$store.dispatch('user',res.data);
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Fira+Sans:400,500,600,700,800');

* {
  box-sizing: border-box;
}

body {
  /*background-color: #c7d6eb;*/
  min-height: 100vh;
  display: flex;
  background: linear-gradient(to bottom,#FBAE21, #FF00FF, #35A2CB, #80F4FF,  #4E1F3C);
  font-weight: 400;
  font-family: 'Fira Sans', sans-serif;
  overflow: auto;
  scrollbar-width: thin;
  scrollbar-color: #999999 #f5f5f5;
}

h1, h2, h3, h4, h5, h6, label, span {
  font-weight: 500;
  font-family: 'Fira Sans', sans-serif;
}

/*body, html, #app, #root, .auth-wrapper {
  width: 100%;
  height: 100%;
}*/

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  width: 100%;
}

/*.navbar-light {
  background-color: rgb(197, 169, 223);
  box-shadow: 8px 14px 80px rgba(34, 35, 58, 0.2);
  height: 35px;
}*/

.auth-wrapper {
  display: flex;
  justify-content: center;
  flex-direction: column;
  text-align: left;
  width: 100%;
  height: 100%;
}

.auth-inner {
  width: 450px;
  margin: auto;
  background: #ffffff;
  box-shadow: 8px 14px 80px rgba(34, 35, 58, 0.2);
  padding: 40px 55px 45px 55px;
  border-radius: 15px;
  transition: all .3s;
}

.auth-wrapper .form-control:focus {
  border-color: #167bff;
  box-shadow: none;
}

.auth-wrapper h3 {
  text-align: center;
  margin: 0;
  line-height: 1;
  padding-bottom: 20px;
}

.custom-control-label {
  font-weight: 400;
}

.forgot-password,
.forgot-password a {
  text-align: right;
  font-size: 13px;
  padding-top: 10px;
  color: #7f7d7d;
  margin: 0;
}

</style>
