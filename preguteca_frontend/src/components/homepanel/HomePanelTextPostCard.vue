<script setup lang="ts">
import HomePanelCard from "../homepanel-card/HomePanelCard.vue";

type Props = {
  title: string;
  content: string;
};

defineProps<Props>();
</script>
<template>
  <HomePanelCard :header-title="title">
    <div class="details">
      <div class="text-content">
        <span v-dompurify-html="content"></span>
      </div>
    </div>
  </HomePanelCard>
</template>
<style>
.details {
  padding: 8px;
}

.text-content {
  font-style: normal;
  font-size: 14px;
  line-height: 1.5;
}

.text-content span a {
  color: var(--text);
  font-weight: 600;
  word-break: break-all !important;
}
</style>
