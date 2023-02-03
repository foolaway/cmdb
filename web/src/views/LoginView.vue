<template>
  <n-layout class="login-view">
    <div
        style=" height: 100%; width: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; ">
      <div class="title">登录 CMDB</div>
      <div class="box">
        <n-input placeholder="请输入用户名">
          <template #prefix>
            <n-icon :component="UserOutlined"/>
          </template>
        </n-input>
      </div>
      <div class="box">
        <n-input type="password" show-password-on="mousedown" placeholder="密码" :maxlength="8">
          <template #prefix>
            <n-icon :component="LockOutlined"/>
          </template>
        </n-input>
      </div>
      <div class="help-box">
        <div class="about-text" @click="handleAboutLinkedClicked">关于 CMDB</div>
        <div class="forget-password">忘记密码？ 点击找回</div>
      </div>
      <div class="box">
        <n-tooltip placement="bottom" trigger="hover">
          <template #trigger>
            <n-button @click="handleLoginButtonClicked" strong secondary type="primary" style="width: 100%"
                      :loading="loginButtonLoadingStatus">进&nbsp;入&nbsp;系&nbsp;统
            </n-button>
          </template>
          输入用户名和密码后，点击进入 CMDB
        </n-tooltip>

      </div>
      <div></div>
    </div>
  </n-layout>
</template>

<script setup>
import {onMounted, ref} from 'vue'
import {useRouter} from 'vue-router'
import {UserOutlined, LockOutlined} from '@vicons/antd'

const router = useRouter();

let username = ref("")
let password = ref("")
let loginButtonLoadingStatus = ref(false)

onMounted(() => {
  document.title = "登录 CMDB"
})

function handleLoginButtonClicked() {
  router.push({
    path: "/dashboard"
  })
}

function handleAboutLinkedClicked() {
  router.push({
    path: "/about"
  })
}
</script>

<style scoped>
.login-view {
  width: 100%;
  height: 100%;
}

.title {
  font-size: 20px;
  text-align: center;
  margin-bottom: 10px;
}

.box {
  width: 350px;
  margin-top: 10px;
}

.help-box {
  width: 350px;
  margin-top: 15px;
  display: flex;
  justify-content: space-between;
}

.forget-password {
  margin-top: 10px;
  text-align: right;
  font-size: 8pt;
}

.about-text {
  margin-top: 10px;
  text-align: right;
  font-size: 8pt;
}

.forget-password:hover, .about-text:hover {
  text-decoration-line: underline;
  cursor: pointer;
}
</style>