<script setup lang="ts">
import { reactive } from "vue";
import CategoryDetail from "./components/CategoryDetail.vue";
import { TCategory } from "./types";
import { useCategories } from "./queries/useCategories.ts";
import MainIllustration from "./components/MainIllustration.vue";

const globalState = reactive({
  activeCategory: {} as TCategory
})


const categoriesQ = reactive(useCategories())

function handleCategoryClick(category: TCategory) {
  globalState.activeCategory = category

}

function setActiveCategory(categoryName: string){
  const category = categoriesQ.data.find(category => category.name === categoryName)
  console.log(category)
  if(!category) return
  globalState.activeCategory = category
  const videoEntryList = document.querySelector("#video-entry-list") as HTMLElement
  console.log(videoEntryList)
  videoEntryList.scrollTo(0,0)

}

</script>

<template>
  <header id="page-header" class="border-thin">
    <h1 id="page-title">PREGUTECA</h1>
  </header>
  <div id="page-content" class="border-thin">
    <section id="main-scroll">
      <div id="scroll-illustration">

<MainIllustration :set-active-category="setActiveCategory"/>
      </div>
    </section>
    <CategoryDetail :active-category="globalState.activeCategory" />
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

#page-header {
  position: relative;
  top: 0;
  display: flex;
  flex-direction: row;
  align-items: center;
  padding-left: 16px;
  grid-area: header;
}

#page-title {
  font-size: 32px;
  font-weight: 500;
}

#page-content {
  position: relative;
  box-sizing: border-box;
  grid-area: content;
  display: grid;
  bottom: 0;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: minmax(0, 1fr);
  grid-template-areas: "main-scroll main-scroll aside aside aside";
}

#main-scroll {
  grid-area: main-scroll;
  overflow-y: scroll;
}

#scroll-illustration{
}


.border-thin {
  border: solid 1px var(--border-color)
}


h1 {
  font-family: "Space Grotesk", "Arial Black", sans-serif;
  font-size: 2.4rem;
  font-weight: 600;
}

h2 {
  font-family: "Space Grotesk", "Arial Black", sans-serif;
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
