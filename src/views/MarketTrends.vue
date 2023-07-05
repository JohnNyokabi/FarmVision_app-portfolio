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
          <a href="#" @click="openNewPickupLocationDialog">Pickup Location</a>
        </li>
      </ul>
    </div>
    
    <h3 class="market-trends__title">For all your Market Requirements</h3>
    <div class="content">
      <div v-if="showNewProductDialog || showOrderDialog || showPickupLocationDialog" class="dialog-overlay">
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
            <button @click="cancelCreateProduct">Cancel</button>
          </form>
        </div>

        <div v-if="showOrderDialog" class="dialog">
          <h2>Product Orders</h2>
          <form>
            <label>ID</label>
            <input type="Number" v-model="newOrder.id">
            <label>Customer Name</label>
            <input type="text" v-model="newOrder.customerName">
            <label>Status</label>
            <select id="status" v-model="newOrder.status">
              <option value="draft">Draft</option>
              <option value="ordered">Ordered</option>
              <option value="available">Available</option>
              <option value="sold">Sold Out</option>
            </select>
            <label>Order Date</label>
            <input type="date" v-model="newOrder.orderDate">
            <label>Product</label>
            <select id="product" v-model="newOrder.product">
              <option disabled value="product">Please select product</option>
              <option v-for="product in products" :value="product.productId">{{ product.productName }}</option>
            </select>
            <a v-if="products.length === 0" href="#" @click="openNewProductDialog">Create a new product</a>
            <label>Payment method</label>
            <select id="paymentMethod" v-model="newOrder.paymentMethod">
              <option value="Cash">Cash</option>
              <option value="Card">Card</option>
              <option value="Cheque">Cheque</option>
              <option value="mobileTransfer">Mobile Transfer</option>
              <option value="wireTransfers">Wire Transfer</option>
            </select>
            <label>Payment Status</label>
            <select id="paymentStatus" v-model="newOrder.paymentStatus">
              <option value="pending">Pending</option>
              <option value="Paid">Paid</option>
              <option value="partiallyPaid">Partially Paid</option>
              <option value="due">Due</option>
              <option value="cancelled">Cancelled</option>
            </select>
            <label>Delivery Option</label>
            <select id="deliveryOption" v-model="newOrder.deliveryOption">
              <option value="delivery">delivery</option>
              <option value="pickup">Pick up</option>
              <option value="shipped">Shipped</option>
            </select>
            <label>Delivery date</label>
            <input type="date" v-model="newOrder.deliveryDate">
            <label>Customer Remarks</label>
            <textarea v-model="newOrder.customerRemarks"></textarea>

            <button @click="createOrder">Create</button>
            <button @click="cancelCreateOrder">Cancel</button>
          </form>
        </div>

        <div v-if="showPickupLocationDialog" class="dialog">
          <form>
            <label>Name</label>
            <input type="text" v-model="newLocation.name">
            <label>Country</label>
            <input type="text" v-model="newLocation.country">
            <label>State/Province</label>
            <input type="text" v-model="newLocation.state">
            <label>Residence</label>
            <input type="text" v-model="newLocation.residence" placeholder="Kericho, Nakuru, Murang'a">
            <label>Address</label>
            <input type="number" v-model="newLocation.address">
            <label>Postal Code</label>
            <input type="number" v-model="newLocation.postalCode">
            <label>Phone Number</label>
            <input type="number" v-model="newLocation.phoneNumber">
            <label>Day</label>
            <select id="day" v-model="newLocation.day">
              <option value="mon">Mon</option>
              <option value="tue">Tue</option>
              <option value="wed">Wed</option>
              <option value="thur">Thur</option>
              <option value="fri">Fri</option>
              <option value="sat">Sat</option>
              <option value="sun">Sun</option>
            </select>
            <label>Date</label>
            <input type="date" v-model="newLocation.date">
            <label>Time</label>
            <input type="time" v-model="newLocation.time">
            <label>Details</label>
            <textarea type="text" v-model="newLocation.details"></textarea>
          </form>
          <button @click="createPickupLocation">Create</button>
          <button @click="cancelCreatePickupLocation">Cancel</button>
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
              <tr v-for="product in products">
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
      <div v-show="showOrderTable">
        <div class="dialog">
          <div class="dialog-header">
            <h2>Product Orders</h2>
            <button class="close" @click="closeOrderTable">&times;</button>
          </div>
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Customer Name</th>
                <th>Status</th>
                <th>Order Date</th>
                <th>Product</th>
                <th>Payment Method</th>
                <th>Payment Status</th>
                <th>Delivery Option</th>
                <th>Delivery Date</th>
                <th>Customer Remarks</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="order in orders">
                <td>
                  <span v-if="!order.isEditing">{{ order.id }}</span>
                  <input v-else type="number" v-model="order.id">
                </td>
                <td>
                  <span v-if="!order.isEditing">{{ order.customerName }}</span>
                  <input v-else type="text" v-model="order.customerName">
                </td>
                <td>
                  <span v-if="!order.isEditing">{{ order.status }}</span>
                  <select v-else v-model="order.status">
                    <option value="draft">Draft</option>
                    <option value="ordered">Ordered</option>
                    <option value="available">Available</option>
                    <option value="sold">Sold Out</option>
                  </select>
                </td>
                <td>
                  <span v-if="!order.isEditing">{{ order.orderDate }}</span>
                  <input v-else type="date" v-model="order.orderDate">
                </td>
                <td>
                  <span v-if="!order.isEditing">{{ order.product }}</span>
                  <select v-else v-model="order.product">
                    <option disabled value="product">product</option>
                    <option v-for="product in products" :value="product.productId">{{ product.productName }}</option>
                  </select>
                </td>
                <td>
                  <span v-if="!order.isEditing">{{ order.paymentMethod }}</span>
                  <select v-else v-model="order.paymentMethod">
                    <option value="Cash">Cash</option>
                    <option value="Card">Card</option>
                    <option value="Cheque">Cheque</option>
                    <option value="mobileTransfer">Mobile Transfer</option>
                    <option value="wireTransfers">Wire Transfer</option>
                  </select>
                </td>
                <td>
                  <span v-if="!order.isEditing">{{ order.paymentStatus }}</span>
                  <select v-else v-model="order.paymentStatus">
                    <option value="pending">Pending</option>
                    <option value="Paid">Paid</option>
                    <option value="partiallyPaid">Partially Paid</option>
                    <option value="due">Due</option>
                    <option value="cancelled">Cancelled</option>
                  </select>
                </td>
                <td>
                  <span v-if="!order.isEditing">{{ order.deliveryOption }}</span>
                  <select v-else v-model="order.deliveryOption">
                    <option value="delivery">delivery</option>
                    <option value="pickup">Pick up</option>
                    <option value="shipped">Shipped</option>
                  </select>
                </td>
                <td>
                  <span v-if="!order.isEditing">{{ order.deliveryDate }}</span>
                  <input v-else type="date" v-model="order.deliveryDate">
                </td>
                <td>
                  <span v-if="!order.isEditing">{{ order.customerRemarks }}</span>
                  <textarea v-else type="text" v-model="order.customerRemarks"></textarea>
                </td>
                <td>
                  <button v-if="!order.isEditing" @click="editOrder(order)">Edit</button>
                  <button v-else @click="saveOrder(order)">Save</button>
                  <button @click="deleteOrder(order)">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <button @click="openNewOrderDialog">Add Order</button>
      </div>
      <div v-show="showLocationTable">
        <div class="dialog">
          <div class="dialog-header">
            <h2>Pickup Location</h2>
            <button class="close" @click="closeLocationTable">&times;</button>
          </div>
          <table>
            <thead>
              <tr>
                <th>Name</th>
                <th>Country</th>
                <th>State/Province</th>
                <th>Residence</th>
                <th>Address</th>
                <th>Postal Code</th>
                <th>Phone Number</th>
                <th>Day</th>
                <th>Date</th>
                <th>Time</th>
                <th>Details</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="location in locations">
                <td>
                  <span v-if="!location.isEditing">{{location.name }}</span>
                  <input v-else type="text" v-model="location.name">
                </td>
                <td>
                  <span v-if="!location.isEditing">{{ location.country }}</span>
                  <input v-else type="text" v-model="location.country">
                </td>
                <td>
                  <span v-if="!location.isEditing">{{ location.state }}</span>
                  <input v-else type="text" v-model="location.state">
                </td>
                <td>
                  <span v-if="!location.isEditing">{{ location.residence }}</span>
                  <input v-else type="text" v-model="location.residence">
                </td>
                <td>
                  <span v-if="!location.isEditing">{{ location.address }}</span>
                  <input v-else type="number" v-model="location.address">
                </td>
                <td>
                  <span v-if="!location.isEditing">{{ location.postalCode }}</span>
                  <input v-else type="number" v-model="location.postalCode">
                </td>
                <td>
                  <span v-if="!location.isEditing">{{ location.phoneNumber }}</span>
                  <input v-else type="number" v-model="location.phoneNumber">
                </td>
                <td>
                  <span v-if="!location.isEditing">{{ location.day }}</span>
                  <select v-else v-model="location.day">
                    <option value="mon">Mon</option>
                    <option value="tue">Tue</option>
                    <option value="wed">Wed</option>
                    <option value="thur">Thur</option>
                    <option value="fri">Fri</option>
                    <option value="sat">Sat</option>
                    <option value="sun">Sun</option>
                  </select>
                </td>
                <td>
                  <span v-if="!location.isEditing">{{ location.date }}</span>
                  <input v-else type="date" v-model="location.date">
                </td>
                <td>
                  <span v-if="!location.isEditing">{{ location.time }}</span>
                  <input v-else type="time" v-model="location.time">
                </td>
                <td>
                  <span v-if="!location.isEditing">{{ location.details }}</span>
                  <textarea v-else type="text" v-model="location.details"></textarea>
                </td>
                <td>
                  <button v-if="!location.isEditing" @click="editLocation(location)">Edit</button>
                  <button v-else @click="saveLocation(location)">Save</button>
                  <button @click="deleteLocation(location)">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <button @click="openNewPickupLocationDialog">Add Pick Location</button>
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
        productId: "",
        productName: "",
        productType: "",
        amount: "",
        measurementUnit: "",
        retailPrice: "",
        wholesalePrice: "",
        status: "",
        delivery: false,
        pickup: false,
        shipped: false,
        description: "",
      },
      products: [],
      showOrderDialog: false,
      showOrderTable: false,
      newOrder: {
        id: null,
        customerName: "",
        status: "",
        orderDate: "",
        product: "",
        paymentMethod: "",
        paymentStatus: "",
        deliveryOption: "",
        deliveryDate: "",
        customerRemarks: "",
      },
      orders:[],
      showPickupLocationDialog: false,
      showLocationTable: false,
      newLocation: {
        name: "",
        country: "",
        state: "",
        residence: "",
        address: "",
        postalCode: "",
        phoneNumber: "",
        day: "",
        date: "",
        time: "",
        details: ""
      },
      locations: [],
    }
  },
  computed: {
    availableProducts() {
      return this.products.filter((product) => product.status === 'available');
    }
  },
  methods: {
    openNewProductDialog() {
      this.showNewProductDialog = true;
    },
    openNewOrderDialog() {
      this.showOrderDialog = true;
    },
    openNewPickupLocationDialog() {
      this.showPickupLocationDialog = true;
    },
    createProduct () {
      this.products.push({...this.newProduct});
      this.showNewProductDialog = false;
      this.showProductTable = true;
      this.newProduct = {
        productId: null,
        productName: "",
        productType: "",
        amount: null,
        measurementUnit: "quantity",
        retailPrice: null,
        wholesalePrice: null,
        status: "draft",
        delivery: false,
        pickup: false,
        shipped: false,
        description: ""
      };
      this.newOrder.product = this.products[this.products.length - 1].productId;
    },
    createOrder () {
      if (this.newOrder.product !== "") {
        this.orders.push({...this.newOrder});
        this.newOrder = {
          id: null,
          customerName: "",
          status: "",
          orderDate: "",
          product: "",
          paymentMethod: "",
          paymentStatus: "",
          deliveryOption: "",
          deliveryDate: "",
          customerRemarks: ""
        };
        this.showOrderDialog = false;
        this.showOrderTable = true;
      }
    },
    createPickupLocation () {
      this.locations.push({...this.newLocation});
      this.showPickupLocationDialog = false;
      this.showLocationTable = true;
      this.newLocation = {
        name: "",
        country: "",
        state: "",
        residence: "",
        address: "",
        postalCode: "",
        phoneNumber: "",
        day: "",
        date: "",
        time: "",
        details: ""
      };
    },
    cancelCreateProduct() {
      this.showNewProductDialog = false;
    },
    cancelCreateOrder() {
      this.showOrderDialog = false;
    },
    cancelCreatePickupLocation() {
      this.showPickupLocationDialog = false;
    },
    editProduct(product) {
      product.isEditing = true;
    },
    editOrder(order) {
      order.isEditing = true;
    },
    editLocation(location) {
      location.isEditing = true;
    },
    saveProduct(product) {
      product.isEditing = false;
    },
    saveOrder(order) {
      order.isEditing = false;
    },
    saveLocation(location) {
      location.isEditing = false;
    },
    deleteProduct(product) {
      const index = this.products.indexOf(product);
      if (index !== -1) {
        this.products.splice(index, 1);
      }
    },
    deleteOrder(order) {
      const index = this.orders.indexOf(order);
      if (index !== -1) {
        this.orders.splice(index, 1);
      }
    },
    deleteLocation(location) {
      const index = this.locations.indexOf(location);
      if (index !== -1) {
        this.locations.splice(index, 1);
      }
    },
    closeProductTable() {
      this.showProductTable = false;
    },
    closeOrderTable() {
      this.showOrderTable = false;
    },
    closeLocationTable() {
      this.showLocationTable = false;
    }
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
