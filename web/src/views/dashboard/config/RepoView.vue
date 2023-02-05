<template>
  <div class="repo-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>配置</n-breadcrumb-item>
          <n-breadcrumb-item>存储库</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <div class="op-area">
      <n-input style="width: 700px; margin-right: 15px" v-model:value="repoName" type="text" placeholder="请输入名称"></n-input>
      <n-select style="width: 700px; margin-right: 15px" v-model:value="repoTypeSelectOptionValue" :options="repoTypeSelectOptions" placeholder="请选择类型"></n-select>
      <n-input style="margin-right: 15px" v-model:value="repoUsage" type="type" placeholder="请输入用途,支持全文检索.."></n-input>
      <n-tooltip trigger="hover">
        <template #trigger>
          <n-button tertiary circle style="margin-left: 5px" secondary type="info">
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
          <n-button tertiary circle style="margin-left: 5px" secondary type="primary">
            <template #icon>
              <n-icon>
                <PlusOutlined/>
              </n-icon>
            </template>
          </n-button>
        </template>
        <span>添加</span>
      </n-tooltip>
      <n-tooltip trigger="hover">
        <template #trigger>
          <n-button tertiary circle style="margin-left: 5px" secondary type="error">
            <template #icon>
              <n-icon>
                <DeleteOutlined/>
              </n-icon>
            </template>
          </n-button>
        </template>
        <span>删除选中条目</span>
      </n-tooltip>
      <n-tooltip trigger="hover">
        <template #trigger>
          <n-button tertiary circle style="margin-left: 5px" secondary type="error">
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
    <n-data-table :columns="columns" :data="repos" :pagination="paginationReactive" striped/>
    <div style="width: 100%; min-height: 20px">&nbsp;</div>
  </div>
</template>

<script setup>
import {h, reactive, ref} from "vue";
import {NButton, NTag} from "naive-ui";
import {SearchOutlined, CloseOutlined, DeleteOutlined, PlusOutlined} from "@vicons/antd"

let repoName = ref("")
let repoUsage = ref("")
let repoTypeSelectOptionValue = ref(null)
const repoTypeSelectOptions = [
  {
    label: "全部",
    value: null
  },
  {
    label: "SSH",
    value: "SSH"
  },
  {
    label: "HTTPS",
    value: "HTTPS"
  }
];

let repos = ref([
  {
    "key": "0",
    "name": "ss/sss",
    "content-type": "ssh",
    "location": "git@github.com:swxfll/CMDB.git",
    "create-time": "2012/12/12 00:00:00",
    "usage": "用于调试环境"
  }
]);

const columns = [
  {
    type: "selection",
    fixed: "left"
  },
  {
    title: "名称",
    key: "name",
    fixed: "left",
    width: 200
  },
  {
    title: "类型",
    key: "content-type",
    width: 100
  },
  {
    title: "地址",
    key: "location",
    width: 250
  },
  {
    title: "添加时间",
    key: "create-time",
    width: 220
  },
  {
    title: "用途",
    key: "usage",
    width: 220,
    resizable: true
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
]

function handleDeleteCurrentItemButtonClicked() {

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
.repo-view{
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