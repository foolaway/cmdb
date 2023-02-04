<template>
    <div class="exec-step-view">
      <n-card style="width: 100%; height: 100%;">
        <div style="width:100%; height:100%; display: flex; flex-direction: column;">
          <div class="step-form-content">
            <n-divider title-placement="left">通知到:</n-divider>
            <div style="margin-bottom: 25px">
              <div style="font-size: 15pt; margin-bottom: 15px">WebHook URL:</div>
              <n-input type="text" placeholder=""/>
            </div>
            <div style="margin-bottom: 25px">
              <div style="font-size: 15pt; margin-bottom: 15px">秘钥(如果存在):</div>
              <n-input style="width: 50%;" type="text" placeholder=""/>
            </div>
            <div style="margin-bottom: 25px">
              <n-divider title-placement="left">正在执行, 还剩:</n-divider>
              <div style="padding-left: 50px; display: flex; align-items: flex-end">
                <div style="font-size: 35pt">{{remain}}</div>
                <div style="font-size: 8pt; color: gray; padding-left: 5px">台</div>
              </div>
            </div>
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
let remain = ref(20)

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