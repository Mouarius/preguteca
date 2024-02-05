<script setup lang="ts">
import { ref } from "vue";
import ChevronLeft from "../assets/chevron-left.svg";
import { updateActivePanel } from "../store";
import { dimmElement, undimmElement } from "../utils.ts"
defineProps<{
  title?: string;
  subtitle?: string;
  titleClickHandler?: (e: Event) => void
}>()
const mainIllustrationContainer = ref<HTMLElement | null>(null)
function scrollTop(event: MouseEvent) {
  event.preventDefault();
  const panelContent = document.querySelector(".panel-content");
  panelContent?.scrollTo(0, 0);
}
</script>
<template>
  <div class="panel-container" @mouseover="() => { dimmElement(mainIllustrationContainer) }"
    @mouseleave="(_event: MouseEvent) => { undimmElement(mainIllustrationContainer) }">
    <div class="panel-header" @click="scrollTop">
      <img alt="chevron-left" :src="ChevronLeft" @click="() => updateActivePanel('home')" />
      <span class="panel-header__title">{{ title }}</span>
    </div>
    <div class="panel-content">
      <slot />
    </div>
  </div>
</template>
<style scoped>
.panel-container {
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
  transition: transform 0.4s ease-in;
}

.panel-container--hidden {
  transform: translateX(100vw)
}

.panel-header {
  background: var(--white);
  color: var(--black);
  display: flex;
  gap: 8px;
  padding: 8px;
  padding-left: 10px;
  padding-right: 12px;
}

.panel-header .panel-header__title {
  cursor: pointer;
  font-family: var(--font-title);
  font-size: 24px;
  font-weight: 600;
  height: 100%;
}

.panel-header img {
  cursor: pointer;
}

.panel-content {
  max-height: 100%;
  overflow: hidden;
}

@media (min-width: 768px) {
  .panel-container {
    position: relative;
    transform: translateX(0);
  }

  .panel-header {
    padding-left: 12px;
    justify-content: flex-start;
  }

  .panel-header img {
    display: none;
  }
}
</style>
