<template>
  <div class="table" v-if="farmer">
    <h2>Farmer Details</h2>
    <table>
      <thead>
        <tr>
          <th>Full Name</th>
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
        <tr>
          <td>{{ farmer.fullName }}</td>
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
  name: 'FarmerDetails',
  props: {
    farmer: {
      type: Object,
      required: true,
      default: () => ({}),
    },
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
