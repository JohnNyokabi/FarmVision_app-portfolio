<template>
  <div>
    <h2>Weather</h2>
    <div v-if="loading">Loading weather data...</div>
    <div v-else-if="error">Error fetching weather data</div>
    <div v-else>
      <h3>Current Weather in {{ location }}</h3>
      <p>{{ weather.description }}</p>
      <p>Temperature: {{ weather.temperature }}°C</p>
      <p>Humidity: {{ weather.humidity }}%</p>
      <p>Wind Speed: {{ weather.windSpeed }} km/h</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Weather',
  data() {
    return {
      loading: true,
      error: false,
      location: '',
      weather: {},
    };
  },
  mounted() {
    // Assuming you have access to the farmer's registered location in Vuex or component props
    // Replace 'this.farmerLocation' with the actual location data
    this.location = this.farmerLocation;
    this.fetchWeatherData();
  },
  methods: {
    async fetchWeatherData() {
      const options = {
        method: 'GET',
        url: 'https://weatherapi-com.p.rapidapi.com/current.json',
        params: { q: this.location },
        headers: {
          'X-RapidAPI-Key': '652e2d3cdcmsh8531a16f7c8cb55p1ce86cjsn18637c9d0b32',
          'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com',
        },
      };

      try {
        const response = await axios.request(options);
        this.loading = false;
        this.weather = {
          description: response.data.current.condition.text,
          temperature: response.data.current.temp_c,
          humidity: response.data.current.humidity,
          windSpeed: response.data.current.wind_kph,
        };
      } catch (error) {
        this.loading = false;
        this.error = true;
        console.error(error);
      }
    },
  },
};
</script>
