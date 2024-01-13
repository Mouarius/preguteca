<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useHomePage } from "../queries/useHomePage.ts";
import { updateActiveCategory, updateActivePanel } from "../store";
import HomePanelTextPostCard from "./HomePanelTextPostCard.vue";
import HomePanelVideoCard from "./HomePanelVideoCard.vue";
import { TCategory } from "../types";
const homePage = useHomePage();

const emits = defineEmits<
  { (e: "heightChanged", height: number): void }
>();

const oldHeight = ref(0)

const panelContainer = ref<HTMLElement | null>(null)
onMounted(() => {
  window.addEventListener("resize", () => {
    if (panelContainer.value?.offsetHeight) {
      if (panelContainer.value.offsetHeight === oldHeight.value) return;
      oldHeight.value = panelContainer.value.offsetHeight
      emits("heightChanged", panelContainer.value.offsetHeight)
    }
  })
})

function navigateToCategory(category: TCategory | undefined) {
  if (!category) return;
  updateActivePanel("category")
  updateActiveCategory(category)

}
</script>
<template>
  <div class="panel-container" ref="panelContainer">
    <div class="panel-header">
      <div class="panel-header__section hearder__part--building">
        <div class="panel-header__title" @click="() => navigateToCategory(homePage.data.value?.monthCategory)
          ">
          {{ homePage.data.value?.monthCategory.fullName }}
        </div>
        <div class="separator separator--header"></div>
        <div class="header__subtitle">Edificio del mes</div>
      </div>
      <div class="panel-header__section hearder__part--question">
        <div class="header__keywords">
          {{ homePage.data.value?.monthCategory.keywords }}
        </div>
        <div class="separator separator--header"></div>
        <div class="header__subtitle">Palabras clave</div>
      </div>
    </div>
    <div class="panel-subheader">
      <div class="panel-subheader__section subheader__section--left">
        <p class="panel-subheader__general-questions">
          {{ homePage.data.value?.monthQuestions }}
        </p>
      </div>
      <div class="panel-subheader__section subheader__section--right">
        <div class="question-of-the-day">
          {{ homePage.data.value?.dayQuestion }}
        </div>
        <div class="separator separator--subheader"></div>
        <div class="panel-subheader__subtitle">Question del dia</div>
      </div>
    </div>
    <div class="panel-content" v-if="homePage.isSuccess">
      <HomePanelVideoCard v-for="videoPost in homePage.data.value?.videoPosts" v-bind:key="videoPost.id"
        :video-post="videoPost" />
      <HomePanelTextPostCard v-for="textPost in homePage.data.value?.textPosts" v-bind:key="textPost.id"
        :title="textPost.headerTitle" :content="textPost.content" />
    </div>
  </div>
</template>
<style scoped>
.panel-content {
  display: none;
}


.hearder__part--question {
  font-style: normal;
}

.panel-container {
  width: 100%;
  grid-area: aside;
  height: fit-content;
  display: flex;
  flex-direction: column;
  font-style: italic;
  border: solid 1px var(--border-color);
  overflow: scroll;
}

.panel-header {
  padding: 8px;
  padding-left: 10px;
  padding-right: 12px;
  background: var(--white);
  color: var(--black);
  display: grid;
  height: min-content;
  gap: 16px;
  grid-template-columns: 1fr;
}

.panel-header__section {
  display: flex;
  align-items: end;
  height: 100%;
}

.separator {
  width: 0px;
  height: 100%;
  margin-left: 10px;
  margin-right: 10px;
  border: solid 1px black;
  transform: skewX(-15deg);
}

.separator--header {
  border: solid 1px black;
}

.separator--subheader {
  border: solid 1px var(--border-color);
}

.panel-header__title {
  font-size: 24px;
  cursor: pointer;
  font-weight: 600;
  height: 100%;
}

.header__subtitle,
.panel-subheader__subtitle {
  font-size: 14px;
}

.panel-subheader__subtitle {
  color: var(--border-color);
  place-self: end;
}

.panel-subheader {
  color: var(--border-color);
  background-color: var(--black);
  display: flex;
  flex-direction: column;
  align-items: start;
  border-bottom: solid 1px var(--border-color);
}

.panel-subheader__section {
  display: flex;
  padding: 8px;
  height: 100%;
}

.question-of-the-day {
  font-weight: 600;
  font-style: normal;
}

.subheader__section--left {
  flex: 1;
}

.panel-subheader__general-questions {
  height: 100%;
  overflow: hidden;
  font-style: normal;
}

.subheader__section--right .question-of-the-day {
  flex-shrink: 0;
}

.header__keywords {
  font-weight: 600;
  word-break: break-word;
  height: 100%;
}

@media screen and (min-width: 812px) {
  .panel-container {

    height: 100%;
  }

  .panel-header {
    gap: 8px;
    grid-template-columns: 2fr 3fr;
  }

  .panel-subheader {
    gap: 8px;
    flex-direction: row;
  }

  .subheader__section--right {
    border-left: solid 1px var(--border-color);
  }

  .panel-content {
    display: grid;
    position: relative;
    grid-template-columns: 1fr;
    padding: 8px;
    gap: 8px;
    overflow-y: scroll;
    width: 100%;
    height: 100%;
  }
}

@media screen and (min-width: 1200px) {
  .panel-content {
    grid-template-columns: 1fr 1fr;
  }
}
</style>
