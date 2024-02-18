<script setup lang="ts">
import { MenuPage } from "../types";
import MainPanel from "./MainPanel.vue";

type MenuPanelProps = {
  menuPage: MenuPage | null;
};

defineProps<MenuPanelProps>();
</script>
<template>
  <MainPanel :title="menuPage?.title">
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
