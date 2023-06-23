<template>
  <div class="home">
    <h1 v-if="user">Welcome to FarmVision, {{ user.firstName }} {{ user.lastName }}</h1>
    <h1 v-else>Welcome to FarmVision, Guest</h1>
    <p class="tagline">Your All-in-One Farm Management Solution</p>
    <div class="features">
      <div class="feature">
        <h2>Crop and Livestock Management</h2>
        <img src="../assets/images/farm-management.jpg" alt="Farm Management">
        <p>Efficiently manage your crops and livestock with our intuitive tools.</p>
      </div>
      <div class="feature">
        <h2>Inventory Management</h2>
        <img src="../assets/images/Inventory_management.gif" alt="Inventory Management">
        <p>Keep track of your inventory, including seeds, fertilizers, equipment, and more.</p>
      </div>
      <div class="feature">
        <h2>Market Analysis</h2>
        <img src="../assets/images/market_analysis.jpg" alt="Market Analysis">
        <p>Stay informed about the latest market trends and make informed decisions for your farm.</p>
      </div>
      <div class="feature">
        <h2>Financial Analysis</h2>
        <img src="../assets/images/financial_management.jpg" alt="Financial Analysis">
        <p>Analyze the financial aspects of your farm, including revenue, expenses, and profitability.</p>
      </div>
      <div class="feature">
        <h2>Weather</h2>
        <img src="../assets/images/weather.png" alt="Weather">
        <p>Get real-time weather updates and forecasts for your farm's location.</p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'HomeView',
  computed: {
    ...mapGetters(['user'])
  }
};
</script>

<style scoped>
.home {
  padding: 40px 20px;
  text-align: center;
}

h1 {
  font-size: 36px;
  margin-bottom: 10px;
  color: #333;
}

.tagline {
  font-size: 18px;
  color: #555;
  margin-bottom: 40px;
}

.features {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  grid-gap: 20px;
  justify-items: center;
}

.feature {
  background-color: #f9f9f9;
  border-radius: 5px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.feature h2 {
  font-size: 24px;
  margin-bottom: 10px;
  color: #333;
}

.feature img {
  width: 100%;
  max-width: 300px;
  height: auto;
  border-radius: 5px;
  margin-bottom: 10px;
}

.feature p {
  font-size: 16px;
  color: #555;
}
</style>
