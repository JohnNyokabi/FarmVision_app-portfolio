<template>
  <nav>
    <div class="container">
      <router-link to="/" class="logo">FarmVision</router-link>
      <div class="menu">
        <div class="menu-item" @mouseover="showFarmManagementLinks = true" @mouseleave="showFarmManagementLinks = false">
          <div>Farm Management</div>
          <ul aria-hidden="true" v-show="showFarmManagementLinks">
            <div>
              <router-link v-if="!farmer" to="/Registration">Farmer Registration</router-link>
            </div>
            <div>
              <router-link to="/LivestockManagement">Livestock Management</router-link>
            </div>
            <div>
              <router-link to="/CropManagement">Crops Management</router-link>
            </div>
            <div>
              <router-link to="/InventoryManagement">Inventory Management</router-link>
            </div>
          </ul>
        </div>

        <router-link to="/MarketTrends" class="menu-item">Market Trends</router-link>
        <router-link to="/Financial_analysis" class="menu-item">Financial Analysis</router-link>
        <router-link to="/Weather" class="menu-item">Weather</router-link>
        <router-link to="/About" class="menu-item">About</router-link>
      </div>
      <div class="user">
        <router-link v-if="!user" to="/Login">Login</router-link>
        <router-link v-if="!user" to="/SignUp">Sign Up</router-link>
        <a v-if="user" href="javascript:void(0)" @click="handleClick">Logout</a>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Nav',
  data() {
    return {
      showFarmManagementLinks: false
    }
  },
  methods: {
    handleClick() {
      localStorage.removeItem('token');
      this.$store.dispatch('user', null);
      this.$router.push('/')
    }
  },
  computed: {
    ...mapGetters(['user'])
  }
}
</script>

<style scoped>
nav {
  background-color: #fff;
  padding: 10px 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}
.logo {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  text-decoration: none;
}

.menu {
  display: flex;
  gap: 20px;
}

.menu-item {
  color: #555;
  text-decoration: none;
  transition: color 0.3s;
}

.menu-item:hover {
  color: #888;
}
.user {
  display: flex;
  gap: 10px;
}

.menu-item ul {
  display: none;
}

.menu-item:hover ul {
  display: block;
}
</style>
