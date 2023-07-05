<template>
  <form @submit="onSubmit" class="add-form">
    <div class="form-control">
      <label>Task</label>
      <input type="text" v-model="text" name="text" placeholder="Add Task" />
    </div>

    <div class="form-control">
      <label>Day & Time</label>
      <input v-model="day"
        type="text"
        name="day"
        placeholder="Add Day & Time" 
      /> 
    </div>

    <div class="form-control form-control-check">
      <label>Set Reminder</label>
      <input v-model="reminder"
        type="checkbox"
        name="reminder"
      />
    </div>

    <span @click="onSubmit" class="btn" id="btn2">Save Task</span>

  </form>
</template>

<script>
export default {
  name: 'AddTask',
  data() {
    return {
      text: '',
      day: '',
      reminder: false
    }
  },
  methods: {
    onSubmit(e) {
      e.preventDefault();
      
      if(!this.text) {
        alert('please add a task')
        return
      }

      const newTask = {
        //id: Math.floor(Math.random() * 100000),
        text: this.text,
        day: this.day,
        reminder: this.reminder
      }

      this.$emit('add-task', newTask);

      this.text = '',
      this.day = '',
      this.reminder = false
    }
  }
}
</script>

<style scoped>
.add-form {
  margin-bottom: 40px;
}

.form-control {
  margin: 20px 0;
}

.form-control label {
  display: block;
}

.form-control input {
  width: 100%;
  height: 40px;
  margin: 5px;
  padding: 3px 7px;
  font-size: 17px;
}

.form-control-check {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.form-control-check label {
  flex: 1;
}

.form-control-check input {
  flex: 2;
  height: 20px;
}

.btn {
  margin: 20px;
  cursor: pointer;
  position: relative;
  padding: 10px 30px;
  background: rgb(173, 172, 172);
  font-size: 20px;
  text-transform: capitalize;
  border-top-right-radius: 10px;
  border-bottom-left-radius: 10px;
  transition: all 1s;
}

.btn:after, .btn:before {
  content: " ";
  width: 10px;
  height: 10px;
  position: absolute;
  border: 0px solid #9a1b1b;
  transition: all 1s;
}

.btn:after {
  top: -1px;
  left: -1px;
}

.btn:before {
  bottom: -1px;
  right: -1px;
}

#btn2:after {
  border-top: 5px solid #dd03d2;
  border-left: 5px solid #dd03d2;
}

#btn2:before {
  border-bottom: 5px solid #dd03d2;
  border-right: 5px solid #dd03d2;
}

.btn:hover {
  border-top-right-radius: 0px;
  border-bottom-left-radius: 0px;
  letter-spacing: 3px;
}

.btn:hover:before, .btn:hover:after {
  width: 100%;
  height: 100%;
}
</style>
