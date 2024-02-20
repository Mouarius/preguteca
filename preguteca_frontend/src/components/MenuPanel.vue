<script setup lang="ts">
import { MenuPage } from "../types";
import MainPanel from "./MainPanel.vue";

const props = defineProps<{
  menuPage: MenuPage | null;
  onBackButtonClick?: (e: MouseEvent) => void;
}>();

const handleBackButtonClick = (evt: MouseEvent) => {
  props.onBackButtonClick?.call(null, evt);
};
</script>
<template>
  <MainPanel
    :title="menuPage?.title"
    :on-back-button-click="handleBackButtonClick"
  >
    <div class="text-content">
      <span v-dompurify-html="menuPage?.content"></span>
    </div>
  </MainPanel>
</template>
<style scoped>
.text-content {
  padding: 8px;
  height: 100%;
  overflow: scroll;
}
</style>
