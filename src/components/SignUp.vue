<template>
  <div class="auth-wrapper">
    <div class="auth-inner">
      <form @submit.prevent="handleSubmit">
        <error v-if="error" :error="error"/>
        <h3>Sign Up to FarmVision</h3>
        <div class="form-group">
          <label>First Name</label>
          <input type="text" class="form-control" v-model="firstName" placeholder="First Name" required>
        </div>

        <div class="form-group">
          <label>Last Name</label>
          <input type="text" class="form-control" v-model="lastName" placeholder="Last Name" required>
        </div>

        <div class="form-group">
          <label>Email</label>
          <input type="email" class="form-control" v-model="email" placeholder="Email" required>
        </div>
              
        <div class="form-group">
          <label>Password</label>
          <input type="password" class="form-control" v-model="password" placeholder="Password" required>
        </div>
        <div class="form-group">
          <label>Confirm Password</label>
          <input type="password" class="form-control" v-model="confirmPassword" placeholder="Confirm Password" required>
        </div>

        <div v-if="passwordsMatchError" class="alert alert-danger" role="alert">
          Passwords do not match.
        </div>

        <button class="btn btn-primary btn-block">Sign Up</button>
      </form>

    </div>
  </div>
</template>
  

<script>
import axios from 'axios'
import Error from './Error.vue'

export default {
  name: 'SignUp',
  components: {
    Error
  },
  data() {
    return {
      firstName: '',
      lastName: '',
      email: '',
      password: '',
      confirmPassword: '',
      passwordsMatchError: false,
      error: ''
    }
  },
  methods: {
    async handleSubmit() {
      // Check if passwords match
      if (this.password !== this.confirmPassword) {
        this.passwordsMatchError = true;
        return;
      }

      try {
        await axios.post('http://localhost:5000/signup', {
          firstName: this.firstName,
          lastName: this.lastName,
          email: this.email,
          password: this.password,
          confirmPassword: this.confirmPassword
        });

        alert("Sign up successful");

        this.$router.push('/login');
      } catch (e) {
        // Handle sign-up error
        this.error = 'Error occured!'
      }
    }
  }
}
</script>
