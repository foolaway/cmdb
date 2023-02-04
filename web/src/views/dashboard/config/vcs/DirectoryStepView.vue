<template>
  <div class="div-step-view">
    <n-card style="width: 100%; height: 100%;">
      <div style="width:100%; height:100%; display: flex; flex-direction: column;">
        <div class="step-form-content">
          <div style="margin-bottom: 25px">
            <div style="font-size: 15pt; margin-bottom: 15px">同步到:</div>
            <n-input type="text"
                     placeholder="请输入一个目录,如果指定目录在目标机器或者群组上不存在,则会自动创建该目录."/>
          </div>
          <div style="margin-bottom: 25px">
            <div style="font-size: 15pt; margin-bottom: 15px">同步后执行脚本: </div>
            <div style="font-size: 8pt; margin-bottom: 5px; color: gray">这将在每个机器(或者群组中的机器)同步完后执行下面的脚本</div>
            <n-input v-model:value="postSyncScriptContent" type="textarea" rows="10"/>
          </div>
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
import {onMounted, ref} from "vue";

const router = useRouter();
const emit = defineEmits(['update-step-index', 'update-step-status'])
let postSyncScriptContent = ref("#/bin/bash")

function handleStepNextButtonClicked() {
  router.push({
    path: '/dashboard/config/vcs/target-step'
  });
}

onMounted(() => {
  emit('update-step-index', "2")
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