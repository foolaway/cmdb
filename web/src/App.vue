<script setup>
import {RouterLink, RouterView} from 'vue-router'
import {h, defineComponent, ref, onMounted} from "vue";
import {NIcon, darkTheme} from "naive-ui";
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
        label: renderRouteLink("/overview/permission", {}, "权限"),
        key: "permission-overview",
        icon: renderIcon(DesktopOutlined)
      },
      {
        label: renderRouteLink("/overview/machine", {}, "机器"),
        key: "machine-overview",
        icon: renderIcon(CloudServerOutlined)
      },
      {
        label: renderRouteLink("/overview/concept", {}, "业务概念"),
        key: "concept-overview",
        icon: renderIcon(PaperClipOutlined)
      },
      {
        label: renderRouteLink("/overview/repo-config", {}, "存储库与配置"),
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
        label: renderRouteLink("/permission-control/group-mgmt", {}, "组管理"),
        key: "group-mgmt",
        icon: renderIcon(UsergroupAddOutlined)
      },
      {
        label: renderRouteLink("/permission-control/member-mgmt", {}, "成员"),
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
        label: renderRouteLink("/biz-concept/machine", {}, "机器"),
        key: "machine",
        icon: renderIcon(CloudServerOutlined)
      },
      {
        label: renderRouteLink("/biz-concept/group", {}, "群组"),
        key: "group",
        icon: renderIcon(GroupOutlined)
      },
      {
        label: renderRouteLink("/biz-concept/safe-group", {}, "安全组"),
        key: "safe-group",
        icon: renderIcon(SafetyOutlined)
      },
      {
        label: renderRouteLink("/biz-concept/res-pool", {}, "资源池"),
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
        label: renderRouteLink("/config/repo", {}, "存储"),
        key: "repo",
        icon: renderIcon(GithubFilled)
      },
      {
        label: renderRouteLink("/config/vcs", {}, "版本控制"),
        key: "vcs",
        icon: renderIcon(FileSyncOutlined)
      }
    ]
  },
  {
    label: renderRouteLink("/audit", {}, "审计"),
    key: "audit",
    icon: renderIcon(AuditOutlined)
  },
  {
    label: renderRouteLink("/about", {}, "关于"),
    key: "about",
    icon: renderIcon(InfoCircleOutlined)
  }
];

// 左侧菜单栏被收起或展开调用
function autoChangeRightContentWidth(collapsed) {
  document.getElementById("right-content").style.width = (collapsed ? window.innerWidth - 64 : window.innerWidth - 240) + "px";
}

function handleMenuClicked(key, item) {
  console.log(key, item)
}

// 用户的系统,使用的是否是深色模式
let systemDarkModeMedia = window.matchMedia("(prefers-color-theme: dark)");
let useDarkTheme = ref(systemDarkModeMedia.matches)

// 当挂载时
onMounted(() => {
  document.getElementById("left-menu").style.height = window.innerHeight + "px";
  document.getElementById("right-content").style.width = window.innerWidth - 240 + "px";
  window.onresize = () => {
    document.getElementById("left-menu").style.height = window.innerHeight + "px";
    autoChangeRightContentWidth()
  }

  let systemThemCallback = (e) => {
    let prefersDarkMode = e.matches;
    useDarkTheme.value = !!prefersDarkMode;
  };

  if (typeof systemDarkModeMedia.addEventListener === 'function'){
    systemDarkModeMedia.addEventListener('change', systemThemCallback)
  } else if (typeof systemDarkModeMedia.addListener === 'function'){
    systemDarkModeMedia.addListener(systemThemCallback);
  }

  // 强制使用深色模式
   useDarkTheme.value = true
})
</script>

<template>
  <div class="app-view">
    <n-config-provider :theme="useDarkTheme ? darkTheme: null">
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
          <n-layout-content id="right-content" content-style="padding: 24px">
            <router-view></router-view>
          </n-layout-content>
        </n-layout>
      </n-space>
    </n-config-provider>

  </div>
</template>

<style scoped>
.app-view {
  width: 100%;
  height: 100%;
  display: flex;
}
</style>
