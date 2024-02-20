<script setup lang="ts">
import ChevronLeft from "../assets/chevron-left.svg";
const props = defineProps<{
  title?: string;
  subtitle?: string;
  onTitleClick?: (e: Event) => void;
  onBackButtonClick?: (e: MouseEvent) => void;
}>();

function scrollTop(event: MouseEvent) {
  event.preventDefault();
  const panelContent = document.querySelector(".panel-content");
  panelContent?.scrollTo(0, 0);
}

const handleBackButtonClick = (evt: MouseEvent) => {
  props.onBackButtonClick?.call(null, evt)
}

</script>
<template>
  <div class="panel-container">
    <div class="panel-header" @click="scrollTop">
      <img alt="chevron-left" :src="ChevronLeft" @click="handleBackButtonClick" />
      <span class="panel-header__title">{{ title }}</span>
    </div>
    <div class="panel-content">
      <slot />
    </div>
  </div>
</template>
<style scoped>
.panel-container {
  position: relative;
  height: 100%;
  background-color: var(--black);
  border-left: solid 1px var(--border-color);
  display: flex;
  flex-direction: column;
  transition: transform 0.4s ease-in;
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
  .panel-header {
    padding-left: 12px;
    justify-content: flex-start;
  }

  .panel-header img {
    display: none;
  }
}
</style>
