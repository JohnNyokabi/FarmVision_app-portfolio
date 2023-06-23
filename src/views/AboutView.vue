<template>
  <div class="about">
    <h1><b>About FarmVision</b></h1>
    <p>Welcome to FarmVision, a platform dedicated to revolutionizing the farming industry.</p>
    <p>Our mission is to provide farmers with advanced technologies and data-driven insights to optimize their operations, increase productivity, and maximize yields.</p>
    <p><b>With FarmVision, you can:</b></p>
    <ul>
      <li>Monitor real-time weather conditions and receive personalized weather forecasts for your farm.</li>
      <li>Access a comprehensive database of agricultural information and best practices.</li>
    </ul>
    <p>We are committed to empowering farmers and driving sustainable farming practices through innovation and technology.</p>
    <p>Join FarmVision today and take your farming operations to the next level!</p>
  </div>
</template>

<script>
export default {
  name: 'AboutView'
}
</script>

<style scoped>
.about {
  max-width: 800px;
  min-height: 80vh;
  margin: 0 auto;
  padding: 20px;
  background-color: rgb(219, 219, 219);
  color: blue;
}

h1, p {
  color: black;
}

p {
  font-weight: 600;
}
</style>
