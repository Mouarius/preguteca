<script setup lang="ts">
import HomePanelCardHeader from "./HomePanelCardHeader.vue";
import HomePanelCardFooter from "./HomePanelCardFooter.vue";

type Props = {
  headerTitle: string;
  headerSupplementaryInformation?: string | null;
  footerLeftName?: string | null;
  footerLeftValue?: string | null;
  footerRightName?: string | null;
  footerRightValue?: string | null;
};

defineProps<Props>();
</script>
<template>
  <div class="card-container">
    <HomePanelCardHeader
      :title="headerTitle"
      :supplementary-information="headerSupplementaryInformation"
    />
    <slot />
    <HomePanelCardFooter
      :left-name="footerLeftName"
      :left-value="footerLeftValue"
      :right-name="footerRightName"
      :right-value="footerRightValue"
    />
  </div>
</template>
<style>
.card-container {
  box-shadow: 4px 4px var(--orange);
  border: solid 1px var(--border-color);
  display: flex;
  flex-direction: column;
  min-width: 100%;
}

.card-container > div:not(:last-child) {
  border-bottom: solid 1px var(--border-color);
}

.row {
  padding: 0 8px;
  display: flex;
  align-items: center;
  height: 32px;
  min-height: 32px;
}
</style>
