<script setup lang="ts">
import { Ref, computed, reactive, ref } from "vue";
import SearchIcon from "../assets/search-icon.svg";
import { useCategories } from "../queries/useCategories";
import { TCategory } from "../types";
import { updateActiveCategory, updateActivePanel } from "../store";
import Fuse from "fuse.js";

const MIN_CHARACTERS_TO_START = 3;

let searchText = ref("");

const activeChoice = reactive({
  key: -1,
  category: undefined as TCategory | undefined,
});
const categories = reactive(useCategories());
const matchedCategories: Ref<TCategory[]> = computed(() => {
  if (categories.data) {
    return getMatchedCategories(searchText.value, categories.data);
  }
  return [];
});

const setActiveChoice = (key: number, category: TCategory) => {
  activeChoice.key = key;
  activeChoice.category = category;
};

function getMatchedCategories(
  searchText: string,
  categoriesList: TCategory[]
): TCategory[] {
  const fuse = new Fuse(categoriesList, { keys: ["fullName", "name"] });
  const result = fuse.search(searchText);
  console.log(result);
  return result.map((res) => res.item);
}

function handleFormSubmit(event: Event) {
  event.preventDefault();
  if (!searchText.value && categories.isError) return;
  if (categories.data) {
    const matchedCategories = getMatchedCategories(
      searchText.value,
      categories.data
    );
    if (matchedCategories.length === 0) return;
    if (!activeChoice.category) {
      activeChoice.category = matchedCategories[0];
    }
    updateActivePanel("category");
    updateActiveCategory(activeChoice.category);
    clearSearchBar();
  }
}
function clearSearchBar() {
  activeChoice.category = undefined;
  activeChoice.key = -1;
  searchText.value = "";
}

function handleSuggestionClick(index: number, category: TCategory) {
  activeChoice.key = index;
  activeChoice.category = category;
  if (!activeChoice.category || !activeChoice.key) return;
  updateActivePanel("category");
  updateActiveCategory(activeChoice.category);
  clearSearchBar();
}

function handleKeyDown(event: KeyboardEvent) {
  switch (event.key) {
    case "ArrowDown":
      if (activeChoice.key <= 8) {
        activeChoice.key += 1;
        activeChoice.category = matchedCategories.value[activeChoice.key];
      }
      break;
    case "ArrowUp":
      if (activeChoice.key >= 1) {
        activeChoice.key -= 1;
        activeChoice.category = matchedCategories.value[activeChoice.key];
      }
      break;

    default:
      break;
  }
}
</script>
<template>
  <div class="search-bar">
    <form action="get" @submit="handleFormSubmit">
      <input
        id="search-bar__autocomplete"
        v-model="searchText"
        autocomplete="off"
        dir="ltr"
        spellcheck="false"
        autocorrect="off"
        autocapitalize="off"
        tabindex="1"
        type="text"
        :onkeydown="handleKeyDown"
      />
      <button type="submit"><img :src="SearchIcon" /></button>
    </form>
    <div
      v-if="
        matchedCategories.length > 0 &&
        searchText.length >= MIN_CHARACTERS_TO_START
      "
      class="suggestions"
    >
      <ul>
        <li
          v-for="(category, index) in matchedCategories"
          :key="category.id"
          :class="{
            suggestion__element: true,
            active: index === activeChoice.key,
          }"
          @mouseover="() => setActiveChoice(index, category)"
          @click="() => handleSuggestionClick(index, category)"
        >
          {{ category.fullName.toLowerCase() }}
        </li>
      </ul>
    </div>
  </div>
</template>
<style scoped>
.active {
  background-color: white;
  color: var(--black);
  font-weight: 500;
}

.suggestions {
  position: absolute;
  width: 100%;
  display: flex;
  flex-direction: column;
  background: var(--black);
  border: solid 1px white;
  border-top: none;
  z-index: 10;
  overflow: scroll;
  max-height: 330px;
}

.suggestions li {
  padding: 8px;
  border-bottom: solid 1px rgba(255, 255, 255, 0.554);
}

.suggestion__element {
  cursor: pointer;
}

.search-bar__label {
  font-size: 18px;
}

.search-bar__container {
  grid-column: 4/6;
  width: 100%;
}

.search-bar {
  position: relative;
  height: 100%;
  width: 100%;
}

.search-bar form {
  display: flex;
  background-color: var(--black);
  border: solid 1px var(--border-color);
  height: 100%;
  width: 100%;
}

.search-bar form input {
  display: flex;
  background-color: var(--black);
  border: none;
  height: 100%;
  width: 100%;
  color: var(--text);
  padding: 0px 8px;
}

.search-bar form input:focus {
  outline: none;
}

.search-bar form button {
  border: none;
  background: none;
  color: var(--text);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
</style>
