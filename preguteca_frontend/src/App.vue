<script setup lang="ts">
import { dimmElement, undimmElement } from "./utils";
import { computed, onMounted, reactive, ref, watch } from "vue";
import { store, updateActiveCategory, updateActivePanel } from "./store";

import AppHeader from "./components/AppHeader.vue";
import CategoryDetail from "./components/CategoryDetail.vue";
import MainIllustration from "./components/MainIllustration.vue";
import MenuPanel from "./components/MenuPanel.vue";
import HomePanel from "./components/homepanel/HomePanel.vue";
import { useCategories } from "./queries/useCategories";
import { useHomePage } from "./queries/useHomePage";
import HomePanelHeader from "./components/homepanel/HomePanelHeader.vue";

const sidePanelContainer = ref<HTMLElement | null>(null);

const screenWidth = ref(window.innerWidth);

const isMobile = computed(() => screenWidth.value <= 812);
const homePanelDetailsVisible = ref(false);

const categories = reactive(useCategories());
const homePage = useHomePage();

onMounted(() => {
  window.addEventListener(
    "resize",
    () => {
      screenWidth.value = window.innerWidth;
    },
    { passive: true }
  );
});

const toggleHomePanelDetails = () => {
  return (homePanelDetailsVisible.value = !homePanelDetailsVisible.value);
};

watch(
  () => categories.status,
  () => {
    if (!categories.isSuccess || !categories.data) return;
    const hashValue = window.location.hash.slice(1);
    const categoryFromHash = categories.data.find(
      (category) => category.name === hashValue
    );
    if (categoryFromHash) {
      updateActivePanel("category");
      updateActiveCategory(categoryFromHash);
    }
  }
);
</script>

<template>
  <AppHeader />
  <div id="page-content" class="border-thin">
    <section id="main-scroll" class="scrollable">
      <div
        v-if="store.activePanel === 'home' && isMobile"
        class="home-panel--mobile"
      >
        <HomePanelHeader
          v-if="homePage.isSuccess && homePage.data.value"
          :home-page="homePage.data.value"
        />
      </div>
      <div id="main-illustration">
        <MainIllustration />
      </div>
    </section>
    <div id="side-panel-container" ref="sidePanelContainer">
      <HomePanel
        v-if="store.activePanel === 'home'"
        class="home-panel--desktop"
        :show-content="true"
      />
      <CategoryDetail
        v-if="store.activePanel === 'category'"
        :active-category="store.activeCategory"
      />
      <MenuPanel
        v-if="store.activePanel === 'menu'"
        :menu-page="store.activeMenuPage"
      />
    </div>
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
  display: flex;
  flex-direction: column;
}

#main-illustration {
  position: relative;
}

#side-panel-container {
  grid-area: aside;
  height: 100%;
  overflow-y: hidden;
}

.home-panel--mobile {
  z-index: 5;
}

@media screen and (min-width: 812px) {
  .home-panel--mobile {
    display: none;
  }
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
