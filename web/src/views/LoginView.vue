<template>
  <div class="login-view">
    Login
  </div>
</template>

<script setup>
import {onMounted} from 'vue'

onMounted(()=> {
  document.title = "登录 CMDB"
})
</script>

<style scoped>
.login-view {
  width: 100%;
  height: 100%;
}
</style>