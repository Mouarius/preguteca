<script setup lang="ts">
import CategoryDetail from "./components/CategoryDetail.vue";
import MainIllustration from "./components/MainIllustration.vue";
import AppHeader from "./components/AppHeader.vue";
import { store } from "./store";
import HomePanel from "./components/HomePanel.vue";
import MenuPanel from "./components/MenuPanel.vue";
import { dimmElement, undimmElement } from "./utils";
import { ref } from "vue";

const sidePanelContainer = ref<HTMLElement | null>(null)
const mainIllustrationContainer = ref<HTMLElement | null>(null)


function translateScrollContent(amount: number) {
  if (!mainIllustrationContainer.value || window.innerWidth > 812) return
  mainIllustrationContainer.value.style.transform = `translateY(${amount}px)`

}

</script>

<template>
  <AppHeader />
  <div id="page-content" class="border-thin">
    <section id="main-scroll" class="scrollable">
      <div id="main-illustration" ref="mainIllustrationContainer" @mouseover="() => { dimmElement(sidePanelContainer) }"
        @mouseleave="() => {
          undimmElement(sidePanelContainer)
        }">
        <MainIllustration />
      </div>
    </section>
    <HomePanel v-if="store.activePanel == 'home'" v-on:height-changed="(height) => translateScrollContent(height)" />
    <CategoryDetail v-if="store.activePanel == 'category'" :active-category="store.activeCategory" />
    <MenuPanel v-if="store.activePanel == 'menu'" :menu-page="store.activeMenuPage" />

  </div>
</template>

<style>
#app {
  height: 100vh;
  width: 100vw;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  padding: 8px;
  display: grid;
  grid-template-columns: 1fr;
  column-gap: 8px;
  row-gap: 8px;
  grid-template-rows: 52px minmax(0, 1fr);
  grid-template-areas: "header" "content";
  overflow: hidden;
}

#page-content {
  position: relative;
  box-sizing: border-box;
  grid-area: content;
  display: grid;
  bottom: 0;
  grid-template-columns: 1fr;
  grid-template-rows: minmax(0, 1fr);
  grid-template-areas: "main-scroll";
}

@media (min-width: 812px) {
  #page-content {
    grid-template-columns: repeat(5, 1fr);
    grid-template-rows: minmax(0, 1fr);
    grid-template-areas: "main-scroll main-scroll aside aside aside";
  }
}

#main-scroll {
  grid-area: main-scroll;
  overflow-y: scroll;
  position: relative;
  height: 100%;
}


.sr-only {
  border: 0 !important;
  clip: rect(1px, 1px, 1px, 1px) !important;
  -webkit-clip-path: inset(50%) !important;
  clip-path: inset(50%) !important;
  height: 1px !important;
  overflow: hidden !important;
  padding: 0 !important;
  position: absolute !important;
  width: 1px !important;
  white-space: nowrap !important;
}

.border-thin {
  border: solid 1px var(--border-color);
}

h1 {
  font-family: var(--font-title);
  font-size: 2.4rem;
  font-weight: 600;
}

h2 {
  font-family: var(--font-title);
  font-size: 24px;
  font-weight: 600;
}

h3 {
  font-size: 1.4rem;
  font-weight: 600;
}

li {
  list-style-type: none;
}

.container {
  display: block;
  position: relative;
  width: 100%;
}
</style>
