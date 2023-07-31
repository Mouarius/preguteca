<script setup lang="ts">
import VideoEntry from "./VideoEntry.vue";
import { TCategory } from "../types";
import ChevronLeft from "../assets/chevron-left.svg";

interface CategoryDetailProps {
  activeCategory: TCategory;
  toggleCategoryDetails: () => void;
}

function scrollTop(event: MouseEvent) {
  event.preventDefault();
  const videoEntryListEl = document.querySelector(".video-entry-list");
  videoEntryListEl?.scrollTo(0, 0);
}

defineProps<CategoryDetailProps>();
</script>

<template>
  <section class="category-container category-container--hidden">
    <header v-if="activeCategory.fullName" @click="scrollTop" class="category-container__header">
      <img @click="toggleCategoryDetails" :src="ChevronLeft" alt="chevron-left" />
      <h2>{{ activeCategory.fullName }}</h2>
    </header>
    <ul v-if="activeCategory.fullName" id="video-entry-list" class="video-entry-list scrollable">
      <VideoEntry v-for="(video_entry, index) in activeCategory.videoEntries" :key="video_entry.id"
        :video-entry="video_entry" :videos-in-category="activeCategory.videoEntries.length" :index-in-category="index" />
    </ul>
    <div v-else class="category-placeholder">
      <div class="category-placeholder__welcome">
        <h3>Bienvenue sur Preguteca.com</h3>
        <p>Ce site regroupe des vidéos sur des sujets de société, des vidéos qui m'ont amenés à me questionner, et que
          j'ai voulu consigner dans ce site web. Pour commencer cliquez sur un batiment pour découvrir les vidéos.</p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.category-placeholder {
  display: flex;
  height: 100%;
  width: 100%;
  align-items: center;
  justify-content: center;
}

.category-placeholder__welcome {
  width: 80%;
  max-width: 480px;
}

.category-placeholder__welcome h3 {
  margin-bottom: 16px;
}

.category-container__header {
  padding-left: 10px;
  padding-right: 12px;
  background: var(--white);
  height: 42px;
  width: 100%;
  color: var(--black);
  display: flex;
  justify-content: flex-start;
  align-items: center;
  justify-content: space-between;
}

.category-container__header img {
  cursor: pointer;
}

.category-container {
  background-color: var(--black);
  grid-area: aside;
  border-left: solid 1px var(--border-color);
  position: absolute;
  display: flex;
  flex-direction: column;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  transform: translateX(0);
  transition: all 0.4s ease-in;
}

.category-container--hidden {
  transform: translateX(100vw);
}

@media (min-width: 768px) {
  .category-container {
    transform: translateX(0);
    display: flex;
    position: relative;
    flex-direction: column;
  }

  .category-container__header {
    padding-left: 12px;
    justify-content: flex-start;
  }

  .category-container__header img {
    display: none;
  }
}

#video-entry-list {
  padding: 8px;
  scroll-behavior: smooth;
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
