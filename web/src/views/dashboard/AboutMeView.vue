<template>
  <div class="about-me-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>关于我</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <div class="cards">
      <div class="card">
        <n-card>
          <div class="car-title">姓名</div>
          <div class="car-content">小张 / Z3333333 / (+86)1333333333 </div>
        </n-card>
      </div>
      <div class="card">
        <n-card>
          <div class="car-title">组织架构</div>
          <div class="car-content">A公司事业群/基础架构部</div>
        </n-card>
      </div>
      <div class="card">
        <n-card>
          <div class="car-title">使用 CMDB 天数</div>
          <div class="car-content">112天</div>
        </n-card>
      </div>
    </div>
    <div style="width: 100%; padding-top: 20px; padding-left: 15px; font-size: 8pt; color: gray"><span>更多内容敬请期待...</span></div>
  </div>
</template>
<script setup>

</script>

<style scoped>
.about-me-view {
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
}

.cards {
  width: 100%;
  display: flex;
}

.card {
  width: 500px;
  padding: 10px 15px 10px 15px;
}

.car-title {
  height: 50%;
  font-size: 12pt;
  color: gray;
  display: flex;
  align-items: end;
  padding-bottom: 5px;
}

.car-content {
  height: 50%;
  padding-top: 5px;
  font-size: 12pt;
}

</style>