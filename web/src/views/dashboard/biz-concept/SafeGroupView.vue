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
      <n-input style="width: 500px; margin-right: 15px" v-model:value="safeGroupName" type="text" placeholder="请输入名称"></n-input>
      <n-input v-model:value="safeGroupBizDemand" type="text" placeholder="请输入业务需求,支持全文检索.."></n-input>
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
          <n-button tertiary circle style="margin-left: 5px" secondary type="primary" @click="handleAddButtonClicked">
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
          <n-button tertiary circle style="margin-left: 5px" secondary type="error" @click="handleBatchDeleteButtonClicked">
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
    <n-data-table :columns="columns" :data="safeGroups" :pagination="paginationReactive" striped/>
    <n-modal v-model:show="isShowModal" :segmented="false"
             :mask-closable="false" preset="card" title="添加群组"
             :on-after-leave="onAddModalAfterLeave"
             style="width: 45%; min-width: 600px">
      <div style="display: flex; width: 100%; height: 100%; flex-direction: column">
        <div style="width: 1000px">
          Model Content
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onAddModalFailed" style="margin-right: 10px">取消</n-button>
          <n-button @click="onAddModalOk" type="primary">添加</n-button>
        </div>
      </div>
    </n-modal>
    <div style="width: 100%; min-height: 20px">&nbsp;</div>
  </div>
</template>

<script setup>
import {h, reactive, ref} from "vue";
import {NButton, NTag, useDialog, useMessage} from "naive-ui";
import {SearchOutlined, CloseOutlined, DeleteOutlined, PlusOutlined} from "@vicons/antd"
import TableOperationAreaButtonGroup from "@/components/TableOperationAreaButtonGroup.vue";

const dialog = useDialog();
const message = useMessage();

function handleBatchDeleteButtonClicked() {
  dialog.warning({
    title: "批量删除",
    content: "即将删除 24 个条目, 是否继续?",
    positiveText: "确定",
    negativeText: "取消",
    onPositiveClick: () => {
      message.success("删除成功")
    },
  })
}

let isShowModal = ref(false)

function handleAddButtonClicked() {
  isShowModal.value = true
}

function onAddModalAfterLeave() {

}

function onAddModalFailed(){

}

function onAddModalOk() {

}

let safeGroupName = ref("")
let safeGroupBizDemand = ref("")

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
          TableOperationAreaButtonGroup,
          {
            isShowDetail: true,
            isShowModify: true,
            isShowDelete: true,
            onDetailButtonClicked: () =>{

            },
            onModifyButtonClicked: () => {

            },
            onDeleteButtonClicked: () => {

            }
          }
      );
    },
    fixed: "right",
    width: 150
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