<script setup lang="ts">
import HomePanelCard from '../homepanel-card/HomePanelCard.vue';


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
<style scoped>
.details {
  padding: 8px;
}

.text-content {
  font-style: normal;
}
</style>
