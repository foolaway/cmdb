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
      <n-input style="width: 700px; margin-right: 15px" v-model:value="groupName" type="text"
               placeholder="请输入名称"></n-input>
      <n-select style="width: 360px; margin-right: 15px" v-model:value="groupLevelSelectOptionValue"
                :options="groupLevelSelectOptions" placeholder="请选择层级"/>
      <n-input style="width: 700px; margin-right: 15px" v-model:value="parentGroup" type="text"
               placeholder="请输入所属群组"></n-input>
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
    <n-data-table :columns="columns" :data="groups" :pagination="paginationReactive" striped/>
    <n-modal v-model:show="isShowAddModal" :segmented="false"
             :mask-closable="false" preset="card" title="添加群组(服务)"

             :on-after-leave="onAddModalAfterLeave"
             style="width: 45%; min-width: 600px">
      <div style="display: flex; width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%">
          <div style="font-size: 12pt; font-weight: bold;">名称</div>
          <n-input type="text" placeholder="必填,请输入名称" style="margin-bottom: 10px;" />
          <div style="font-size: 12pt; font-weight: bold;">层级</div>
          <n-select  placeholder="必填,请选择层级" style="margin-bottom: 10px" />
          <div style="font-size: 12pt; font-weight: bold;">所属群组</div>
          <n-select  placeholder="必填,请选择所属群组" style="margin-bottom: 10px" />
          <div style="font-size: 12pt; font-weight: bold;">业务需求</div>
          <n-input type="text" placeholder="必填,请输入业务需求" style="margin-bottom: 10px;" />
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onAddModalFailed" style="margin-right: 10px">取消</n-button>
          <n-button @click="onAddModalOk" type="primary">添加</n-button>
        </div>
      </div>
    </n-modal>
    <n-modal v-model:show="isShowModifyModal" :segmented="false"
             :mask-closable="false" preset="card" title="修改群组(服务)"
             :on-after-leave="onModifyModalAfterLeave"
             style="width: 45%; min-width: 600px">
      <div style="display: flex; width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%">
          <div style="font-size: 12pt; font-weight: bold;">姓名</div>
          <n-input type="text" placeholder="必填,请输入姓名" style="margin-bottom: 10px;" />
          <div style="font-size: 12pt; font-weight: bold;">层级</div>
          <n-select  placeholder="必填,请选择层级" style="margin-bottom: 10px" />
          <div style="font-size: 12pt; font-weight: bold;">所属群组</div>
          <n-select  placeholder="必填,请选择所属群组" style="margin-bottom: 10px" />
          <div style="font-size: 12pt; font-weight: bold;">业务需求</div>
          <n-input type="text" placeholder="必填,请输入业务需求" style="margin-bottom: 10px;" />
          <div style="font-size: 12pt; font-weight: bold;">安全组</div>
          <n-input type="textarea" rows="10" placeholder="选填, 请输入安全组名称, 使用英文半角小写逗号分割" style="margin-bottom: 10px;" />
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
import {h, reactive, ref} from "vue";
import {NButton, NTag, useDialog, useMessage} from "naive-ui";
import {SearchOutlined, CloseOutlined, DeleteOutlined, PlusOutlined} from "@vicons/antd"
import TableOperationAreaButtonGroup from "@/components/TableOperationAreaButtonGroup.vue";

const message = useMessage();
const dialog = useDialog();

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

let isShowAddModal = ref(false);
let isShowModifyModal = ref(false);

function onModifyModalAfterLeave() {
}

function handleAddButtonClicked() {
  isShowAddModal.value = true
}

function onAddModalAfterLeave() {

}

function onAddModalFailed(){
  isShowAddModal.value = false;
}

function onAddModalOk() {
  isShowAddModal.value = false;
}

function onModifyModalFailed() {
  isShowModifyModal.value = false;
}

function onModifyModalOk(){
  isShowModifyModal.value = false;
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
    // M 表示当前群组下的机器所用的安全组
    // G 表示当前群组下面次级群组所用的安全组
    // 只能修改当前群组下面机器的安全组,会影响当前层级群组下面全部机器的安全组
    // 若要修改指定机器的安全组配置,那么可以通过搜索指定的机器进行修改,在机器页面
    "safe-groups-list": ["M:Web 服务", "M:数据库服务", "G:网关服务", "G:登录服务"],
    "level": "1",
    "parent": "1",
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
    title: "安全组汇总",
    key: "safe-groups-list",
    resizable: true,
    render(row) {
      return row["safe-groups-list"].map((tagKey) => {
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
            onDetailButtonClicked: () => {

            },
            onModifyButtonClicked: () => {
              isShowModifyModal.value = true;
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