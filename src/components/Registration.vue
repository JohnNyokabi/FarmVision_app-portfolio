<template>
  <div class="auth-wrapper">
    <div class="auth-inner">
      <div class="farmer-registration">
        <h2>Farmer Registration</h2>
        <form @submit.prevent="submitForm">
          <error v-if="error" :error="error"/>
          <div class="form-group">
            <label for="firstName">Full Name</label>
            <input type="text" id="fullName" v-model="formData.fullName" required>
          </div>
          <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" v-model="formData.email" required>
          </div>
          <div class="form-group">
            <label for="country">Country</label>
            <input type="text" id="country" v-model="formData.country" placeholder="Please Enter your Country" required>
          </div>
          <div class="form-group">
            <label for="identification">Identification</label>
            <input type="text" id="identification" v-model="formData.identification" required>
          </div>
          <div class="form-group">
            <label for="farmName">Farm Name</label>
            <input type="text" id="farmName" v-model="formData.farmName" required>
          </div>
          <div class="form-group">
            <label for="farmLocation">Farm Location</label>
            <input type="text" id="farmLocation" v-model="formData.farmLocation" placeholder="e.g. Bahati" required>
          </div>
          <div class="form-group">
            <label for="farmAddress">Farm Address</label>
            <textarea id="farmAddress" v-model="formData.farmAddress" name="farm_address" required></textarea>
          </div>
          <div class="form-group">
            <label for="farmingType">Farming Type</label>
            <textarea id="farmingType" v-model="formData.farmingType" name="farming_type" required></textarea>
          </div>
          <button type="submit">Register</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Error from './Error.vue';

export default {
  name: 'Registration',
  components: {
    Error
  },
  data() {
    return {
      formData: {
        fullName: '',
        email: '',
        country: '',
        identification: '',
        farmName: '',
        farmLocation: '',
        farmAddress: '',
        farmingType: ''
      },
      error: ''
    };
  },
  methods: {
    async submitForm() {
      const payload = {
        full_name: this.formData.fullName,
        email: this.formData.email,
        country: this.formData.country,
        identification: this.formData.identification,
        farm_name: this.formData.farmName,
        farm_location: this.formData.farmLocation,
        farm_address: this.formData.farmAddress,
        farming_type: this.formData.farmingType,
      };

      try {
        const response = await axios.post('http://localhost:5001/farmers', payload);
        console.log('Response from backend:', response.data);

        this.$router.push({
          name: 'farmerDetails',
          props: { farmer: response.data },
        });
      } catch (error) {
        this.error = 'An error occurred!';
      }
    }
  },
};
</script>

<style scoped>
.farmer-registration {
  max-width: 600px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: center;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

input[type="text"],
input[type="email"],
textarea,
select {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button[type="submit"] {
  padding: 0.5rem 1rem;
  margin-top: 0.5rem;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f2f2f2;
}

input[type="date"] {
  width: 150px;
}
</style>
