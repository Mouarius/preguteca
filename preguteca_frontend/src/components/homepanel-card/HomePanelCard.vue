<script setup lang="ts">
import type { HomepagePost } from "../../types/"
import HomePanelCardHeader from "./HomePanelCardHeader.vue";
import HomePanelCardContent from "./HomePanelCardContent.vue"
import HomePanelCardFooter from "./HomePanelCardFooter.vue";

type Props = {
  post: HomepagePost;
};

defineProps<Props>();
</script>
<template>
  <div class="card-container">
    <HomePanelCardHeader :title="post.headerTitle" :supplementary-information="post.headerSupplementaryInformation"
      :is-video-post="post.video !== null" />
    <HomePanelCardContent :content="post.content" :video="post.video" />
    <HomePanelCardFooter :left-name="post.footerLeftName" :left-value="post.footerLeftValue"
      :right-name="post.footerRightName" :right-value="post.footerRightValue" />
  </div>
</template>
<style>
.card-container {
  box-shadow: 4px 4px var(--orange);
  border: solid 1px var(--border-color);
  display: inline-flex;
  flex-direction: column;
  margin: 4px 0px;
  width: 100%;
}

.card-container>div:not(:last-child) {
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
