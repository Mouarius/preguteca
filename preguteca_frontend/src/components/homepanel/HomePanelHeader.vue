<script setup lang="ts">
import { HomePage } from "../../types";

defineProps<{
  homePage: HomePage;
  setActiveCategory: (name: string) => void;
  onBackButtonClick: (evt: MouseEvent) => void;
  onHeaderClick?: (evt: MouseEvent) => void;
}>();
</script>
<template>
  <div class="panel-header" @click="onHeaderClick">
    <div class="panel-header__section hearder__part--building">
      <div
        class="panel-header__title"
        @click="() => setActiveCategory(homePage.monthCategory.name)"
      >
        {{ homePage.monthCategory.fullName }}
      </div>
      <div class="separator separator--header"></div>
      <div class="header__subtitle">Edificio del mes</div>
    </div>
    <div class="panel-header__section hearder__part--question">
      <div class="header__keywords">
        {{ homePage.monthCategory.keywords }}
      </div>
      <div class="separator separator--header"></div>
      <div class="header__subtitle">Palabras clave</div>
    </div>
  </div>
  <div class="panel-subheader">
    <div class="panel-subheader__section subheader__section--left">
      <p class="panel-subheader__general-questions">
        {{ homePage.monthQuestions }}
      </p>
    </div>
    <div class="panel-subheader__section subheader__section--right">
      <div class="question-of-the-day">
        {{ homePage.dayQuestion }}
      </div>
      <div class="panel-subheader__subtitle">Pregunta del día</div>
    </div>
  </div>
</template>
<style scoped>
.arrow-right__container {
  display: flex;
  justify-content: flex-end;
}

.panel-header {
  padding: 8px;
  justify-content: space-between;
  background: var(--white);
  color: var(--black);
  cursor: pointer;
  display: flex;
  gap: 16px;
}

.panel-header__section {
  display: flex;
  align-items: end;
  height: 40px;
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
  height: auto;
}

.panel-header__title {
  font-size: 24px;
  cursor: pointer;
  font-weight: 600;
  height: 100%;
  min-width: 8ch;
}

.header__subtitle,
.panel-subheader__subtitle {
  font-size: 14px;
}

.panel-subheader__subtitle {
  color: var(--border-color);
  place-self: end;
  position: absolute;
  right: 10px;
}

.panel-subheader {
  color: var(--border-color);
  background-color: var(--black);
  display: flex;
  flex-direction: column;
  align-items: start;
  line-height: 1.3;
  min-height: 6lh;
  height: fit-content;
  border-bottom: solid 1px var(--border-color);
}
.subheader__section--right {
  position: relative;
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
  min-width: 0px;
  overflow: scroll;
}

.panel-subheader__general-questions {
  min-height: 4lh;
  height: fit-content;
  font-style: normal;
}

.subheader__section--right .question-of-the-day {
  flex-shrink: 0;
}

.header__keywords {
  font-weight: 600;
  word-break: break-word;
  height: 100%;
  min-width: 8ch;
}

@media screen and (min-width: 812px) {
  .panel-header {
    gap: 8px;
  }

  .panel-subheader {
    gap: 8px;
    flex-direction: row;
  }

  .subheader__section--right {
    border-left: solid 1px var(--border-color);
  }
}
</style>
