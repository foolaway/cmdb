<template>
    <div class="exec-step-view">
      <n-card style="width: 100%; height: 100%;">
        <div style="width:100%; height:100%; display: flex; flex-direction: column;">
          <div class="step-form-content">
            farm contentdiv-step-view
          </div>
          <div class="step-op-area">
            <n-button strong style="margin-right: 10px">取&nbsp;消</n-button>
            <n-button strong style="margin-right: 10px" type="primary" @click="handleStepNextButtonClicked" :loading="submitButtonLoading">提&nbsp;交</n-button>
            <n-button strong type="primary" @click="handleStepNextButtonClicked" :loading="submitNohupButtonLoading">提&nbsp;交,但&nbsp;放&nbsp;置&nbsp;到&nbsp;后&nbsp;台</n-button>
          </div>
        </div>
      </n-card>
    </div>
</template>

<script setup>
import {useRouter} from 'vue-router'
import {onMounted, ref} from "vue";

const router = useRouter();
const emit = defineEmits(['update-step-index', 'update-step-status'])

let submitButtonLoading = ref(false)
let submitNohupButtonLoading = ref(false)

function handleStepNextButtonClicked() {
  router.push({
    path: '/dashboard/config/vcs/finsh-step'
  });
}

onMounted(() => {
  emit('update-step-index',"4")
})
</script>

<style scoped>
.exec-step-view {
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