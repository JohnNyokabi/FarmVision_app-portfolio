import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Forgot from '../components/Forgot.vue'
import Reset from '../components/Reset.vue'
import Login from '../components/Login.vue'
import Weather from '../views/Weather.vue'
import MarketTrends from '../views/MarketTrends.vue'
import FarmManagement from '../views/FarmManagement'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/FarmManagement/:farmers',
    name: 'FarmManagement',
    component: FarmManagement,
    props: true,
  },    
  /*{
    path: '/FarmManagement',
    name: 'farmManagement',
    component: () => import('../views/FarmManagement.vue')
  },*/
  {
    path: '/Registration',
    name: 'registration',
    component: () => import('../components/Registration.vue')
  },
  {
    path: '/CropManagement',
    name: 'crops',
    component: () => import('../components/CropManagement.vue')
  },
  {
    path: '/LivestockManagement',
    name: 'livestock',
    component: () => import('../components/LivestockManagement.vue')
  },
  {
    path: '/InventoryManagement',
    name: 'Inventory',
    component: () => import('../components/InventoryManagement.vue')
  },
  {
    path: '/MarketTrends',
    name: 'MarketTrends',
    component: MarketTrends
  },
  {
    path: '/weather',
    name: 'Weather',
    component: Weather
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/AboutView.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: () => import('../components/SignUp.vue')
  },
  {
    path: '/forgot',
    name: 'Forgot',
    component: Forgot
  },
  {
    path: '/reset/:token',
    name: 'Reset',
    component: Reset
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
