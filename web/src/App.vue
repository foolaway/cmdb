<script setup>
import {RouterLink, RouterView} from 'vue-router'
import {h, defineComponent, ref, onMounted} from "vue";
import {NIcon} from "naive-ui";
import {
  BarChartOutlined,
  DesktopOutlined,
  ControlOutlined,
  UserOutlined,
  UsergroupAddOutlined,
  PaperClipOutlined,
  CloudServerOutlined,
  GroupOutlined,
  SafetyOutlined,
  BoxPlotOutlined,
  FileOutlined,
  GithubFilled,
  FileSyncOutlined,
  AuditOutlined
} from "@vicons/antd";

function renderIcon(icon) {
  return () => h(NIcon, null, {default: () => h(icon)});
}

const menuOptions = [
  {
    label: "概览",
    key: "overview",
    icon: renderIcon(BarChartOutlined),
    children: [
      {
        label: "权限",
        key: "permission-overview",
        icon: renderIcon(DesktopOutlined)
      },
      {
        label: "机器",
        key: "machine-overview",
        icon: renderIcon(CloudServerOutlined)
      },
      {
        label: "业务概念",
        key: "concept-overview",
        icon: renderIcon(PaperClipOutlined)
      },
      {
        label: "存储库与配置",
        key: "repo-config-overview",
        icon: renderIcon(CloudServerOutlined)
      }
    ]
  },
  {
    label: "权限控制",
    key: "permission-control",
    icon: renderIcon(ControlOutlined),
    children: [
      {
        label: "组管理",
        key: "group-mgmt",
        icon: renderIcon(UsergroupAddOutlined)
      },
      {
        label: "成员管理",
        key: "member-mgmt",
        icon: renderIcon(UserOutlined)
      }
    ]
  },
  {
    label: "业务概念",
    key: "biz-concept",
    icon: renderIcon(PaperClipOutlined),
    children: [
      {
        label: "机器",
        key: "machine",
        icon: renderIcon(CloudServerOutlined)
      },
      {
        label: "群组",
        key: "group",
        icon: renderIcon(GroupOutlined)
      },
      {
        label: "安全组",
        key: "safe-group",
        icon: renderIcon(SafetyOutlined)
      },
      {
        label: "资源池",
        key: "res-pool",
        icon: renderIcon(BoxPlotOutlined)
      }
    ]
  },
  {
    label: "配置",
    key: "config",
    icon: renderIcon(FileOutlined),
    children: [
      {
        label: "存储库",
        key: "repo",
        icon: renderIcon(GithubFilled)
      },
      {
        label: "版本控制",
        key: "vcs",
        icon: renderIcon(FileSyncOutlined)
      }
    ]
  },
  {
    label: "审计",
    key: "audit",
    icon: renderIcon(AuditOutlined)
  }
];

// 左侧菜单栏被收起或展开调用
function autoChangeRightContentWidth(collapsed) {
  document.getElementById("right-content").style.width = (collapsed ? window.innerWidth - 64 : window.innerWidth - 240) + "px";
}

function handleMenuClicked(key, item) {
  console.log(key, item)
}

// 当挂载时
onMounted(() => {
  document.getElementById("left-menu").style.height = window.innerHeight + "px";
  document.getElementById("right-content").style.width = window.innerWidth - 240 + "px";
  window.onresize = () => {
    document.getElementById("left-menu").style.height = window.innerHeight + "px";
    autoChangeRightContentWidth()
  }
})


</script>

<template>
  <div class="app-view">
    <n-space vertical>
      <n-layout has-sider>
        <n-layout-sider
            id="left-menu"
            bordered
            show-trigger
            collapse-mode="width"
            :collapsed-width="64"
            :width="240"
            :native-scrollbar="false"
            :inverted="inverted"
            @on-update:collapsed="autoChangeRightContentWidth"
        >
          <n-menu
              :inverted="inverted"
              :collapsed-width="64"
              :collapsed-icon-size="22"
              :options="menuOptions"
              @update:value="handleMenuClicked"
          />
        </n-layout-sider>
        <n-layout-content id="right-content" content-style="padding: 24px;background-color: red">
          <router-view></router-view>
        </n-layout-content>
      </n-layout>
    </n-space>
  </div>
</template>

<style scoped>
.app-view {
  width: 100%;
  height: 100%;
  display: flex;
}
</style>
