<template>
  <div class="auth-wrapper">
    <div class="auth-inner">
      <form @submit.prevent="handleSubmit">
        <error v-if="error" :error="error"/>
        <h3>Login to FarmVision</h3>

        <div class="form-group">
          <label>Email</label>
          <input type="email" class="form-control" v-model="email" placeholder="Email"/>
        </div>

        <div class="form-group">
          <label>Password</label>
          <input type="password" class="form-control" v-model="password" placeholder="password"/>
        </div>

        <button class="btn btn-primary btn-block">Login</button>

        <p class="forgot-password text-right">
          <RouterLink to="forgot">Forgot Password</RouterLink>
        </p>
      </form>
    </div>
  </div>
  
</template>

<script>
import axios from 'axios'
import Error from './Error.vue'

export default {
  name: 'Login',
  components: {
    Error
  },
  data () {
    return {
      email: '',
      password: '',
      error: ''
    }
  },

  methods: {
    async handleSubmit() {
      try {
        const res = await axios.post('login', {
          email: this.email,
          password: this.password
        });

        localStorage.setItem('token', res.data.token);
        this.$store.dispatch('user', res.data.user);
        this.$router.push('/');
      }catch (e) {
        this.error = 'Invalid username/password!'
      }
    }
  }
}
</script>

