<template>
  <span @click.prevent="onClick()" class="btn" id="btn1">{{ text }}</span>
</template>

<script>
export default {
  name: 'Button',
  props: {
    text: {
      String
    }
  },
  methods: {
    onClick() {
      this.$emit('batton-click')
    }
  },
}
</script>

<style scoped>
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

#btn1:after {
  border-top: 5px solid #7EDD03;
  border-left: 5px solid #7EDD03;
}

#btn1:before {
  border-bottom: 5px solid #7EDD03;
  border-right: 5px solid #7EDD03;
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