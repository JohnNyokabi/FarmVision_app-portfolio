<template>
  <div class="auth-wrapper">
    <div class="auth-inner">
      <div class="farmer-registration">
        <h2>Farmer Registration</h2>
        <form @submit.prevent="submitForm">
          <error v-if="error" :error="error"/>
          <div class="form-group">
            <label for="firstName">First Name</label>
            <input type="text" id="firstName" v-model="formData.firstName" required>
          </div>
          <div class="form-group">
            <label for="lastName">Last Name</label>
            <input type="text" id="lastName" v-model="formData.lastName" required>
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
            <!--<div>
              <label>
                <input type="checkbox" v-model="formData.farmingType.livestock" value="Livestock">
                Livestock
              </label>
              <div v-if="formData.farmingType.livestock">
                <label>
                  <input type="checkbox" v-model="formData.livestockOptions.dairy" value="Dairy">
                  Dairy
                </label>
                <label>
                  <input type="checkbox" v-model="formData.livestockOptions.beef" value="Beef">
                  Beef
                </label>
                <label>
                  <input type="checkbox" v-model="formData.livestockOptions.shoat" value="Shoat">
                  Shoat
                </label>
                <label>
                  <input type="checkbox" v-model="formData.livestockOptions.broilers" value="Broilers">
                  Broilers
                </label>
                <label>
                  <input type="checkbox" v-model="formData.livestockOptions.layers" value="Layers">
                  Layers
                </label>
                <label>
                  <input type="checkbox" v-model="formData.livestockOptions.pig" value="Pig">
                  Pig
                </label>
                <label>
                  <input type="checkbox" v-model="formData.livestockOptions.rabbit" value="Rabbit">
                  Rabbit
                </label>
                <input type="text" v-model="formData.livestockOptions.otherLivestock" placeholder="Other">
              </div>
              <label>
                <input type="checkbox" v-model="formData.farmingType.crops" value="Crops">
                Crops
              </label>
              <div v-if="formData.farmingType.crops">
                <label>
                  <input type="checkbox" v-model="formData.cropOptions.corn" value="Corn">
                  Corn
                </label>
                <label>
                  <input type="checkbox" v-model="formData.cropOptions.wheat" value="Wheat">
                  Wheat
                </label>
                <label>
                  <input type="checkbox" v-model="formData.cropOptions.barley" value="Barley">
                  Barley
                </label>
                <label>
                  <input type="checkbox" v-model="formData.cropOptions.potatoes" value="Potatoes">
                  Potatoes
                </label>
                <label>
                  <input type="checkbox" v-model="formData.cropOptions.tomatoes" value="Tomatoes">
                  Tomatoes
                </label>
                <label>
                  <input type="checkbox" v-model="formData.cropOptions.sorghum" value="Sorghum">
                  Sorghum
                </label>
                <label>
                  <input type="checkbox" v-model="formData.cropOptions.sweetPotatoes" value="Sweet Potatoes">
                  Sweet Potatoes
                </label>
                <input type="text" v-model="formData.cropOptions.otherCrops" placeholder="Other">
              </div>
            </div>-->
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
import FarmerDetails from '../components/FarmerDetails.vue';

export default {
  name: 'Registration',
  components: {
    Error,
    FarmerDetails
  },
  data() {
    return {
      formData: {
        firstName: '',
        lastName: '',
        email: '',
        country: '',
        identification: '',
        farmName: '',
        farmAddress: '',
        farmingType: '',
        /*{
          livestock: false,
          crops: false
        },
        livestockOptions: {
          dairy: false,
          beef: false,
          shoat: false,
          broilers: false,
          layers: false,
          pig: false,
          rabbit: false,
          otherLivestock: ''
        },
        cropOptions: {
          corn: false,
          wheat: false,
          barley: false,
          potatoes: false,
          tomatoes: false,
          sorghum: false,
          sweetPotatoes: false,
          otherCrops: ''
        },*/
        error: ''
      },
      farmers: []
    };
  },
  methods: {
    async submitForm() {
      /*const selectedLivestock = {};
      Object.entries(this.formData.livestockOptions).forEach(([key, value]) => {
        if (value) {
          selectedLivestock[key] = value;
        }
      });

      const selectedCrops = {};
      Object.entries(this.formData.cropOptions).forEach(([key, value]) => {
        if (value) {
          selectedCrops[key] = value;
        }
      });*/

      const payload = {
        first_name: this.formData.firstName,
        last_name: this.formData.lastName,
        email: this.formData.email,
        country: this.formData.country,
        identification: this.formData.identification,
        farm_name: this.formData.farmName,
        farm_address: this.formData.farmAddress,
        farming_type: this.formData.farmingType,
        //livestock_options: this.formData.livestockOptions,
        //crop_options: this.formData.cropOptions,
        //livestock_options: selectedLivestock,
        //crop_options: selectedCrops,
      };

      try {
        const response = await axios.post('http://localhost:5001/farmers', payload);
        console.log('Response from backend:', response.data);

        // Add the captured form data to the farmers array
        this.farmers.push(response.data);

        console.log('Form data from registrationVue:', response.data);

        this.$router.push({
          name: 'FarmManagement',
          params: { farmers: JSON.stringify([response.data]) },
        });
      } catch (error) {
        this.error = 'An error occurred!';
      }

      /*try {
        const response = await axios.post('http://localhost:5001/farmers', payload);
        console.log('Response from backend:', response.data);
        
        this.$router.push('/FarmManagement')
      } catch (error) {
        this.error = 'An error occurred!';
      }*/
    }
  }
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
