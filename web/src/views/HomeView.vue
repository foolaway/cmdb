<template>
  <div class="home-view">
    <div class="welcome-text">欢迎使用 CMDB</div>
    <div class="version-text">V1.0.0</div>
    <div class="left-img">
      <img src="../assets/images/no-network.svg" alt="" style="width: 100%;height: 100%">
    </div>
    <div class="right-img">
      <img src="../assets/images/loading.svg" alt="" style="width: 100%;height: 100%">
    </div>
  </div>
</template>

<style scoped>
.home-view {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

.welcome-text {
  font-size: 20pt;
}

.version-text {
  margin-top: 10px;
  font-size: 16pt;
}

.left-img {
  width: 120px;
  height: 120px;
  position: absolute;
  left: 0;
  bottom: 0;
}

.right-img {
  width: 120px;
  height: 120px;
  position: absolute;
  right: 0;
  bottom: 0;
}

</style>
