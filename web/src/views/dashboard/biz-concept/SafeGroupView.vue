<template>
  <div class="safe-group-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>业务概念</n-breadcrumb-item>
          <n-breadcrumb-item>安全组</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <div class="op-area">
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
    <n-data-table :columns="columns" :data="safeGroups" :pagination="paginationReactive" striped/>
    <div style="width: 100%; min-height: 20px">&nbsp;</div>
  </div>
</template>

<script setup>
import {h, reactive, ref} from "vue";
import {NButton, NTag} from "naive-ui";
import {SearchOutlined, CloseOutlined} from "@vicons/antd"

let safeGroups = ref([
  {
    "key": "0",
    "name": "常规",
    "ports": ["IN:TCP:80", "IN:TCP:443", "OUT:TCP:443", "ALL:TCP:22"],
    "create-time": "2023/12/12 00:00:00",
    "usage": "常规的静态 WEB 服务 和 远程管理端口"
  }
]);

const columns = [
  {
    type: "selection",
    fiex: "left"
  },
  {
    title: "名称",
    key: "name",
    fixed: "left",
    width: 250
  },
  {
    title: "放行端口列表",
    key: "ports",
    render(row) {
      return row["ports"].map((tagKey) => {
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
    title: "创建时间",
    key: "create-time"
  },
  {
    title: "业务需求",
    key: "usage"
  },
  {
    title: "操作",
    key: "op",
    render(row) {
      return h(
          NButton,
          {
            size: "tiny",
            onClick: () => handleDeleteCurrentItemButtonClicked(row),
          },
          {default: () => "删除"}
      );
    },
    fixed: "right",
    width: 150
  }
];

function handleDeleteCurrentItemButtonClicked(row) {

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
</script>

<style scoped>
.safe-group-view{
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