<template>
  <div class="group-mgmt-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>权限控制</n-breadcrumb-item>
          <n-breadcrumb-item>组管理</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <div class="op-area">
      <n-select v-model:value="roleSelectOptionValue" :options="roleSelectOptions"
                placeholder="选择检索条件" style="width: 150px; margin-right: 5px"/>
      <n-input v-model:value="groupOrUsageSearchInputValue" type="text" placeholder="按照组名或者用途搜索,支持全文索引..."></n-input>
      <n-tooltip trigger="hover">
        <template #trigger>
          <n-button tertiary circle style="margin-left: 5px" secondary type="info" @click="searchButtonOnClick">
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
          <n-button tertiary circle style="margin-left: 5px" secondary type="error"
                    @click="handleBatchDeleteButtonClicked">
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
    <n-modal v-model:show="isShowModal" :segmented="false"
             :mask-closable="false" preset="card" title="添加群组"
             :on-after-leave="onAddModalAfterLeave"
             style="width: 45%; min-width: 600px">
      <div style="display: flex; width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%">
          <div style="font-size: 12pt; font-weight: bold;">名称</div>
          <n-input type="text" placeholder="必填,请输入名称" style="margin-bottom: 10px"/>
          <div style="font-size: 12pt; font-weight: bold;">用途</div>
          <n-input type="text" placeholder="请输入用途"/>
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onAddModalFailed" style="margin-right: 10px">取消</n-button>
          <n-button @click="onAddModalOk" type="primary">添加</n-button>
        </div>
      </div>
    </n-modal>
    <n-modal v-model:show="isShowModifyModal" :segmented="false"
             :mask-closable="false" preset="card" title="修改组"
             :on-after-leave="onAddModalAfterLeave"
             style="width: 45%; min-width: 600px">
      <div style="display: flex; width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%">
          <div style="font-size: 12pt; font-weight: bold;">用途</div>
          <n-input type="text" placeholder="请输入用途"/>
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onModifyModalFailed" style="margin-right: 10px">取消</n-button>
          <n-button @click="onModifyModalOk" type="primary">添加</n-button>
        </div>
      </div>
    </n-modal>
    <div style="width: 100%; min-height: 20px">&nbsp;</div>
  </div>
</template>

<script setup>
import {reactive, ref, defineComponent, h, getCurrentInstance, onMounted} from "vue";
import {NButton, NTag, useDialog, useMessage} from "naive-ui";
import {SearchOutlined, CloseOutlined, DeleteOutlined, PlusOutlined} from "@vicons/antd"
import TableOperationAreaButtonGroup from "@/components/TableOperationAreaButtonGroup.vue";

const {proxy} = getCurrentInstance()
const groupOrUsageSearchInputValue = ref("")

onMounted(() => {
  console.log("执行onMounted()...")
  console.log('import.env.MODE', import.meta.env.MODE)
  proxy.$axios.get("/api/group/", {}).then(r => {
    if (r.status === 200) {
      const content = r.data
      if (content["code"] === "10000") {
        const data = content["data"]
        let result = [];

        data.map((item) => {
          result.push({
            "key": item["name"],
            "name": item["name"],
            "create-time": item["ctime"],
            "usage": item["usage"]
          })
        });

        groups.value = result;
      } else {
      }
    } else {
      console.error(r.status)
    }
  }).catch(e => {
  })
})

function searchButtonOnClick() {
  let inputVal = groupOrUsageSearchInputValue.value
  proxy.$axios.get("/api/group/" + inputVal, {
  }).then(r => {
    if (r.status === 200) {
      const content = r.data
      console.log("搜索事件执行成功")
      if (content["code"] === "10000") {
        const data = content["data"]
        let result = [];
        console.log("data", data)

        data.map((item) => {
          result.push({
            "key": item["name"],
            "name": item["name"],
            "create-time": item["ctime"],
            "usage": item["usage"]
          })
        });

        console.log(result)

        groups.value = result;
      } else {
      }
    } else {
      console.error(r.status)
    }
  }).catch(e => {
  })
}

// let {proxy} = getCurrentInstance()
// onMounted(() => {
//   axios.get("/api/group/").then(r => {
//     console.log(r.data)
//   })
//   // proxy.$axios.get("/group", {}).then(r => {
//   //   console.log(r.data)
//   //
//   // }).catch(e => {
//   //
//   // })
// })

const dialog = useDialog();
const message = useMessage();


let isShowModifyModal = ref(false)

function onModifyModalFailed() {
  isShowModifyModal.value = false;
}

function onModifyModalOk() {
  isShowModifyModal.value = false;
}

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

function onAddModalFailed() {

}

function onAddModalOk() {

}

let roleSelectOptionValue = ref(null)
const roleSelectOptions = ref([
  {
    label: "全部",
    value: null
  },
  {
    label: "名称",
    value: "名称"
  },
  {
    label: "用途",
    value: "用途"
  }
])

let groups = ref([]);

// let groups = ref([
//   {
//     "key": "0",
//     "name": "运维一组",
//     "create-time": "2023/12/12 00:00:00",
//     "usage": "用于处理日常工作"
//   }
// ]);

const columns = [
  {
    type: "selection",
    fixed: "left"
  },
  {
    title: "名称",
    key: "name",
    fixed: "left",
    width: 250
  },
  {
    title: "创建时间",
    key: "create-time",
    width: 200
  },
  {
    title: "用途",
    key: "usage",
    resizable: true
  },
  {
    title: "操作",
    key: "op",
    render(row) {
      return h(
          TableOperationAreaButtonGroup,
          {
            isShowDetail: false,
            isShowModify: true,
            isShowDelete: true,
            onDetailButtonClicked: () => {
            },
            onModifyButtonClicked: () => {
              isShowModifyModal.value = true
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
.group-mgmt-view {
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