<script setup lang="ts">
import VideoEntry from "./VideoEntry.vue";
import { TCategory } from "../types";

interface CategoryDetailProps {
  activeCategory: TCategory;
}

defineProps<CategoryDetailProps>();
</script>

<template>
  <section id="category-container">
    <header>
      <h2>{{ activeCategory.fullName }}</h2>
    </header>
    <ul id="video-entry-list">
      <VideoEntry
        v-for="(video_entry, index) in activeCategory.videoEntries"
        :key="video_entry.id"
        :video-entry="video_entry"
        :videos-in-category="activeCategory.videoEntries.length"
        :index-in-category="index"
      />
    </ul>
  </section>
</template>

<style scoped>
#category-container {
  grid-area: aside;
  border-left: solid 1px var(--border-color);
  position: relative;
  display: flex;
  flex-direction: column;
}

#category-container > header {
  background: var(--white);
  padding-left: 16px;
  height: 42px;
  width: 100%;
  color: var(--text);
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

#video-entry-list {
  padding: 8px;
  display: flex;
  flex-direction: column;
  align-self: stretch;
  align-items: center;
  justify-content: flex-start;
  width: 100%;
  height: 100%;
  position: relative;
  overflow: scroll;
}
</style>
