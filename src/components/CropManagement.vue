<template>
  <div>
    <h2>Crop Management</h2>
    <div class="search-bar">
      <input type="text" id="searchInput" v-model="searchTerm" placeholder="Search crops..." />
      <span class="search-icon" @click="searchCrops">
        <font-awesome-icon icon="search" />
      </span>
    </div>
    <div class="form-section">
      <h3>New Crop</h3>
      <div class="form-group">
        <label for="crop-type">Crop Type:</label>
        <input type="text" id="crop-type" v-model="newCrop.type" />
      </div>
      <div class="form-group">
        <label for="crop-variety">Variety:</label>
        <input type="text" id="crop-variety" v-model="newCrop.variety" />
      </div>
      <div class="form-group">
        <label for="date-planted">Date Planted:</label>
        <input type="date" id="date-planted" v-model="newCrop.datePlanted" />
      </div>
      <div class="form-group">
        <label for="area-planted">Area Planted (in acres):</label>
        <input type="number" id="area-planted" v-model="newCrop.areaPlanted" />
      </div>
      <div class="form-group">
        <label for="plant-spacing">Plant Spacing (in inches):</label>
        <input type="number" id="plant-spacing" v-model="newCrop.plantSpacing" />
      </div>
      <div class="form-group">
        <label for="row-spacing">Row Spacing (in inches):</label>
        <input type="number" id="row-spacing" v-model="newCrop.rowSpacing" />
      </div>
      <div class="form-group">
        <label for="depth-planted">Depth Planted (in inches):</label>
        <input type="number" id="depth-planted" v-model="newCrop.depthPlanted" />
      </div>
      <div class="form-group">
        <label for="planting-method">Planting Method:</label>
        <select id="planting-method" v-model="newCrop.plantingMethod">
          <option value="direct-sow">Direct Sow</option>
          <option value="broadcasting">Broadcasting</option>
          <option value="transplanting">Transplanting</option>
        </select>
      </div>
      <div class="form-group">
        <label for="days-to-germinate">Days to Germinate:</label>
        <input type="number" id="days-to-germinate" v-model="newCrop.daysToGerminate" />
      </div>
      <div class="form-group">
        <label for="germination-rate">Estimated Germination Rate (%):</label>
        <input type="number" id="germination-rate" v-model="newCrop.germinationRate" />
      </div>
      <div class="form-group">
        <label for="seeds-per-hole">Seeds per Hole:</label>
        <input type="number" id="seeds-per-hole" v-model="newCrop.seedsPerHole" />
      </div>
      <div class="form-group">
        <label for="planting-details">Planting Details:</label>
        <textarea id="planting-details" v-model="newCrop.plantingDetails"></textarea>
      </div>
      <div class="form-group">
        <label for="harvesting-date">Harvesting Date:</label>
        <input type="date" id="harvesting-date" v-model="newCrop.harvestingDate" />
      </div>
      <div class="form-group">
        <label for="amount-harvested">Amount Harvested:</label>
        <input type="number" id="amount-harvested" v-model="newCrop.amountHarvested" />
      </div>
      <div class="form-group">
        <label for="weight-unit">Weight Unit:</label>
        <select id="weight-unit" v-model="newCrop.weightUnit">
          <option value="kg">Kilograms (kg)</option>
          <option value="lb">Pounds (lb)</option>
          <option value="t">Tonnes (t)</option>
        </select>
      </div>
      <div class="button-container">
        <button @click="handleAddNewCrop">Add New Crop</button>
      </div>
    </div>

    <div v-if="isTableDialogOpen" class="dialog-overlay">
      <div class="dialog">
        <span class="close-icon" @click="closeTableDialog">
          <font-awesome-icon icon="times" />
        </span>
        <div class="table-section">
          <h3>Crop List</h3>
          <table>
            <thead>
              <tr>
                <th>Crop Type</th>
                <th>Variety</th>
                <th>Date Planted</th>
                <th>Area Planted (acres)</th>
                <th>Plant Spacing (inches)</th>
                <th>Row Spacing (inches)</th>
                <th>Depth Planted (inches)</th>
                <th>Planting Method</th>
                <th>Days to Germinate</th>
                <th>Estimated Germination Rate (%)</th>
                <th>Seeds per Hole</th>
                <th>Planting Details</th>
                <th>Harvesting Date</th>
                <th>Amount Harvested</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(crop, index) in filteredCrops" :key="crop.id">
                <td>{{ crop.type }}</td>
                <td>{{ crop.variety }}</td>
                <td>{{ crop.datePlanted }}</td>
                <td>{{ crop.areaPlanted }}</td>
                <td>{{ crop.plantSpacing }}</td>
                <td>{{ crop.rowSpacing }}</td>
                <td>{{ crop.depthPlanted }}</td>
                <td>{{ crop.plantingMethod }}</td>
                <td>{{ crop.daysToGerminate }}</td>
                <td>{{ crop.germinationRate }}</td>
                <td>{{ crop.seedsPerHole }}</td>
                <td>{{ crop.plantingDetails }}</td>
                <td>{{ crop.harvestingDate }}</td>
                <td>{{ crop.amountHarvested }} {{ crop.weightUnit }}</td>
                <td>
                  <div class="button-container">
                    <template v-if="editedCropIndex === index">
                      <button @click="saveCrop(index)">Save</button>
                    </template>
                    <template v-else>
                     <button @click="editCrop(index)">Edit</button>
                    </template>
                    <button @click="deleteCrop(index)">Delete</button>
                  </div>
                  
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { library } from '@fortawesome/fontawesome-svg-core';
import { faSearch, faTimes } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

library.add(faSearch, faTimes);

export default {
  name: 'CropManagement',
  components: {
    FontAwesomeIcon,   
  },
  data() {
    return {
      newCrop: {
        id: null,
        type: '',
        variety: '',
        datePlanted: '',
        areaPlanted: null,
        plantSpacing: null,
        rowSpacing: null,
        depthPlanted: null,
        plantingMethod: 'direct-sow',
        daysToGerminate: null,
        germinationRate: null,
        seedsPerHole: null,
        plantingDetails: '',
        harvestingDate: '',
        amountHarvested: null,
        weightUnit: 'kg',
      },
      crops: [],
      editedCropIndex: null,
      searchTerm: '',
      isTableDialogOpen: false,
    };
  },
  computed: {
    filteredCrops() {
      const term = this.searchTerm.toLowerCase();
      return this.crops.filter(
        (crop) =>
          crop.type.toLowerCase().includes(term) ||
          crop.variety.toLowerCase().includes(term)
      );
    },
  },
  methods: {
    handleAddNewCrop() {
      this.addNewCrop();
      this.openTableDialog();
    },

    generateUniqueId() {
      return Math.random().toString(36).substr(2, 9);
    },

    addNewCrop() {
      const editedCrop = { ...this.newCrop }; // Create a copy of the new crop object

      if (
        editedCrop.type &&
        editedCrop.variety &&
        editedCrop.datePlanted &&
        editedCrop.areaPlanted &&
        editedCrop.plantSpacing &&
        editedCrop.rowSpacing &&
        editedCrop.depthPlanted &&
        editedCrop.plantingMethod &&
        editedCrop.daysToGerminate &&
        editedCrop.germinationRate &&
        editedCrop.seedsPerHole &&
        editedCrop.plantingDetails &&
        editedCrop.harvestingDate &&
        editedCrop.amountHarvested &&
        editedCrop.weightUnit
      ) {
        if (this.editedCropIndex !== null) {
          // Update existing crop
          this.crops.splice(this.editedCropIndex, 1, editedCrop);
        } else {
          editedCrop.id = this.generateUniqueId(); // Generate a unique ID for the new crop
          this.crops.push(editedCrop);
        }
        this.resetForm();
      }
    },

    openTableDialog() {
      this.isTableDialogOpen = true;
    },

    editCrop(index) {
      const crop = this.crops[index];

      // Set the form fields with the values of the selected crop
      this.newCrop.id = crop.id;
      this.newCrop.type = crop.type;
      this.newCrop.variety = crop.variety;
      this.newCrop.datePlanted = crop.datePlanted;
      this.newCrop.areaPlanted = crop.areaPlanted;
      this.newCrop.plantSpacing = crop.plantSpacing;
      this.newCrop.rowSpacing = crop.rowSpacing;
      this.newCrop.depthPlanted = crop.depthPlanted;
      this.newCrop.plantingMethod = crop.plantingMethod;
      this.newCrop.daysToGerminate = crop.daysToGerminate;
      this.newCrop.germinationRate = crop.germinationRate;
      this.newCrop.seedsPerHole = crop.seedsPerHole;
      this.newCrop.plantingDetails = crop.plantingDetails;
      this.newCrop.harvestingDate = crop.harvestingDate;
      this.newCrop.amountHarvested = crop.amountHarvested;
      this.newCrop.weightUnit = crop.weightUnit;

      this.editedCropIndex = index;
    },
    saveCrop(index) {
      const editedCrop = { ...this.newCrop };
      this.crops.splice(index, 1, editedCrop);
      this.resetForm();
    },

    deleteCrop(index) {
      this.crops.splice(index, 1);
    },

    resetForm() {
      this.newCrop = {
        id: null,
        type: '',
        variety: '',
        datePlanted: '',
        areaPlanted: null,
        plantSpacing: null,
        rowSpacing: null,
        depthPlanted: null,
        plantingMethod: 'direct-sow',
        daysToGerminate: null,
        germinationRate: null,
        seedsPerHole: null,
        plantingDetails: '',
        harvestingDate: '',
        amountHarvested: null,
        weightUnit: 'kg',
      };
      this.editedCropIndex = null;
    },

    closeTableDialog() {
      this.isTableDialogOpen = false;
    },
  },
};
</script>

<style scoped>
.search-bar {
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 30px;
  margin-top: 5px;
  background-color: #f0f0f0;
  padding: 5px;
  max-width: 300px;
  margin: 0 auto;
  height: 7vh;
}

.search-bar input {
  flex: 1;
  padding: 10px;
  font-size: 16px;
  border: none;
  outline: none;
  background: transparent;
  width: 300px;
}

.search-icon {
  cursor: pointer;
  padding: 5px;
  margin-left: 5px;
  background-color: #ccc;
  border-radius: 50%;
  height: 5vh;
}

.search-icon:hover {
  background-color: #999;
}

.form-section {
  margin-bottom: 20px;
  margin-top: 10px;
  background-color: white;
  border-radius: 10px;
  padding: 10px;
  width: 70%;
  margin-left: 15%;
  justify-content: center;
}

.form-group {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.form-group label {
  width: 30%;
  margin-right: 5px;
  font-weight: bold;
}

.form-group input[type="text"],
.form-group input[type="number"],
.form-group select,
.form-group textarea {
  flex: 1;
  width: 70%;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
  height: 5vh;
}

#planting-details {
  resize: vertical;
  height: 100px;
}
.form-group textarea {
  resize: vertical;
}

.button-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.button-container button {
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  background-color: #4caf50;
  color: white;
  cursor: pointer;
}

.button-container button:hover {
  background-color: #45a049;
}

.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.dialog {
  background-color: #ffffff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  max-width: 100%;
  width: 90%;
  position: relative;
}

.close-icon {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
  background-color: #ccc;
  border-radius: 50%;
  padding: 5px;
}

.close-icon:hover {
  background-color: #999;
}

.table-section table {
  width: 100%;
  border-collapse: collapse;
}

.table-section th,
.table-section td {
  padding: 5px 10px;
  border: 1px solid #ccc;
}

.table-section th {
  background-color: #f0f0f0;
}

.table-section td:last-child {
  white-space: nowrap;
}
</style>
