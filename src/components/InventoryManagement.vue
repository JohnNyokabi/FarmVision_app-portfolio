<template>
  <div class="farm-inventory">
    <div class="left-nav">
      <ul>
        <li>
          <a href="#" @click="scrollToNewStructure">Farm Structure Inventory</a>
        </li>
        <li>
          <a href="#" @click="openNewEquipmentDialog">Farm Equipment and Machinery Inventory</a>
        </li>
        <li>
          <a href="#" @click="openOtherInventoryDialog">Other Inventories</a>
        </li>
      </ul>
    </div>
    <div class="content">
      <h1>Inventory Management</h1>
      <button @click="showDialog = true">New Structure</button>

      <div v-if="showDialog || showNewEquipmentDialog || showOtherInventoryDialog" class="dialog-overlay">
        <div class="dialog" v-if="showDialog">
          <h2>Create Structure</h2>
          <form @submit.prevent="createStructure">
            <label for="structure-id">Structure ID:</label>
            <input type="text" id="structure-id" v-model="structureId">

            <label for="structure-name">Name:</label>
            <input type="text" id="structure-name" v-model="structureName">

            <label for="structure-description">Description:</label>
            <textarea id="structure-description" v-model="structureDescription"></textarea>

            <button type="submit">Create</button>
            <button @click="cancelCreate">Cancel</button>
          </form>
        </div>
        <div class="dialog" v-show="showNewEquipmentDialog">
          <h2>Create Equipment</h2>
          <form>
            <label>ID/Plate number</label>
            <input type="text" v-model="newEquipment.idPlateNumber">

            <label>Serial number</label>
            <input type="text" v-model="newEquipment.serialNumber">

            <label>Engine</label>
            <input type="text" v-model="newEquipment.engine">

            <label>Date acquired</label>
            <input type="date" v-model="newEquipment.dateAcquired">

            <label>Purchase price</label>
            <input type="text" v-model="newEquipment.purchasePrice">

            <label>Equipment insured</label>
            <input type="checkbox" v-model="newEquipment.insured">

            <label>Description</label>
            <textarea v-model="newEquipment.description"></textarea>

            <button @click="createEquipment">Create</button>
            <button @click="cancelCreate">Cancel</button>
          </form>
        </div>
        <div class="dialog" v-show="showOtherInventoryDialog">
          <h2>Specify the Type of Inventory</h2>
          <form>
            <label>Type</label>
            <input type="text" v-model="newOtherInventory.type" placeholder="e.g. Vaccines, Drug, Seeds">

            <label>Variety</label>
            <input type="text" v-model="newOtherInventory.variety">

            <label>ID/Serial number</label>
            <input type="text" v-model="newOtherInventory.idSerialNumber">

            <label>Amount/length</label>
            <input type="number" v-model="newOtherInventory.amountOrLength">

            <label>Measurement Unit</label>
            <select id="measurementUnit" v-model="newOtherInventory.measurementUnit">
              <option value="quantity">quantity</option>
              <option value="kilogram">kilogram (kg)</option>
              <option value="gram">gram (g)</option>
              <option value="pound">pound (lb)</option>
              <option value="liter">liter (l)</option>
              <option value="tonne">tonne (t)</option>
              <option value="milliliter">milliliter (ml)</option>
              <option value="meter">meter (m)</option>
              <option value="feet">feet (f)</option>
              <option value="inch">inch (in)</option>
              <option value="dozen">dozen</option>
              <option value="barrel">barrel</option>
              <option value="bale">bale</option>
            </select>

            <label>Unit Price</label>
            <input type="text" v-model="newOtherInventory.unitPrice">

            <label>Description</label>
            <textarea v-model="newOtherInventory.description"></textarea>

            <button @click="createOtherInventory">Create</button>
            <button @click="cancelCreate">Cancel</button>
          </form>
        </div>
      </div>

      <div v-if="showTable" class="dialog-overlay">
        <div class="dialog">
          <div class="dialog-header">
            <h2>Structure Inventory</h2>
            <span class="close" @click="closeTable">&times;</span>
          </div>
          <table>
            <thead>
              <tr>
                <th>Structure ID</th>
                <th>Name</th>
                <th>Description</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="structure in structures" :key="structure.id">
                <td>
                  <span v-if="!structure.isEditing">{{ structure.id }}</span>
                  <input v-else type="text" v-model="structure.id">
                </td>
                <td>
                  <span v-if="!structure.isEditing">{{ structure.name }}</span>
                  <input v-else type="text" v-model="structure.name">
                </td>
                <td>
                  <span v-if="!structure.isEditing">{{ structure.description }}</span>
                  <textarea v-else v-model="structure.description"></textarea>
                </td>
                <td>
                  <button v-if="!structure.isEditing" @click="editStructure(structure)">Edit</button>
                  <button v-else @click="saveStructure(structure)">Save</button>
                  <button @click="deleteStructure(structure)">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
          <button @click="showDialog = true">Add Structure</button>
        </div>
      </div>

      <div v-show="showEquipmentTable">
        <div class="dialog">
          <div class="dialog-header">
            <h2>Equipment Inventory</h2>
            <button class="close" @click="closeEquipmentTable">&times;</button>
          </div>
          <table>
            <thead>
              <tr>
                <th>ID/Plate number</th>
                <th>Serial number</th>
                <th>Engine</th>
                <th>Date acquired</th>
                <th>Purchase price</th>
                <th>Insured</th>
                <th>Description</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="equipment in equipment">
                <td>
                  <span v-if="!equipment.isEditing">{{ equipment.idPlateNumber }}</span>
                  <input v-else type="text" v-model="equipment.idPlateNumber">
                </td>
                <td>
                  <span v-if="!equipment.isEditing">{{ equipment.serialNumber }}</span>
                  <input v-else type="text" v-model="equipment.serialNumber">
                </td>
                <td>
                  <span v-if="!equipment.isEditing">{{ equipment.engine }}</span>
                  <input v-else type="text" v-model="equipment.engine">
                </td>
                <td>
                  <span v-if="!equipment.isEditing">{{ equipment.dateAcquired }}</span>
                  <input v-else type="date" v-model="equipment.dateAcquired">
                </td>
                <td>
                  <span v-if="!equipment.isEditing">{{ equipment.purchasePrice }}</span>
                  <input v-else type="text" v-model="equipment.purchasePrice">
                </td>
                <td>
                  <span v-if="!equipment.isEditing">{{ equipment.insured ? 'Yes' : 'No' }}</span>
                  <input v-else type="checkbox" v-model="equipment.insured">
                </td>
                <td>
                  <span v-if="!equipment.isEditing">{{ equipment.description }}</span>
                  <textarea v-else type="text" v-model="equipment.description"></textarea>
                </td>
                <td>
                  <button v-if="!equipment.isEditing" @click="editEquipment(equipment)">Edit</button>
                  <button v-else @click="saveEquipment(equipment)">Save</button>
                  <button @click="deleteEquipment(equipment)">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <button @click="openNewEquipmentDialog">Add New Equipment</button>
      </div>

      <div v-show="showOtherInventoryTable">
        <div class="dialog">
          <div class="dialog-header">
            <h2>Other Inventories</h2>
            <button class="close" @click="closeOtherInventoryTable">&times;</button>
          </div>
          <table>
            <thead>
              <tr>
                <th>Type</th>
                <th>Variety</th>
                <th>ID/Serial Number</th>
                <th>Amount/Length</th>
                <th>Measurement Unit</th>
                <th>Unit Price</th>
                <th>Description</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="otherInventory in otherInventory">
                <td>
                  <span v-if="!otherInventory.isEditing">{{ otherInventory.type }}</span>
                  <input v-else type="text" v-model="otherInventory.type">
                </td>
                <td>
                  <span v-if="!otherInventory.isEditing">{{ otherInventory.variety }}</span>
                  <input v-else type="text" v-model="otherInventory.variety">
                </td>
                <td>
                  <span v-if="!otherInventory.isEditing">{{ otherInventory.idSerialNumber }}</span>
                  <input v-else type="text" v-model="otherInventory.idSerialNumber">
                </td>
                <td>
                  <span v-if="!otherInventory.isEditing">{{ otherInventory.amountOrLength }}</span>
                  <input v-else type="number" v-model="otherInventory.amountOrLength">
                </td>
                <td>
                  <span v-if="!otherInventory.isEditing">{{ otherInventory.measurementUnit }}</span>
                  <select v-else v-model="otherInventory.measurementUnit">
                    <option value="quantity">quantity</option>
                    <option value="kilogram">kilogram (kg)</option>
                    <option value="gram">gram (g)</option>
                    <option value="pound">pound (lb)</option>
                    <option value="liter">liter (l)</option>
                    <option value="tonne">tonne (t)</option>
                    <option value="milliliter">milliliter (ml)</option>
                    <option value="meter">meter (m)</option>
                    <option value="feet">feet (f)</option>
                    <option value="inch">inch (in)</option>
                    <option value="dozen">dozen</option>
                    <option value="barrel">barrel</option>
                    <option value="bale">bale</option>
                  </select>
                </td>
                <td>
                  <span v-if="!otherInventory.isEditing">{{ otherInventory.unitPrice }}</span>
                  <input v-else type="text" v-model="otherInventory.unitPrice">
                </td>
                <td>
                  <span v-if="!otherInventory.isEditing">{{ otherInventory.description }}</span>
                  <input v-else type="text" v-model="otherInventory.description">
                </td>
                
                <td>
                  <button v-if="!otherInventory.isEditing" @click="editOtherInventory(otherInventory)">Edit</button>
                  <button v-else @click="saveOtherInventory(otherInventory)">Save</button>
                  <button @click="deleteOtherInventory(otherInventory)">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <button @click="openOtherInventoryDialog">Add New Item</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FarmInventory',
  data() {
    return {
      showDialog: false,
      showTable: false,
      newStructure: {
        structureId: '',
        structureName: '',
        structureDescription: '',
      },
      structures: [],
      showNewEquipmentDialog: false,
      showEquipmentTable: false,
      newEquipment: {
        idPlateNumber: '',
        serialNumber: '',
        engine: '',
        dateAcquired: '',
        purchasePrice: '',
        insured: false,
        description: ''
      },
      equipment: [],
      showOtherInventoryDialog: false,
      showOtherInventoryTable: false,
      newOtherInventory: {
        type: '',
        variety: '',
        idSerialNumber: '',
        amountOrLength: '',
        measurementUnit: '',
        unitPrice: '',
        description: ''
      },
      otherInventory: []
    };
  },
  methods: {
    scrollToNewStructure() {
      const button = document.querySelector('.new-structure-button');
      if (button) {
        button.scrollIntoView({ behavior: 'smooth' });
      }
    },
    createStructure() {
      const newStructure = {
        id: this.structureId,
        name: this.structureName,
        description: this.structureDescription,
        isEditing: false
      };
      this.structures.push(newStructure);
      this.showDialog = false;
      this.showTable = true;
    },
    cancelCreate() {
      this.showDialog = false;
    },
    editStructure(structure) {
      structure.isEditing = true;
    },
    saveStructure(structure) {
      structure.isEditing = false;
    },
    deleteStructure(structure) {
      const index = this.structures.indexOf(structure);
      if (index > -1) {
        this.structures.splice(index, 1);
      }
    },
    closeTable() {
      this.showTable = false;
    },

    openNewEquipmentDialog() {
      this.showNewEquipmentDialog = true;
    },
    createEquipment() {
      this.equipment.push({ ...this.newEquipment });
      this.showNewEquipmentDialog = false;
      this.showEquipmentTable = true;
      this.newEquipment = {
        idPlateNumber: '',
        serialNumber: '',
        engine: '',
        dateAcquired: '',
        purchasePrice: '',
        insured: false,
        description: '',
        isEditing: false
      };
    },
    editEquipment(equipment) {
      equipment.isEditing = true;
    },
    saveEquipment(equipment) {
      equipment.isEditing = false;
    },
    deleteEquipment(equipment) {
      const index = this.equipment.indexOf(equipment);
      if (index !== -1) {
        this.equipment.splice(index, 1);
      }
    },
    closeEquipmentTable() {
      this.showEquipmentTable = false;
    },

    openOtherInventoryDialog() {
      this.showOtherInventoryDialog = true;
    },

    createOtherInventory() {
      this.otherInventory.push({ ...this.newOtherInventory });
      this.showOtherInventoryDialog = false;
      this.showOtherInventoryTable = true;
      this.newOtherInventory = {
        type: '',
        variety: '',
        idSerialNumber: '',
        amountOrLength: '',
        measurementUnit: '',
        unitPrice: '',
        description: '',
        isEditing: false
      };
    },
    editOtherInventory(otherInventory) {
      otherInventory.isEditing = true;
    },
    saveOtherInventory(otherInventory) {
      otherInventory.isEditing = false;
    },
    deleteOtherInventory(otherInventory) {
      const index = this.otherInventory.indexOf(otherInventory);
      if (index !== -1) {
        this.otherInventory.splice(index, 1);
      }
    },
    closeOtherInventoryTable() {
      this.showOtherInventoryTable = false;
    },
  }
};
</script>

<style>
.farm-inventory {
  display: flex;
}

.left-nav {
  width: 200px;
  background-color: #f1f1f1;
  padding: 20px;
}

.left-nav ul {
  list-style-type: none;
  padding: 0;
}

.left-nav ul li {
  margin-bottom: 10px;
}

.content {
  flex-grow: 1;
  padding: 20px;
}

.dialog-overlay {
  position: fixed;
  border-radius: 5px;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.dialog {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
}

.dialog-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

tr:nth-child(even) {
  background-color: #f2f2f2;
}

.close {
  color: #db1212;
  cursor: pointer;
}

button {
  margin-top: 10px;
  background-color: rgb(71, 219, 219);
  border-radius: 10px;
  border: none;
}
</style>
