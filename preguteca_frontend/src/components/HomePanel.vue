<script setup lang="ts">
import { useHomePage } from "../queries/useHomePage.ts";
import { updateActiveCategory } from "../store";
import HomePanelTextPostCard from "./HomePanelTextPostCard.vue";
import HomePanelVideoCard from "./HomePanelVideoCard.vue";
const homePage = useHomePage();
</script>
<template>
  <div class="container">
    <div class="header">
      <div class="header__section hearder__part--building">
        <div
          class="header__title"
          @click="
            () => updateActiveCategory(homePage.data.value?.monthCategory)
          "
        >
          {{ homePage.data.value?.monthCategory.fullName }}
        </div>
        <div class="separator separator--header"></div>
        <div class="header__subtitle">Edificio del mes</div>
      </div>
      <div class="header__section hearder__part--question">
        <div class="header__keywords">
          {{ homePage.data.value?.monthCategory.keywords }}
        </div>
        <div class="separator separator--header"></div>
        <div class="header__subtitle">Palabras clave</div>
      </div>
    </div>
    <div class="subheader">
      <div class="subheader__section subheader__section--left">
        <p class="subheader__general-questions">
          {{ homePage.data.value?.monthQuestions }}
        </p>
      </div>
      <div class="subheader__section subheader__section--right">
        <div class="question-of-the-day">
          {{ homePage.data.value?.dayQuestion }}
        </div>
        <div class="separator separator--subheader"></div>
        <div class="subheader__subtitle">Question del dia</div>
      </div>
    </div>
    <div class="content" v-if="homePage.isSuccess" >
      <HomePanelVideoCard
        v-for="videoPost in homePage.data.value?.videoPosts"
        v-bind:key="videoPost.id"
        :video-post="videoPost"
      />
      <HomePanelTextPostCard
        v-for="textPost in homePage.data.value?.textPosts"
        v-bind:key="textPost.id"
        :title="textPost.headerTitle"
        :content="textPost.content"
      />
    </div>
  </div>
</template>
<style scoped>
.content {
  display: grid;
  position: relative;
  grid-template-columns: 1fr;
  padding: 8px;
  gap: 8px;
  overflow-y: scroll;
  width: 100%;
  height: 100%;
}

@media screen and (min-width: 1000px) {
  .content {
    grid-template-columns: 1fr 1fr;
  }
}

.container {
  width: 100%;
  grid-area: aside;
  display: flex;
  flex-direction: column;
  font-family: "Times New Roman", Times, serif;
  font-style: italic;
  border: solid 1px var(--border-color);
  overflow: scroll;
}

.header {
  padding: 8px;
  padding-left: 10px;
  padding-right: 12px;
  background: var(--white);
  color: var(--black);
  display: grid;
  gap: 8px;
  grid-template-columns: 1fr;
}

.header__title {
  cursor: pointer;
}

.header__section {
  display: flex;
  align-items: end;
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

.header__title {
  font-size: 24px;
  font-weight: 600;
  height: 100%;
}

.header__subtitle,
.subheader__subtitle {
  font-size: 14px;
}

.subheader__subtitle {
  color: var(--border-color);
  place-self: end;
}

.subheader {
  color: var(--border-color);
  background-color: var(--black);
  display: flex;
  flex-direction: column;
  align-items: start;
  border-bottom: solid 1px var(--border-color);
}

.subheader__section {
  display: flex;
  padding: 8px;
  height: 100%;
}

.question-of-the-day {
  font-family: "Open Sans", Arial, Helvetica, sans-serif;
  font-weight: 600;
  font-style: normal;
}

.subheader__section--left {
  flex: 1;
}

.subheader__general-questions {
  height: 100%;
  overflow: hidden;
}

.subheader__section--right .question-of-the-day {
  flex-shrink: 0;
}

.header__keywords {
  font-weight: 600;
  word-break: break-word;
  height: 100%;
}

@media screen and (min-width: 768px) {
  .header {
    gap: 0px;
    grid-template-columns: 2fr 3fr;
  }

  .subheader {
    gap: 0px;
    flex-direction: row;
  }

  .subheader__section--right {
    border-left: solid 1px var(--border-color);
  }
}
</style>
