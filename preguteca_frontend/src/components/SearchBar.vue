<script setup lang="ts">
import { computed, reactive, ref, watch } from "vue";
import SearchIcon from "../assets/search-icon.svg";
import { useCategories } from "../queries/useCategories";
import { BaseCategory} from "../types";
import { updateActivePanel } from "../store";
import Fuse from "fuse.js";

const props = defineProps<{
  setActiveCategory: (name: string) => void;
}>();

const MIN_CHARACTERS_TO_START = 3;
const MAX_LIST_LENGTH = 8;

let searchText = ref("");

const activeIndex = ref(0);
const categories = reactive(useCategories());

const matchedCategories = computed(() => {
  if (categories.data) {
    return getMatchedCategories(searchText.value, categories.data);
  }
  return [];
});
const setActiveIndex = (value: number) => {
  activeIndex.value = value;
};

const getMatchedCategories = (
  searchText: string,
  categoriesList: BaseCategory[]
): BaseCategory[] => {
  const fuse = new Fuse(categoriesList, { keys: ["fullName", "name"] });
  const result = fuse.search(searchText);
  return result.map((res) => res.item).slice(0, MAX_LIST_LENGTH);
};

const handleFormSubmit = (event: Event) => {
  event.preventDefault();
  if (
    !searchText.value ||
    categories.isError ||
    matchedCategories.value.length === 0
  )
    return;
  try {
    const category = matchedCategories.value[activeIndex.value];
    updateActivePanel("category");
    props.setActiveCategory(category.name);
    setActiveIndex(0);
    searchText.value = "";
  } catch {
    return;
  }
};

const nextSuggestion = (current: number) => {
  return Math.min(current + 1, MAX_LIST_LENGTH);
};
const prevSuggestion = (current: number) => {
  return Math.max(current - 1, 0);
};

function handleKeyDown(event: KeyboardEvent) {
  switch (event.key) {
    case "ArrowDown":
      return setActiveIndex(nextSuggestion(activeIndex.value));
    case "ArrowUp":
      return setActiveIndex(prevSuggestion(activeIndex.value));
    default:
      break;
  }
}

// Reset the active index when typing
watch([searchText], () => {
  setActiveIndex(0);
});
</script>
<template>
  <div class="search-bar">
    <form method="get" action="" @submit="handleFormSubmit">
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
      <button type="submit" class="search-bar__search-button">
        <img :src="SearchIcon" alt="Search icon" />
      </button>
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
              active: index === activeIndex,
            }"
          >
            <button type="submit" @mouseenter="() => setActiveIndex(index)">
              {{ category.fullName.toLowerCase() }}
            </button>
          </li>
        </ul>
      </div>
    </form>
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
  top: 34px;
  left: 0;
  box-shadow: 0px 8px 18px rgba(0, 0, 0, 0.6);
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
  border-bottom: solid 1px rgba(255, 255, 255, 0.554);
}

.suggestion__element {
  cursor: pointer;
}

.suggestion__element button {
  border: none;
  background: none;
  color: var(--text);
  display: flex;
  cursor: pointer;
  width: 100%;
  height: 100%;
  padding: 8px;
  text-align: left;
}

.suggestion__element.active button {
  color: var(--black);
  font-weight: 500;
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

.search-bar__search-button {
  border: none;
  background: none;
  color: var(--text);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
</style>
