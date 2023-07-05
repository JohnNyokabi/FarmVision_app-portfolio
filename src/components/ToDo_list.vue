<template>
  <div class="todo-container">
    <TaskHeader @toggle-add-task="toggleAddTask" title="Task Tracker" :showAddTask="showAddTask" />
    <div v-show="showAddTask">
      <AddTask @add-task="addTask" />
    </div>
    <Tasks @toggle-reminder="toggleReminder" @delete-task="deleteTask" :tasks="tasks" />
  </div>
</template>

<script>
import TaskHeader from './TaskHeader.vue';
import Tasks from './Tasks.vue';
import AddTask from './AddTask.vue';

export default {
  name: 'ToDo_list',
  components: {
    TaskHeader,
    Tasks,
    AddTask
  },
  data() {
    return {
      tasks: [],
      showAddTask: false
    }
  },
  methods: {
    toggleAddTask() {
      this.showAddTask = !this.showAddTask
    },
    async addTask(task) {
      const res = await fetch('http://localhost:5005/tasks', {
        method: 'POST',
        headers: {
          'content-type': 'application/json'
        },
        body:JSON.stringify(task)
      })
      const data = await res.json()

      this.tasks = [...this.tasks, data]
    },
    async deleteTask(id) {
      if (confirm('Are you sure?')) {
        const res = await fetch(`http://localhost:5005/tasks/${id}`, {
          method: 'DELETE',
        })
        res.status === 200 ? (this.tasks = this.tasks.filter((task) => task.id !== id)) : alert('Error deleting task') 
      }
    },
    async  toggleReminder(id) {
      const taskToToggle = await this.fetchTask(id)
      const updateTask = {...taskToToggle, reminder: !taskToToggle.reminder}
      const res = await fetch(`http://localhost:5005/tasks/${id}`, {
        method: 'PUT',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(updateTask)
      })
      const data = await res.json()

      this.tasks = this.tasks.map((task) => task.id === id ? {...task, reminder: data.reminder} : task);
    },
    async fetchTasks() {
      const res = await fetch('http://localhost:5005/tasks')
      const data = await res.json()

      return data
    },
    async fetchTask(id) {
      const res = await fetch(`http://localhost:5005/tasks/${id}`)
      const data = await res.json()

      return data
    }
  },
  async created() {
    this.tasks = await this.fetchTasks()
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap');

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Poppins', sans-serif;
}

.todo-container {
  min-width: 700px;
  margin: 30px auto;
  overflow: auto;
  min-height: 300px;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
}
</style>