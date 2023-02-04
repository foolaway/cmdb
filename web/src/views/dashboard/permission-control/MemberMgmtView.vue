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
    <n-data-table :columns="columns" :data="members" :pagination="paginationReactive" striped/>
    <div style="width: 100%; min-height: 20px">&nbsp;</div>
  </div>
</template>

<script setup>
import {h, reactive, ref} from "vue";
import {NButton, NTag} from "naive-ui";
import {SearchOutlined, CloseOutlined} from "@vicons/antd"

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