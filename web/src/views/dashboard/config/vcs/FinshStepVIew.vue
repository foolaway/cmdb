<template>
  <div class="finsh-step-view">
    <n-card style="width: 100%; height: 100%;">
      <div style="width:100%; height:100%; display: flex; flex-direction: column;">
        <div class="step-form-content">
          <n-statistic label="你一共处理了" tabular-nums>
            <n-number-animation ref="numberAnimationInstRef" :from="0" :to="12039"/>
            <template #suffix>
              台机器
            </template>
          </n-statistic>
          <n-statistic label="其中有" tabular-nums>
            <n-number-animation ref="numberAnimationInstRef" :from="0" :to="12030"/>
            <template #suffix>
              完成了变更任务
            </template>
          </n-statistic>
          <n-statistic label="但是有" tabular-nums>
            <n-number-animation ref="numberAnimationInstRef" :from="0" :to="9"/>
            <template #suffix>
              操作失败了
            </template>
          </n-statistic>
          <n-divider title-placement="left">详细的错误信息如下:</n-divider>
          <div>
            <n-log :loading="LogAreaLoading" :log="logContent"></n-log>
          </div>
        </div>
        <div class="step-op-area">

          <n-button strong type="warning" @click="handleCopyToClipBoardButtonClicked" id="log-content"
                    style="margin-right: 10px">拷&nbsp;贝&nbsp;到&nbsp;剪&nbsp;切&nbsp;板
          </n-button>
          <n-button strong type="primary" @click="handleStepNextButtonClicked">好</n-button>
        </div>
      </div>
    </n-card>
  </div>
</template>

<script setup>
import {useRouter} from 'vue-router'
import {onMounted, ref} from "vue";
import {useMessage} from 'naive-ui';

const router = useRouter();
const message = useMessage()
const emit = defineEmits(['update-step-index', 'update-step-status'])

let LogAreaLoading = ref(true)
const logContent = ref("Feb  3 10:51:11 h1 rsyslogd: [origin software=\"rsyslogd\" swVersion=\"7.4.7\" x-pid=\"1116\" x-info=\"http://www.rsyslog.com\"] start\n" +
    "Feb  3 10:51:01 h1 kernel: Linux version 4.10.4-1.el7.elrepo.x86_64 (mockbuild@Build64R7) (gcc version 4.8.5 20150623 (Red Hat 4.8.5-11) (GCC) ) #1 SMP Sat Mar 18 12:50:10 EDT 2017\n" +
    "Feb  3 10:51:01 h1 kernel: Command line: BOOT_IMAGE=/vmlinuz-4.10.4-1.el7.elrepo.x86_64 root=UUID=3437f1a0-f850-4f1b-8a7c-819c5f6a29e4 ro crashkernel=auto consoleblank=0 vga=0x305\n" +
    "Feb  3 10:51:01 h1 kernel: x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'\n" +
    "Feb  3 10:51:01 h1 kernel: x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'\n" +
    "Feb  3 10:51:01 h1 kernel: x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'\n" +
    "Feb  3 10:51:01 h1 kernel: x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256\n" +
    "Feb  3 10:51:01 h1 kernel: x86/fpu: Enabled xstate features 0x7, context size is 832 bytes, using 'standard' format.\n" +
    "Feb  3 10:51:01 h1 kernel: e820: BIOS-provided physical RAM map:\n" +
    "Feb  3 10:51:01 h1 kernel: BIOS-e820: [mem 0x0000000000000000-0x000000000009fbff] usable\n" +
    "Feb  3 10:51:01 h1 kernel: BIOS-e820: [mem 0x000000000009fc00-0x000000000009ffff] reserved\n" +
    "Feb  3 10:51:01 h1 kernel: BIOS-e820: [mem 0x00000000000f0000-0x00000000000fffff] reserved\n" +
    "Feb  3 10:51:01 h1 kernel: BIOS-e820: [mem 0x0000000000100000-0x00000000211ddfff] usable\n" +
    "Feb  3 10:51:01 h1 kernel: BIOS-e820: [mem 0x00000000211de000-0x00000000211fffff] reserved\n" +
    "Feb  3 10:51:01 h1 kernel: BIOS-e820: [mem 0x00000000feffc000-0x00000000feffffff] reserved\n" +
    "Feb  3 10:51:01 h1 kernel: BIOS-e820: [mem 0x00000000fffc0000-0x00000000ffffffff] reserved\n" +
    "Feb  3 10:51:01 h1 kernel: NX (Execute Disable) protection: active\n" +
    "Feb  3 10:51:01 h1 kernel: SMBIOS 2.8 present.\n" +
    "Feb  3 10:51:01 h1 kernel: DMI: Red Hat KVM, BIOS 1.11.0-2.el7 04/01/2014\n" +
    "Feb  3 10:51:01 h1 kernel: Hypervisor detected: KVM\n" +
    "Feb  3 10:51:01 h1 kernel: e820: last_pfn = 0x211de max_arch_pfn = 0x400000000\n" +
    "Feb  3 10:51:01 h1 kernel: x86/PAT: PAT not supported by CPU.\n" +
    "Feb  3 10:51:01 h1 kernel: x86/PAT: Configuration [0-7]: WB  WT  UC- UC  WB  WT  UC- UC\n" +
    "Feb  3 10:51:01 h1 kernel: found SMP MP-table at [mem 0x000f6380-0x000f638f] mapped at [ffff8800000f6380]\n" +
    "Feb  3 10:51:01 h1 kernel: Using GB pages for direct mapping\n" +
    "Feb  3 10:51:01 h1 kernel: RAMDISK: [mem 0x1f8a7000-0x20a0cfff]\n" +
    "Feb  3 10:51:01 h1 kernel: ACPI: Early table checksum verification disabled\n" +
    "Feb  3 10:51:01 h1 kernel: ACPI: RSDP 0x00000000000F6160 000014 (v00 BOCHS )\n" +
    "Feb  3 10:51:01 h1 kernel: ACPI: RSDT 0x00000000211E237B 00002C (v01 BOCHS  BXPCRSDT 00000001 BXPC 00000001)\n" +
    "Feb  3 10:51:01 h1 kernel: ACPI: FACP 0x00000000211E228F 000074 (v01 BOCHS  BXPCFACP 00000001 BXPC 00000001)\n" +
    "Feb  3 10:51:01 h1 kernel: ACPI: DSDT 0x00000000211E0040 00224F (v01 BOCHS  BXPCDSDT 00000001 BXPC 00000001)\n" +
    "Feb  3 10:51:01 h1 kernel: ACPI: FACS 0x00000000211E0000 000040\n" +
    "Feb  3 10:51:01 h1 kernel: ACPI: APIC 0x00000000211E2303 000078 (v01 BOCHS  BXPCAPIC 00000001 BXPC 00000001)\n" +
    "Feb  3 10:51:01 h1 kernel: No NUMA configuration found\n" +
    "Feb  3 10:51:01 h1 kernel: Faking a node at [mem 0x0000000000000000-0x00000000211ddfff]\n" +
    "Feb  3 10:51:01 h1 kernel: NODE_DATA(0) allocated [mem 0x211bc000-0x211ddfff]\n" +
    "Feb  3 10:51:01 h1 kernel: kexec_core: crashkernel: memory value expected\n" +
    "Feb  3 10:51:01 h1 kernel: kvm-clock: Using msrs 4b564d01 and 4b564d00\n" +
    "Feb  3 10:51:01 h1 kernel: kvm-clock: cpu 0, msr 0:2113c001, primary cpu clock\n" +
    "Feb  3 10:51:01 h1 kernel: kvm-clock: using sched offset of 9766985086 cycles\n" +
    "Feb  3 10:51:01 h1 kernel: clocksource: kvm-clock: mask: 0xffffffffffffffff max_cycles: 0x1cd42e4dffb, max_idle_ns: 881590591483 ns\n" +
    "Feb  3 10:51:01 h1 kernel: Zone ranges:\n" +
    "Feb  3 10:51:01 h1 kernel:  DMA      [mem 0x0000000000001000-0x0000000000ffffff]\n" +
    "Feb  3 10:51:01 h1 kernel:  DMA32    [mem 0x0000000001000000-0x00000000211ddfff]\n" +
    "Feb  3 10:51:01 h1 kernel:  Normal   empty\n" +
    "Feb  3 10:51:01 h1 kernel: Movable zone start for each node\n" +
    "Feb  3 10:51:01 h1 kernel: Early memory node ranges\n")

function handleStepNextButtonClicked() {
  router.push({
    path: '/dashboard/config/vcs/repo-step'
  });
}

function handleCopyToClipBoardButtonClicked() {
  //log-content
  const clipboardObj = navigator.clipboard;
  if (clipboardObj !== undefined) {
    // 浏览器支持 clipboard API
    clipboardObj.writeText(logContent.value).then(() => {
      message.success(
          "内容已拷贝到剪切板"
      )
    }).catch(() => {
      message.warning('内容拷贝到剪切板失败')
    })
  } else {
    // 回退到传统方式
    document.getElementById("log-content")
  }

}

onMounted(() => {
  emit('update-step-index', "5")
})
</script>

<style scoped>
.finsh-step-view {
  width: 100%;
  height: 100%;
  padding-top: 20px;
}

.step-form-content {
  flex: 1;
}

.step-op-area {
  display: flex;
  justify-content: flex-end;
}
</style>