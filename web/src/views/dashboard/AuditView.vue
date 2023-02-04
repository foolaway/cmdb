<template>
  <div class="audit-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>审计</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <div class="op-area">
      <n-select style="width: 250px; margin-right: 10px" v-model:value="levelSearchOptionValue" :options="levelSearchOptions" placeholder="选择等级"></n-select>
      <n-select style="width: 250px; margin-right: 10px" v-model:value="resultSearchOptionValue" :options="resultSearchOptions" placeholder="选择执行结果"></n-select>
      <n-input style="width: 250px; margin-right: 10px" placeholder="请输入成员ID" type="text"></n-input>
      <n-input style="width: 250px; margin-right: 10px" placeholder="请输入成员姓名" type="text"></n-input>
      <n-input placeholder="请输入事件,支持全文搜索.." type="text"></n-input>
      <n-tooltip trigger="hover">
        <template #trigger>
          <n-button type="info" secondary tertiary circle style="margin-left: 5px">
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
          <n-button type="error" secondary tertiary circle style="margin-left: 5px">
            <template #icon>
              <n-icon>
                <CloseOutlined/>
              </n-icon>
            </template>
          </n-button>
        </template>
        <span>清空搜索条件</span>
      </n-tooltip>
      <n-tooltip trigger="hover">
        <template #trigger>
          <n-button type="success" secondary tertiary circle style="margin-left: 5px">
            <template #icon>
              <n-icon>
                <DownloadOutlined/>
              </n-icon>
            </template>
          </n-button>
        </template>
        <span>下载当前表格的内容</span>
      </n-tooltip>
    </div>
    <n-data-table :columns="columns" :data="items" :pagination="paginationReactive" striped/>
    <div style="width: 100%; min-height: 20px">&nbsp;</div>
  </div>
</template>

<script setup>
import {h, reactive, ref} from "vue";
import {NButton, NTag} from "naive-ui";
import {SearchOutlined, CloseOutlined, DownloadOutlined} from "@vicons/antd"

let levelSearchOptionValue = ref(null)
const levelSearchOptions = ref([
  {
    label: "全部",
    value: "全部"
  },
  {
    label: "成功",
    value: "成功"
  },
  {
    label: "失败",
    value: "失败"
  }
])

let resultSearchOptionValue = ref(null)
const resultSearchOptions = ref([
  {
    label: "全部",
    value: "全部"
  },
  {
    label: "写入",
    value: "写入"
  },
  {
    label: "读取",
    value: "读取"
  }
])

let items = ref([
  {
    "key": "0",
    "level": "写入",
    "uid": "Z3333333",
    "name": "张三",
    "result": "完成",
    "create-time": "2023/08/19 12:00:00",
    "event": "在 /权限控制/成员 中, 添加了小华 Z 121231341"
  },
  {
    "key": "0",
    "level": "写入",
    "uid": "Z3333333",
    "name": "张三",
    "result": "完成",
    "create-time": "2023/08/19 12:00:00",
    "event": "在 /权限控制/成员 中, 添加了小华 Z 121231341"
  }
]);

const columns = [
  {
    type: "selection",
    fiex: "left"
  },
  {
    title: "等级",
    key: "level"
  },
  {
    title: "成员ID",
    key: "uid"
  },
  {
    title: "成员名字",
    key: "name"
  },
  {
    title: "执行结果",
    key: "result"
  },
  {
    title: "时间点",
    key: "create-time"
  },
  {
    title: "事件",
    key: "event"
  }

];

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
.audit-view {
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