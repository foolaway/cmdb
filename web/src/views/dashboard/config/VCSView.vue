<template>
  <div class="vcs-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>配置</n-breadcrumb-item>
          <n-breadcrumb-item>版本控制</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <n-card>
      <n-steps :current="(currentStepIndex)" :status="currentStepStatus">
        <n-step
            title="选择配置存储库"
            description="选择一个 Git 存储, 并设置分支与提交版本"
        />
        <n-step
            title="下发目录"
            description="设置一个指定的配置目录,来存放远程的配置数据"
        />
        <n-step
            title="机器或者群组"
            description="更新任意数量的机器或者群组的配置数据并提交执行"
        />
        <n-step
            title="执行"
            description="在这里提交任务,设置 WebHook 通知,看执行进度,甚至可以置入后台并开始新的同步任务"
        />
        <n-step
            title="完成"
            description="结果页"
        />
      </n-steps>
    </n-card>
    <router-view @update-step-index="setCurrentStepIndex" @update-step-status="setCurrentStepStatus" style="width: 100%; height: 100%;"></router-view>
    <div style="width: 100%; min-height: 20px">&nbsp;</div>
  </div>
</template>

<script setup>
import {ref} from "vue";

let currentStepIndex = ref(1)
let currentStepStatus = ref("process") //'process' | 'finish' | 'error' | 'wait'

function setCurrentStepIndex(index) {
  currentStepIndex.value = index;
}

function setCurrentStepStatus(status) {
  currentStepStatus.value = status;
}


</script>

<style scoped>
.vcs-view{
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}
</style>