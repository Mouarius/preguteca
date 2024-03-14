<script setup lang="ts">
import { reactive } from "vue";
import { useHomePage } from "../../queries/useHomePage";
import { TCategory } from "../../types";
import HomePanelHeader from "./HomePanelHeader.vue";
import HomePanelCard from "../homepanel-card/HomePanelCard.vue";

defineProps<{
  onBackButtonClick: (e: MouseEvent) => void;
  setActiveCategory: (category: TCategory) => void;
}>();

const homePage = reactive(useHomePage());
</script>
<template>
  <div class="panel-container">
    <HomePanelHeader
      v-if="homePage.isSuccess && homePage.data"
      :home-page="homePage.data"
      :set-active-category="setActiveCategory"
      :on-back-button-click="onBackButtonClick"
    />
    <div v-if="homePage.isSuccess && homePage.data.posts" class="panel-content">
      <HomePanelCard
        v-for="post in homePage.data.posts"
        :key="post.id"
        :post="post"
      />
    </div>
  </div>
</template>
<style scoped>
.panel-content {
  display: grid;
  grid-template-columns: 1fr;
  gap: 8px;
  min-width: 0px;
  position: relative;
  grid-area: aside;
  padding: 8px;
}
.panel-content * {
  height: fit-content;
  min-width: 0px;
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
