<template>
  <div class="market-trends">
    <div class="left-nav">
      <ul>
        <li>
          <a href="#" @click="openNewProductDialog">Product</a>
        </li>
        <li>
          <a href="#" @click="openNewOrderDialog">Order</a>
        </li>
        <li>
          <a href="#" @click="openNewPickUpLocationDialog">Pick Up Location</a>
        </li>
      </ul>
    </div>
    
    <h3 class="market-trends__title">For all your Market Requirements</h3>
    <div class="content">
      <div v-if="showNewProductDialog" class="dialog-overlay">
        <div v-if="showNewProductDialog" class="dialog">
          <h2>Create New Product</h2>
          <form>
            <label>Product ID</label>
            <input type="text" v-model="newProduct.productId">

            <label>Product Name</label>
            <input type="text" v-model="newProduct.productName">

            <label>Product Type</label>
            <input type="text" v-model="newProduct.productType" placeholder="dairy, pork, vegetables...">

            <label>Amount/weight</label>
            <input type="number" v-model="newProduct.amount">

            <label>Measurement Unit</label>
            <select id="measurementUnit" v-model="newProduct.measurementUnit">
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

            <label>Retail Price</label>
            <input type="number" v-model="newProduct.retailPrice">

            <label>Wholesale Price</label>
            <input type="number" v-model="newProduct.wholesalePrice">

            <label>Status</label>
            <select id="status" v-model="newProduct.status">
              <option value="draft">Draft</option>
              <option value="ordered">Ordered</option>
              <option value="available">Available</option>
              <option value="sold">Sold Out</option>
            </select>
            
            <label>Delivery Options</label>
            <div>
              <label>
                <input type="checkbox" v-model="newProduct.delivery" />
                Delivery
              </label>
              <label>
                <input type="checkbox" v-model="newProduct.pickup" />
                Pick up
              </label>
              <label>
                <input type="checkbox" v-model="newProduct.shipped" />
                Shipped
              </label>
            </div>

            <label>Description</label>
            <textarea v-model="newProduct.description"></textarea>

            <button @click="createProduct">Create</button>
            <button @click="cancelCreate">Cancel</button>
          </form>
        </div>
      </div>

      <div v-show="showProductTable">
        <div class="dialog">
          <div class="dialog-header">
            <h2>Products</h2>
            <button class="close" @click="closeProductTable">&times;</button>
          </div>
          <table>
            <thead>
              <tr>
                <th>Product ID</th>
                <th>Product Name</th>
                <th>Product Type</th>
                <th>Amount/Weight</th>
                <th>Measurement Unit</th>
                <th>Retail Price</th>
                <th>Wholesale Price</th>
                <th>Status</th>
                <th>Delivery Options</th>
                <th>Description</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="product in product">
                <td>
                  <span v-if="!product.isEditing">{{ product.productId}}</span>
                  <input v-else type="text" v-model="product.productId">
                </td>
                <td>
                  <span v-if="!product.isEditing">{{ product.productName }}</span>
                  <input v-else type="text" v-model="product.productName">
                </td>
                <td>
                  <span v-if="!product.isEditing">{{ product.productType }}</span>
                  <input v-else type="text" v-model="product.productType">
                </td>
                <td>
                  <span v-if="!product.isEditing">{{ product.amount }}</span>
                  <input v-else type="number" v-model="product.amount">
                </td>
                <td>
                  <span v-if="!product.isEditing">{{ product.measurementUnit }}</span>
                  <select v-else v-model="product.measurementUnit">
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
                  <span v-if="!product.isEditing">{{ product.retailPrice }}</span>
                  <input v-else type="text" v-model="product.retailPrice">
                </td>
                <td>
                  <span v-if="!product.isEditing">{{ product.wholesalePrice }}</span>
                  <input v-else type="text" v-model="product.wholesalePrice">
                </td>
                <td>
                  <span v-if="!product.isEditing">{{ product.status }}</span>
                  <select v-else v-model="product.status">
                    <option value="draft">Draft</option>
                    <option value="ordered">Ordered</option>
                    <option value="available">Available</option>
                    <option value="sold">Sold Out</option>
                  </select>
                </td>
                <td>
                  <span v-if="!product.isEditing">
                    <span v-if="product.delivery">Delivery </span>
                    <span v-if="product.pickup">Pick up </span>
                    <span v-if="product.shipped">Shipped</span>
                    <span v-if="!product.delivery && !product.pickup && !product.shipped">N/A</span>
                  </span>
                  <div v-else>
                    <label>
                      <input type="checkbox" v-model="product.delivery" />
                      Delivery
                    </label>
                    <label>
                      <input type="checkbox" v-model="product.pickup" />
                      Pick up
                    </label>
                    <label>
                      <input type="checkbox" v-model="product.shipped" />
                      Shipped
                    </label>
                  </div>
                </td>
                <td>
                  <span v-if="!product.isEditing">{{ product.description }}</span>
                  <input v-else type="text" v-model="product.description">
                </td>
                
                <td>
                  <button v-if="!product.isEditing" @click="editProduct(product)">Edit</button>
                  <button v-else @click="saveProduct(product)">Save</button>
                  <button @click="deleteProduct(product)">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <button @click="openNewProductDialog">Add Product</button>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'MarketTrends',
  data () {
    return {
      showNewProductDialog: false,
      showProductTable: false,
      newProduct: {
        productId: '',
        productName: '',
        productType: '',
        amount: '',
        measurementUnit: '',
        retailPrice: '',
        wholesalePrice: '',
        status: '',
        delivery: false,
        pickup: false,
        shipped: false,
        description: '',
      },
      product: [],
    }
  },
  methods: {
    openNewProductDialog() {
      this.showNewProductDialog = true;
    },
    createProduct () {
      this.product.push({...this.newProduct});
      this.showNewProductDialog = false;
      this.showProductTable = true;
      this.newProduct = {
        productId: '',
        productName: '',
        productType: '',
        amount: '',
        measurementUnit: '',
        retailPrice: '',
        wholesalePrice: '',
        status: '',
        delivery: false,
        pickup: false,
        shipped: false,
        description: ''
      };
    },
    editProduct(product) {
      product.isEditing = true;
    },
    saveProduct(product) {
      product.isEditing = false;
    },
    deleteProduct(product) {
      const index = this.product.indexOf(product);
      if (index !== -1) {
        this.product.splice(index, 1);
      }
    },
    closeProductTable() {
      this.showProductTable = false;
    },
  }
}; 
</script>

<style scoped>
.market-trends {
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
  min-height: 300px;
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
