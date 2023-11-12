<script setup lang="ts">
import HomePanelCard from './homepanel-card/HomePanelCard.vue';

type Props = {
  title: string;
  content: string;
};

defineProps<Props>();
</script>
<template>
  <HomePanelCard header-title="title">
      <div class="row details__content">
        {{ content }}
      </div>
  </HomePanelCard>
</template>
