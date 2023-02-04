<template>
  <div class="div-step-view">
    <n-card style="width: 100%; height: 100%;">
      <div style="width:100%; height:100%; display: flex; flex-direction: column;">
        <div class="step-form-content">
          farm contentdiv-step-view
        </div>
        <div class="step-op-area">
          <n-button strong style="margin-right: 10px">取&nbsp;消</n-button>
          <n-button strong type="primary" @click="handleStepNextButtonClicked">下&nbsp;一&nbsp;步</n-button>
        </div>
      </div>
    </n-card>
  </div>
</template>

<script setup>
import {useRouter} from 'vue-router'
import {onMounted} from "vue";

const router = useRouter();
const emit = defineEmits(['update-step-index', 'update-step-status'])

function handleStepNextButtonClicked() {
  router.push({
    path: '/dashboard/config/vcs/target-step'
  });
}

onMounted(() => {
  emit('update-step-index',"2")
})
</script>

<style scoped>
.div-step-view {
  width: 100%;
  height: 100%;
  padding-top: 20px;
}

.step-form-content {
  flex: 1;
}

.step-op-area {
  display: flex;
  justify-content: flex-end;
}
</style>