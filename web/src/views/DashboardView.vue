<script setup>
import {RouterLink, RouterView, useRouter} from 'vue-router'
import {h, onMounted} from "vue";
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
  AuditOutlined,
  InfoCircleOutlined
} from "@vicons/antd";

const router = useRouter();

function renderIcon(icon) {
  return () => h(NIcon, null, {default: () => h(icon)});
}

function renderRouteLink(path, params, label) {
  return () =>
      h(
          RouterLink,
          {
            to: {
              path: path,
              params: params
            }
          },
          {default: () => label}
      )
}

const menuOptions = [
  {
    label: "概览",
    key: "overview",
    icon: renderIcon(BarChartOutlined),
    children: [
      {
        label: renderRouteLink("/dashboard/overview/permission", {}, "权限"),
        key: "permission-overview",
        icon: renderIcon(DesktopOutlined)
      },
      {
        label: renderRouteLink("/dashboard/overview/machine", {}, "机器"),
        key: "machine-overview",
        icon: renderIcon(CloudServerOutlined)
      },
      {
        label: renderRouteLink("/dashboard/overview/concept", {}, "业务概念"),
        key: "concept-overview",
        icon: renderIcon(PaperClipOutlined)
      },
      {
        label: renderRouteLink("/dashboard/overview/repo-config", {}, "存储库与配置"),
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
        label: renderRouteLink("/dashboard/permission-control/group-mgmt", {}, "组管理"),
        key: "group-mgmt",
        icon: renderIcon(UsergroupAddOutlined)
      },
      {
        label: renderRouteLink("/dashboard/permission-control/member-mgmt", {}, "成员"),
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
        label: renderRouteLink("/dashboard/biz-concept/machine", {}, "机器"),
        key: "machine",
        icon: renderIcon(CloudServerOutlined)
      },
      {
        label: renderRouteLink("/dashboard/biz-concept/group", {}, "群组"),
        key: "group",
        icon: renderIcon(GroupOutlined)
      },
      {
        label: renderRouteLink("/dashboard/biz-concept/safe-group", {}, "安全组"),
        key: "safe-group",
        icon: renderIcon(SafetyOutlined)
      },
      {
        label: renderRouteLink("/dashboard/biz-concept/res-pool", {}, "资源池"),
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
        label: renderRouteLink("/dashboard/config/repo", {}, "存储"),
        key: "repo",
        icon: renderIcon(GithubFilled)
      },
      {
        label: renderRouteLink("/dashboard/config/vcs", {}, "版本控制"),
        key: "vcs",
        icon: renderIcon(FileSyncOutlined)
      }
    ]
  },
  {
    label: renderRouteLink("/dashboard/audit", {}, "审计"),
    key: "audit",
    icon: renderIcon(AuditOutlined)
  },
  {
    label: renderRouteLink("/dashboard/about-me", {}, "关于我"),
    key: "about",
    icon: renderIcon(InfoCircleOutlined)
  }
];

// 左侧菜单栏被收起或展开调用
function autoChangeRightContentWidth(collapsed) {
  document.getElementById("right-content").style.width = (collapsed ? window.innerWidth - 64 : window.innerWidth - 240) + "px";
  document.getElementById("logout-button").style.width = (collapsed ? "45px" : "220px")
  document.getElementById("logout-button").innerText = (collapsed ? "X" : "退 出 登 录")
  document.getElementById("logout-button").style.transition = (collapsed ? "width 0.2s" : "width 0.4s");

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

function handleLogoutButtonClicked() {
  router.push({
    path: "/login"
  })
}
</script>

<template>
  <div class="dashboard-view">
    <n-button @click="handleLogoutButtonClicked" id="logout-button" strong secondary
              style="width: 220px; position: absolute; bottom: 10px; left: 10px; z-index: 999">退&nbsp;出&nbsp;登&nbsp;录
    </n-button>
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
          :on-update:collapsed="autoChangeRightContentWidth"
      >
        <n-menu
            :inverted="inverted"
            :collapsed-width="64"
            :collapsed-icon-size="22"
            :options="menuOptions"
            @update:value="handleMenuClicked"
        />
      </n-layout-sider>
      <n-layout-content id="right-content" content-style="padding: 20px">
        <router-view></router-view>
      </n-layout-content>
    </n-layout>
  </div>
</template>

<style scoped>
.dashboard-view {
  width: 100%;
  height: 100%;
  display: flex;
}
</style>
