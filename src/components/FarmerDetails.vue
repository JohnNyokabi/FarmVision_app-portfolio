<template>
  <div class="table">
    <table>
      <thead>
        <tr>
          <th>firstName</th>
          <th>lastName</th>
          <th>Email</th>
          <th>Country</th>
          <th>Identification</th>
          <th>Farm Name</th>
          <th>Farm Location</th>
          <th>Farm Address</th>
          <th>Farming Type</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="farmer in farmers" :key="farmer.id">
          <td>{{ farmer.firstName }} {{ farmer.lastName }}</td>
          <td>{{ farmer.email }}</td>
          <td>{{ farmer.country }}</td>
          <td>{{ farmer.identification }}</td>
          <td>{{ farmer.farmName }}</td>
          <td>{{ farmer.farmLocation }}</td>
          <td>{{ farmer.farmAddress }}</td>
          <td>{{ farmer.farmingType }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'FarmDetails',
  props: ['farmers'],
  created() {
    console.log('Farmers prop from farmerdetails:', this.farmers);
  },
};
</script>

<style scoped>
.table {
  margin-top: 1rem;
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
</style>
