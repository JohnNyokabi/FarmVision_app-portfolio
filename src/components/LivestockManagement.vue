<template>
  <div>
    <h2>Livestock Management</h2>
    <form @submit.prevent="submitAnimal">
      <label for="name">Name:</label>
      <input id="name" v-model="animalForm.name" required>

      <label for="type">Type:</label>
      <select id="type" v-model="animalForm.type" required>
        <option disabled value="">Please select</option>
        <option value="Dairy">Dairy</option>
        <option value="Beef">Beef</option>
        <option value="Pigs">Pigs</option>
        <option value="Sheep">Sheep</option>
        <option value="Goats">Goats</option>
        <option value="Poultry">Poultry</option>
      </select>

      <div v-if="animalForm.type">
        <label for="breed">Breed:</label>
        <select id="breed" v-model="animalForm.breed">
          <option value="">Select Breed</option>
          <option v-for="breed in getLivestockBreeds" :value="breed">{{ breed }}</option>
        </select>
      </div>

      <label v-if="animalForm.type !== 'Poultry'">Date of Birth:</label>
      <label v-else>Date Brought-In:</label>
      <input v-model="animalForm.dateOfBirth" type="date">

      <label for="gender">Gender:</label>
      <select id="gender" v-model="animalForm.gender" required>
        <option disabled value="">Please select</option>
        <option value="Male">Male</option>
        <option value="Female">Female</option>
      </select>

      <label v-if="animalForm.type === 'Poultry' && animalForm.breed === 'Broilers'" for="slaughterDate">Slaughter Date:</label>
      <input v-if="animalForm.type === 'Poultry' && animalForm.breed === 'Broilers'" type="date" id="slaughterDate" v-model="animalForm.slaughterDate" required>

      <label v-if="animalForm.type === 'Poultry' && animalForm.breed !== 'Broilers'" for="startDate">{{ getStartDateLabel() }}:</label>
      <input v-if="animalForm.type === 'Poultry' && animalForm.breed !== 'Broilers'" type="date" id="startDate" v-model="animalForm.startDate">

      <label v-if="animalForm.type !== 'Poultry' && animalForm.gender === 'Female'" required>Date Served:</label>
      <input v-if="animalForm.type !== 'Poultry' && animalForm.gender === 'Female'" v-model="animalForm.dateServed" type="date" required>

      <label for="productionSystem">Production System:</label>
      <select id="productionSystem" v-model="animalForm.productionSystem" required>
        <option disabled value="">Please select</option>
        <option value="Intensive">Intensive</option>
        <option value="Semi-Intensive">Semi-Intensive</option>
        <option value="Extensive">Extensive</option>
      </select>

      <label for="feedType">Feed Type:</label>
      <input id="feedType" v-model="animalForm.feedType">

      <label for="amountAdministered">Amount Administered:</label>
      <input id="amountAdministered" v-model="animalForm.amountAdministered" type="number" min="0">

      <button type="submit">Submit</button>
    </form>

    <div v-for="animalType in getUniqueAnimalTypes" :key="animalType">
      <h3>{{ animalType }}</h3>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Breed</th>
            <th v-if="animalForm.type !== 'Poultry'">Date of Birth</th>
            <th>Age (Months)</th>
            <th>Gender</th>
            <th>Date Served</th>
            <th v-if="isPoultryBreedSelected">Start Date</th>
            <th v-if="animalForm.type === 'Poultry' && animalForm.breed === 'Broilers'">Slaughter Date</th>
            <th>Production System</th>
            <th>Feed Type</th>
            <th>Amount Administered(kg/day)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="animal in livestockByType(animalType)" :key="animal.name">
            <td>{{ animal.name }}</td>
            <td>{{ animal.type }}</td>
            <td>{{ animal.breed }}</td>
            <td v-if="animalForm.type !== 'Poultry'">{{ animal.dateOfBirth }}</td>
            <td>{{ calculateAge(animal.dateOfBirth) }}</td>
            <td>{{ animal.gender }}</td>
            <td v-if="isPoultryBreedSelected">{{ animal.startDate }}</td>
            <td v-if="animalForm.type === 'Poultry' && animalForm.breed === 'Broilers'">{{ animal.slaughterDate }}</td>
            <td>{{ animal.dateServed }}</td>
            <td>{{ animal.productionSystem }}</td>
            <td>{{ animal.feedType }}</td>
            <td>{{ animal.amountAdministered }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "LivestockManagement",
  data() {
    return {
      livestock: [],
      animalForm: {
        name: "",
        type: "",
        breed: "",
        dateOfBirth: "",
        dateBroughtIn: "",
        age: "",
        gender: "",
        startDate: "",
        slaughterDate: "",
        dateServed: "",
        productionSystem: "",
        feedType: "",
        amountAdministered: "",
      },
    };
  },
  computed: {
    getUniqueAnimalTypes() {
      return [...new Set(this.livestock.map((animal) => animal.type))];
    },
    getLivestockBreeds() {
      if (this.animalForm.type === "Dairy") {
        return ["Holstein", "Swedish Red", "Ayrshire", "Guernsey", "Jersey", "Brown Swiss", "Sahiwal", "Cross"];
      } else if (this.animalForm.type === "Beef") {
        return ["Angus", "Hereford", "Simmental", "Boran", "Red Poll", "East African Zebu", "Cross"];
      } else if (this.animalForm.type === "Pigs") {
        return ["Duroc", "Large white", "Landrace", "Tamworth", "Chester White", "Hampshire", "Yorkshire", "Cross"];
      } else if (this.animalForm.type === "Sheep") {
        return ["Dorper", "Merino", "Suffolk", "Romney", "Hampshire Down", "Rambouillet", "Cross"];
      } else if (this.animalForm.type === "Goats") {
        return ["Boer", "Saanen", "Alpine", "Toggenberger", "Anglo-Nubian", "Galla", "Nigerian-dwarf"];
      } else if (this.animalForm.type === "Poultry") {
        return ["Layers", "Broilers"];
      }
      return [];
    },
    isPoultryBreedSelected() {
      return this.animalForm.type === "Poultry" && this.animalForm.breed;
    },
  },
  methods: {
    livestockByType(animalType) {
      return this.livestock.filter((animal) => animal.type === animalType);
    },
    submitAnimal() {
      const newAnimal = { ...this.animalForm };
      this.livestock.push(newAnimal);
      this.resetForm();
    },
    resetForm() {
      this.animalForm = {
        name: "",
        type: "",
        breed: "",
        dateOfBirth: "",
        dateBroughtIn: "",
        age: "",
        gender: "",
        startDate: "",
        slaughterDate: "",
        dateServed: "",
        productionSystem: "",
        feedType: "",
        amountAdministered: "",
      };
    },
    calculateAge(dateOfBirth) {
      const birthDate = new Date(dateOfBirth);
      const currentDate = new Date();
      const ageInMilliseconds = currentDate - birthDate;
      const ageInMonths = Math.floor(ageInMilliseconds / (1000 * 60 * 60 * 24 * 30));
      return ageInMonths;
    },
    
    getStartDateLabel() {
      if (this.animalForm.type !== 'Poultry' && this.animalForm.gender === 'Female') {
        return "Date Served";
      } else if (this.animalForm.type === "Poultry" && this.animalForm.breed !== "Broilers") {
        return "Start Date";
      } else {
        return "Date Brought-In";
      }  
    },
    getExpectedDate(animal) {
      const gestationPeriod = this.getGestationPeriod(animal.type);
      if (gestationPeriod && animal.dateServed) {
        const dateServed = new Date(animal.dateServed);
        const expectedDate = new Date(dateServed.getTime() + gestationPeriod * 24 * 60 * 60 * 1000);
        return expectedDate.toISOString().split("T")[0];
      }
      return "";
    },
    getGestationPeriod(animalType) {
      if (animalType === "Dairy" || animalType === "Beef") {
        return 280;
      } else if (animalType === "Pigs") {
        return 115;
      } else if (animalType === "Sheep") {
        return 152;
      } else if (animalType === "Goats") {
        return 150;
      }
      return null;
    },
  },
};
</script>

<!--<template>
  <div>
    <h2>Livestock Management</h2>
    <form @submit.prevent="submitAnimal">
      <label for="name">Name:</label>
      <input id="name" v-model="animalForm.name" required>

      <label for="type">Type:</label>
      <select id="type" v-model="animalForm.type" required>
        <option disabled value="">Please select</option>
        <option value="Dairy">Dairy</option>
        <option value="Beef">Beef</option>
        <option value="Pigs">Pigs</option>
        <option value="Sheep">Sheep</option>
        <option value="Goats">Goats</option>
        <option value="Poultry">Poultry</option>
      </select>

      <div v-if="animalForm.type">
        <label for="breed">Breed:</label>
        <select id="breed" v-model="animalForm.breed">
          <option value="">Select Breed</option>
          <option v-for="breed in getLivestockBreeds" :value="breed">{{ breed }}</option>
        </select>
      </div>

      <label v-if="animalForm.type !== 'Poultry'">Date of Birth:</label>
      <label v-else>Date Brought-In:</label>
      <input v-model="animalForm.dateOfBirth" type="date" required>

      <label for="gender">Gender:</label>
      <select id="gender" v-model="animalForm.gender" required>
        <option disabled value="">Please select</option>
        <option value="Male">Male</option>
        <option value="Female">Female</option>
      </select>

      <label v-if="animalForm.type === 'Poultry' && animalForm.breed === 'Broilers'" for="slaughterDate">Slaughter Date:</label>
      <input v-if="animalForm.type === 'Poultry' && animalForm.breed === 'Broilers'" type="date" id="slaughterDate" v-model="animalForm.slaughterDate" required>

      <label v-if="animalForm.type === 'Poultry' && animalForm.breed !== 'Broilers'" for="startDate">{{ getStartDateLabel() }}:</label>
      <input v-if="animalForm.type === 'Poultry' && animalForm.breed !== 'Broilers'" type="date" id="startDate" v-model="animalForm.startDate">

      <label v-if="animalForm.type !== 'Poultry' && animalForm.gender === 'Female'">Date Served:</label>
      <input v-if="animalForm.type !== 'Poultry' && animalForm.gender === 'Female'" v-model="animalForm.dateServed" type="date" required>

      <label for="productionSystem">Production System:</label>
      <select id="productionSystem" v-model="animalForm.productionSystem" required>
        <option disabled value="">Please select</option>
        <option value="Intensive">Intensive</option>
        <option value="Semi-Intensive">Semi-Intensive</option>
        <option value="Extensive">Extensive</option>
      </select>

      <label for="feedType">Feed Type:</label>
      <input id="feedType" v-model="animalForm.feedType">

      <label for="amountAdministered">Amount Administered:</label>
      <input id="amountAdministered" v-model="animalForm.amountAdministered">

      <button type="submit">Submit</button>
    </form>

    <div v-for="animalType in getUniqueAnimalTypes" :key="animalType">
      <h3>{{ animalType }}</h3>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Breed</th>
            <th v-if="animalForm.type !== 'Poultry'">Date of Birth</th>
            <th>Gender</th>
            <th v-if="isPoultryBreedSelected">Start Date</th>
            <th v-if="animalForm.type === 'Poultry' && animalForm.breed === 'Broilers'">Slaughter Date</th>
            <th>Date Served</th>
            <th>Production System</th>
            <th>Feed Type</th>
            <th>Amount Administered</th>
            <th v-show="animalForm.type !== 'Poultry'">Expected Date</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="animal in livestockByType(animalType)" :key="animal.name">
            <td>{{ animal.name }}</td>
            <td>{{ animal.type }}</td>
            <td>{{ animal.breed }}</td>
            <td v-if="animalForm.type !== 'Poultry'">{{ animal.dateOfBirth }}</td>
            <td>{{ animal.gender }}</td>
            <td v-if="isPoultryBreedSelected">{{ animal.startDate }}</td>
            <td v-if="animalForm.type === 'Poultry' && animalForm.breed === 'Broilers'">{{ animal.slaughterDate }}</td>
            <td>{{ animal.dateServed }}</td>
            <td>{{ animal.productionSystem }}</td>
            <td>{{ animal.feedType }}</td>
            <td>{{ animal.amountAdministered }}</td>
            <td>{{ getExpectedDate(animal) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { placeholder } from '@babel/types';

export default {
  name: "LivestockManagement",
  data() {
    return {
      livestock: [],
      animalForm: {
        name: "",
        type: "",
        breed: "",
        dateOfBirth: "",
        gender: "",
        startDate: "",
        slaughterDate: "",
        dateServed: "",
        productionSystem: "",
        feedType: "",
        amountAdministered: "",
      },
    };
  },
  computed: {
    getUniqueAnimalTypes() {
      return [...new Set(this.livestock.map((animal) => animal.type))];
    },
    getLivestockBreeds() {
      if (this.animalForm.type === "Dairy") {
        return ["Holstein", "Swedish Red", "Ayrshire", "Guernsey", "Jersey", "Brown Swiss", "Sahiwal", "Cross"];
      } else if (this.animalForm.type === "Beef") {
        return ["Angus", "Hereford", "Simmental", "Boran", "Red Poll", "East African Zebu", "Cross"];
      } else if (this.animalForm.type === "Pigs") {
        return ["Duroc", "Large white", "Landrace", "Tamworth", "Chester White", "Hampshire", "Yorkshire", "Cross"];
      } else if (this.animalForm.type === "Sheep") {
        return ["Dorper", "Merino", "Suffolk", "Romney", "Hampshire Down", "Rambouillet", "Cross"];
      } else if (this.animalForm.type === "Goats") {
        return ["Boer", "Saanen", "Alpine", "Toggenberger", "Anglo-Nubian", "Galla", "Nigerian-dwarf"];
      } else if (this.animalForm.type === "Poultry") {
        return ["Layers", "Broilers"];
      }
      return [];
    },
    isPoultryBreedSelected() {
      return this.animalForm.type === "Poultry" && this.animalForm.breed;
    },
  },
  methods: {
    livestockByType(animalType) {
      return this.livestock.filter((animal) => animal.type === animalType);
    },
    submitAnimal() {
      const newAnimal = { ...this.animalForm };
      this.livestock.push(newAnimal);
      this.resetForm();
    },
    resetForm() {
      this.animalForm = {
        name: "",
        type: "",
        breed: "",
        dateOfBirth: "",
        gender: "",
        startDate: "",
        slaughterDate: "",
        dateServed: "",
        productionSystem: "",
        feedType: "",
        amountAdministered: "",
      };
    },
    getStartDateLabel() {
      if (this.animalForm.type !== 'Poultry' && this.animalForm.gender === 'Female') {
        return "Date Served";
      } else {
        return "Start Date"
      }
    },
    getExpectedDate(animal) {
      const gestationPeriod = this.getGestationPeriod(animal.type);
      if (gestationPeriod && animal.dateServed) {
        const dateServed = new Date(animal.dateServed);
        const expectedDate = new Date(dateServed.getTime() + gestationPeriod * 24 * 60 * 60 * 1000);
        return expectedDate.toISOString().split("T")[0];
      }
      return "";
    },
    getGestationPeriod(animalType) {
      if (animalType === "Dairy" || animalType === "Beef") {
        return 280; // 280 days gestation period for cows
      } else if (animalType === "Pigs") {
        return 115; // 115 days gestation period for pigs
      } else if (animalType === "Sheep") {
        return 152; // 152 days gestation period for sheep
      } else if (animalType === "Goats") {
        return 150; // 150 days gestation period for goats
      }
      return null;
    },
  },
};
</script>-->

<style scoped>
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
