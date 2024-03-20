<script setup lang="ts">
import { reactive, watch } from "vue";
import { useHomePage } from "../../queries/useHomePage";
import { HomePage } from "../../types";

defineProps<{
  homePage: HomePage;
  setActiveCategory: (name: string) => void;
  onBackButtonClick: (evt: MouseEvent) => void;
  onHeaderClick?: (evt: MouseEvent) => void;
}>();

const result = reactive(useHomePage());
const { isFetching } = useHomePage();
watch(isFetching, () => console.log(isFetching));
</script>
<template>
  <div>
    <div class="panel-header" @click="onHeaderClick">
      <div
        class="panel-header__section hearder__part--building"
        :class="{ hidden: result.isFetching }"
      >
        <div
          class="panel-header__title"
          @click="() => setActiveCategory(homePage.monthCategory.name)"
        >
          {{ homePage.monthCategory.fullName }}
        </div>
        <div class="separator separator--header"></div>
        <div class="header__subtitle">Edificio del mes</div>
      </div>
      <div
        class="panel-header__section hearder__part--question"
        :class="{ hidden: result.isFetching }"
      >
        <div class="header__keywords">
          {{ homePage.monthCategory.keywords }}
        </div>
        <div class="separator separator--header"></div>
        <div class="header__subtitle">Palabras clave</div>
      </div>
    </div>
    <div class="panel-subheader">
      <div
        class="panel-subheader__section subheader__section--left"
        :class="{ hidden: result.isFetching }"
      >
        {{ homePage.monthQuestions }}
      </div>
      <div
        class="panel-subheader__section subheader__section--right"
        :class="{ hidden: result.isFetching }"
      >
        <div class="question-of-the-day">
          {{ homePage.dayQuestion }}
        </div>
        <div class="panel-subheader__subtitle">Pregunta del día</div>
      </div>
    </div>
  </div>
</template>
<style scoped>
* {
  opacity: 1;
  transition: opacity 0.2s ease-in;
}
.hidden {
  opacity: 0;
}
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

.panel-subheader {
  color: var(--border-color);
  background-color: var(--black);
  display: flex;
  flex-direction: column;
  height: min-content;
  line-height: 1.3;
  border-bottom: solid 1px var(--border-color);
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

.question-of-the-day {
  font-weight: 600;
  font-style: normal;
}

.subheader__section--left {
  flex: 2;
  overflow-y: scroll;
  padding: 8px;
}

.subheader__section--right {
  padding: 8px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex: 1;
  border-top: solid 1px var(--border-color);
}

.panel-subheader__subtitle {
  color: var(--border-color);
  position: relative;
  margin-top: 8px;
  place-self: end;
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
