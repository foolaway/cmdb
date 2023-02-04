<template>
  <div class="machine-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>业务概念</n-breadcrumb-item>
          <n-breadcrumb-item>机器</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <div class="op-area">
      <n-input size="small" type="text" placeholder="按照 ID 搜索, 与其他条件互斥"
               style="width: 250px; margin-right: 5px"/>
      <n-input size="small" type="text" placeholder="按照群组搜索, 支持全文索引"
               style="width: 250px; margin-right: 5px"/>
      <n-input size="small" type="text" placeholder="按照资源池搜索, 支持全文索引"
               style="width: 250px; margin-right: 5px"/>
      <n-select v-model:value="machineTypeSearchOptionValue" :options="machineTypeSearchOptions"
                placeholder="选择机器类型" style="width: 200px; margin-right: 5px"/>
      <n-select v-model:value="machineStatusSearchOptionValue" :options="machineStatusSearchOptions"
                placeholder="选择机器状态" style="width: 200px"/>
      <n-tooltip trigger="hover">
        <template #trigger>
          <n-button tertiary circle style="margin-left: 5px">
            <template #icon>
              <n-icon>
                <SearchOutlined/>
              </n-icon>
            </template>
          </n-button>
        </template>
        <!--        <span>开启、关闭或者挂起机器</span>-->
        <span>按照指定条件进行搜索</span>
      </n-tooltip>
      <n-tooltip trigger="hover">
        <template #trigger>
          <n-button tertiary circle style="margin-left: 5px">
            <template #icon>
              <n-icon>
                <CloseOutlined/>
              </n-icon>
            </template>
          </n-button>
        </template>
        <span>清空搜索条件</span>
      </n-tooltip>
    </div>
    <n-data-table :columns="columns" :data="machines" :pagination="paginationReactive" striped/>
    <div style="width: 100%; min-height: 20px">&nbsp;</div>
  </div>
</template>

<script setup>
import {h, reactive, ref} from "vue";
import {NButton, NTag} from "naive-ui";
import {SearchOutlined, CloseOutlined} from "@vicons/antd"

let machineTypeSearchOptionValue = ref(null);
let machineTypeSearchOptions = [
  {
    label: "全部",
    value: null
  },
  {
    label: "物理机",
    value: "物理机"
  },
  {
    label: "虚拟机",
    value: "虚拟机"
  },
  {
    label: "容器",
    value: "容器"
  }
]

let machineStatusSearchOptionValue = ref(null)
let machineStatusSearchOptions = [
  {
    label: "全部",
    value: null
  },
  {
    label: "已关机",
    value: "已关机",
  },
  {
    label: "正在运行",
    value: "正在运行"
  },
  {
    label: "已挂起",
    value: "已挂起"
  },
  {
    label: "正在挂起",
    value: "正在挂起"
  },
  {
    label: "正在关闭",
    value: "正在关闭"
  },
  {
    label: "就绪中",
    value: "就绪中"
  }
]

function handleMachineItemPowerClicked(row) {
  console.log(row)
}

const paginationReactive = reactive({
  page: 2,
  pageSize: 5,
  showSizePicker: true,
  pageSizes: [3, 5, 7],
  onChange: (page) => {
    paginationReactive.page = page;
  },
  onUpdatePageSize: (pageSize) => {
    paginationReactive.pageSize = pageSize;
    paginationReactive.page = 1;
  }
});

let machines = ref([
  {
    "key": "1",
    "id": "7a259f7a-1a32-4ca2-a273-9e0d1ac1293c",
    "type": "物理机",
    "status": "正在运行",
    "group": "/动物园执行/全球",
    "safe-group": ["web服务", "数据库服务", "登录网关服务", "运维"],
    "res-pool": "北京东三区",
    "create-time": "2023/02/15 00:12:09",
    "update-time": "2023/02/15 00:12:09",

  },
  {
    "key": "1",
    "id": "7a259f7a-1a32-4ca2-a273-9e0d1ac1293c",
    "type": "物理机",
    "status": "正在运行",
    "group": "/动物园执行/全球",
    "safe-group": ["web服务", "数据库服务", "登录网关服务", "运维"],
    "res-pool": "北京东三区",
    "create-time": "2023/02/15 00:12:09",
    "update-time": "2023/02/15 00:12:09",

  },
  {
    "key": "1",
    "id": "7a259f7a-1a32-4ca2-a273-9e0d1ac1293c",
    "type": "物理机",
    "status": "正在运行",
    "group": "/动物园执行/全球",
    "safe-group": ["web服务", "数据库服务", "登录网关服务", "运维"],
    "res-pool": "北京东三区",
    "create-time": "2023/02/15 00:12:09",
    "update-time": "2023/02/15 00:12:09",

  },
  {
    "key": "1",
    "id": "7a259f7a-1a32-4ca2-a273-9e0d1ac1293c",
    "type": "物理机",
    "status": "正在运行",
    "group": "/动物园执行/全球",
    "safe-group": ["web服务", "数据库服务", "登录网关服务", "运维"],
    "res-pool": "北京东三区",
    "create-time": "2023/02/15 00:12:09",
    "update-time": "2023/02/15 00:12:09",

  },
  {
    "key": "1",
    "id": "7a259f7a-1a32-4ca2-a273-9e0d1ac1293c",
    "type": "物理机",
    "status": "正在运行",
    "group": "/动物园执行/全球",
    "safe-group": ["web服务", "数据库服务", "登录网关服务", "运维"],
    "res-pool": "北京东三区",
    "create-time": "2023/02/15 00:12:09",
    "update-time": "2023/02/15 00:12:09",

  }

])
const columns = [
  {
    title: "ID",
    key: "id",
    width: 320,
    fixed: "left"
  },
  {
    title: "类型",
    key: "type",
    width: 80,
    fixed: "left"
  },
  {
    title: "群组",
    key: "group",
    width: 150,
    fixed: "left"
  },
  {
    title: "资源池",
    key: "res-pool",
    width: 150,
    fixed: "left"
  },
  {
    title: "安全组",
    key: "safe-group",
    render(row) {
      return row["safe-group"].map((tagKey) => {
        return h(
            NTag,
            {
              style: {
                marginRight: "6px",
                marginTop: "2px"
              },
              type: "info",
              bordered: false,
              size: "small"
            },
            {
              default: () => tagKey
            }
        );
      });
    },
    resizable: true
  },
  {
    title: "受控时间",
    key: "create-time",
    width: 220
  },
  {
    title: "数据上报时间",
    key: "update-time",
    width: 220
  },
  {
    title: "状态",
    key: "status",
    width: 100,
  },
  {
    title: "操作",
    key: "op",
    render(row) {
      return h(
          NButton,
          {
            size: "tiny",
            onClick: () => handleMachineItemPowerClicked(row),
          },
          {default: () => "电源"}
      );
    },
    fixed: "right",
    width: 150
  }
];
</script>

<style scoped>
.machine-view {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.op-area {
  padding-bottom: 15px;
  display: flex;
}
</style>