<template>
  <div class="about-view">
    <h1>This is an about page</h1>
  </div>
</template>

<script setup>
import {onMounted} from 'vue'

onMounted(() => {
  document.title = "关于 CMDB"
})
</script>

<style scoped>
.about-view {
  width: 100%;
  height: 100%;
  display: flex;
}
</style>
