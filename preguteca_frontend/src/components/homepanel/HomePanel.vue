<script setup lang="ts">
import { useHomePage } from "../../queries/useHomePage";
import HomePanelHeader from "./HomePanelHeader.vue";
import HomePanelTextPostCard from "./HomePanelTextPostCard.vue";
import HomePanelVideoCard from "./HomePanelVideoCard.vue";

defineProps<{ showContent: boolean; onClick?: (evt: MouseEvent) => void }>();

const homePage = useHomePage();
</script>
<template>
  <div class="panel-container">
    <HomePanelHeader
      v-if="homePage.isSuccess && homePage.data.value"
      :home-page="homePage.data.value"
    />
    <div
      v-if="homePage.isSuccess && homePage.data.value && showContent"
      class="panel-content"
    >
      <HomePanelVideoCard
        v-for="videoPost in homePage.data.value?.videoPosts"
        :key="videoPost.id"
        :video-post="videoPost"
      />
      <HomePanelTextPostCard
        v-for="textPost in homePage.data.value?.textPosts"
        :key="textPost.id"
        :title="textPost.headerTitle"
        :content="textPost.content"
      />
    </div>
  </div>
</template>
<style scoped>
.panel-content {
  display: grid;
  position: relative;
  grid-area: aside;
  grid-template-columns: 1fr;
  padding: 8px;
  gap: 8px;
  overflow-y: scroll;
  width: 100%;
  height: 100%;
}

.panel-container {
  width: 100%;
  height: 100%;
  grid-area: aside;
  display: flex;
  overflow-y: scroll;
  flex-direction: column;
  border: solid 1px var(--border-color);
}

@media screen and (min-width: 1200px) {
  .panel-content {
    grid-template-columns: 1fr 1fr;
  }
}
</style>
