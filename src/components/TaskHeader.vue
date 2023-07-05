<template>
  <header>
    <h1>{{ title }}</h1>
    <Button @batton-click="$emit('toggle-add-task')" :text="showAddTask ? 'Close' : 'Add Task'"/>
  </header>
</template>

<script>
import Button from './Button.vue';

export default {
  name: 'Header',
  components: {
    Button
  },
  props: {
    title: String,
    showAddTask: Boolean
  }
}
</script>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}
</style>