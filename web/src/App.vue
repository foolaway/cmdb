<script setup>
// 用户的系统,使用的是否是深色模式
import {onMounted, ref} from "vue";
import {darkTheme}  from 'naive-ui'

let systemDarkModeMedia = window.matchMedia("(prefers-color-theme: dark)");
let useDarkTheme = ref(systemDarkModeMedia.matches)

// 当挂载时
onMounted(() => {
  let systemThemCallback = (e) => {
    let prefersDarkMode = e.matches;
    useDarkTheme.value = !!prefersDarkMode;
  };

  if (typeof systemDarkModeMedia.addEventListener === 'function'){
    systemDarkModeMedia.addEventListener('change', systemThemCallback)
  } else if (typeof systemDarkModeMedia.addListener === 'function'){
    systemDarkModeMedia.addListener(systemThemCallback);
  }

  // 强制使用深色模式
   useDarkTheme.value = true
})
</script>

<template>
  <div class="app-view">
    <n-config-provider :theme="useDarkTheme ? darkTheme: null">
      <router-view style="height: 100%; height: 100%"></router-view>
    </n-config-provider>
  </div>
</template>

<style scoped>
.app-view {
  width: 100%;
  height: 100%;
  display: flex;
}
</style>
