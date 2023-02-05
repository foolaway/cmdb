<template>
  <div class="table-operation-area-button-group">
    <n-button type="info" v-if="props.isShowDetail" @click="onDetailButtonClicked" secondary strong size="tiny" style="margin-right: 5px">详情</n-button>
    <n-button type="warning" v-if="props.isShowModify" @click="onModifyButtonClicked" secondary strong size="tiny" style="margin-right: 5px">修改</n-button>
    <n-button type="error" v-if="props.isShowDelete" @click="onDeleteButtonClicked" secondary strong size="tiny" style="margin-right: 5px">删除</n-button>
  </div>
</template>

<script setup>
const props = defineProps({
  isShowDetail: Boolean,
  isShowModify: Boolean,
  isShowDelete: Boolean,
  onDetailButtonClicked: Function,
  onModifyButtonClicked: Function,
  onDeleteButtonClicked: Function,
})
</script>

<style scoped>
.table-operation-area-button-group {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
}
</style>