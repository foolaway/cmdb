<template>
  <div class="group-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>业务概念</n-breadcrumb-item>
          <n-breadcrumb-item>群组</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <div class="op-area">
      <n-input style="width: 700px; margin-right: 15px" v-model:value="groupName" type="text" placeholder="请输入名称"></n-input>
      <n-select style="width: 360px; margin-right: 15px" v-model:value="groupLevelSelectOptionValue" :options="groupLevelSelectOptions" placeholder="请选择层级" />
      <n-input style="width: 700px; margin-right: 15px" v-model:value="parentGroup" type="text" placeholder="请输入所属群组"></n-input>
      <n-input v-model:value="bizDemand" type="text" placeholder="请输入业务需求,支持全文检索"></n-input>
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
    <n-data-table :columns="columns" :data="groups" :pagination="paginationReactive" striped/>
    <n-modal v-model:show="isShowModal">
      <n-card
          style="width: 600px"
          title="模态框"
          :bordered="false"
          size="huge"
          role="dialog"
          aria-modal="true"
      >

      </n-card>
    </n-modal>
    <div style="width: 100%; min-height: 20px">&nbsp;</div>
  </div>
</template>

<script setup>
import {h, reactive, ref} from "vue";
import {NButton, useDialog, useMessage} from "naive-ui";
import {SearchOutlined, CloseOutlined, DeleteOutlined, PlusOutlined} from "@vicons/antd"

const message = useMessage();
const dialog = useDialog();
let isShowModal = ref(false)

function handleAddButtonClicked (){
  isShowModal.value = true
}


let groupName = ref("");
let parentGroup = ref("")
let bizDemand = ref("")

let groupLevelSelectOptionValue = ref(null);
const groupLevelSelectOptions = [
  {
    label: "全部",
    value: null
  },
  {
    label: "第一层",
    value: "第一层"
  },
  {
    label: "第二层",
    value: "第二层"
  },
  {
    label: "第三层",
    value: "第三层"
  }
];



let groups = ref([
  {
    "key": "0",
    "name": "运维一组",
    "create-time": "2023/12/12 00:00:00",
    "usage": "用于处理日常工作"
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
    width: 150
  },
  {
    title: "层级",
    key: "level",
    fixed: "left",
    width: 80
  },
  {
    title: "所属群组",
    key: "parent",
    width: 250
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
.group-view {
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