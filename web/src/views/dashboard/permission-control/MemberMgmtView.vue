<template>
  <div class="member-mgmt-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>权限控制</n-breadcrumb-item>
          <n-breadcrumb-item>成员</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <div class="op-area">
      <n-input style="width: 700px; margin-right: 15px" v-model:value="memberName" type="text" placeholder="请输入姓名"></n-input>
      <n-input style="width: 700px; margin-right: 15px" v-model:value="memberNo" type="text" placeholder="请输入工号"></n-input>
      <n-input style="width: 700px; margin-right: 15px" v-model:value="memberGroup" type="text" placeholder="请输入组"></n-input>
      <n-input style="width: 700px; margin-right: 15px" v-model:value="memberPhone" type="text" placeholder="请输入手机号码"></n-input>
      <n-input style="width: 700px; margin-right: 15px" v-model:value="memberEmail" type="text" placeholder="请输入工作邮箱"></n-input>
      <n-select style="width: 700px; margin-right: 15px" v-model:value="memberSexSelectOptionValue" :options="memberSexSelectOptions" placeholder="请选择性别"></n-select>
      <n-input style="margin-right: 15px" v-model:value="memberArch" type="text" placeholder="请输入组织架,支持全文检索.."></n-input>
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
          <n-button tertiary circle style="margin-left: 5px" secondary type="error" >
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
    <n-data-table :columns="columns" :data="members" :pagination="paginationReactive" striped/>
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

let memberName = ref("")
let memberNo = ref("")
let memberGroup = ref("")
let memberPhone = ref("")
let memberEmail = ref("")
let memberSexSelectOptionValue = ref(null)
let memberArch = ref("")

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

const memberSexSelectOptions = [
  {
    label: "全部",
    value: null
  },
  {
    label: "男",
    value: "男"
  },
  {
    label: "女",
    value: "女"
  }
];

let members = ref([
  {
    "key": "0",
    "name": "小张",
    "no": "z33333333333",
    "group": "运维一组",
    "arch-group": "xxxxx/xxx/xxx",
    "phone": "13333333333",
    "email": "zs@zs.com",
    "sex": "男",
    "create-time": "2022:02:02 00:00:00",
    "update-time": "2022:02:02 00:00:00"
  }
]);

const columns = [
  {
    type: "selection",
    fixed: "left"
  },
  {
    title: "姓名",
    key: "name",
    fixed: "left",
    width: 100
  },
  {
    title: "工号",
    key: "no",
    fixed: "left",
    width: 150
  },
  {
    title: "组",
    key: "group",
    width: 200,
    fixed: "left",
  },
  {
    title: "手机",
    key: "phone",
    width: 150
  },
  {
    title: "邮箱",
    key: "email",
    width: 230
  },
  {
    title: "性别",
    key: "sex",
    width: 100
  },
  {
    title: "组织架构",
    key: "arch-group",
    width: 150,
    resizable: true
  },
  {
    title: "创建时间",
    key: "create-time",
    width: 200
  },
  {
    title: "最后一次修改时间",
    key: "update-time",
    width: 200
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
.member-mgmt-view{
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