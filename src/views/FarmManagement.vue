<template>
  <div>
    <h2>Farmer Management</h2>
    <FarmDetails :farmers="farmers" />
  </div>
</template>

<script>
import FarmDetails from '../components/FarmerDetails.vue';

export default {
  name: 'FarmManagement',
  components: {
    FarmDetails,
  },
  props: ['farmers'],
  created() {
    console.log('Farmers data from farm management:', this.farmers);
  },
};
</script>

<!--<template>
  <div>
    <h1>Farm Management</h1>
    <FarmerDetails :farmers="farmers" />
  </div>
</template>

<script>
import FarmerDetails from '../components/FarmerDetails.vue';
import axios from 'axios';

export default {
  name: 'FarmManagement',
  components: {
    FarmerDetails
  },
  data() {
    return {
      farmers: []
    };
  },
  // Fetch the farmer data from an API or other source if needed
  // You can populate the farmers array here or in the mounted hook
  mounted() {
    axios.get('http://localhost:5001/farmers')
    .then(response => {
      this.farmers = response.data;
    }).catch(error => {
      console.error('Error fetching farmer data:', error);
    });

    // Example: Populating the array manually (replace with your data)
    this.farmers = [];
  }
};
</script>-->

<style scoped>
/* Styles... */
</style>
