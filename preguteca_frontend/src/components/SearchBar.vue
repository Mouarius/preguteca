<script setup lang="ts">
import { Ref, computed, reactive, ref, } from "vue";
import SearchIcon from "../assets/search-icon.svg";
import { useCategories } from "../queries/useCategories";
import { TCategory } from "../types";
import { updateActiveCategory } from "../store";

// const CHOICES_DISPLAY_COUNT = 10
const MIN_CHARACTERS_TO_START = 3


let searchText = ref("")

const activeChoice = reactive({
    key: -1,
    category: undefined as TCategory | undefined
})
const categories = reactive(useCategories())
const matchedCategories: Ref<TCategory[]> = computed(() => {
    if (categories.data) {
        return getMatchedCategories(searchText.value, categories.data)
    }
    return []
})
const matchedCategoryElements = ref<HTMLLIElement[]>([])


function getMatchedCategories(searchText: string, categoriesList: TCategory[]): TCategory[] {
    return categoriesList.filter(cat => cat.fullName.toLocaleLowerCase().startsWith(searchText))
}

function handleFormSubmit(event: Event) {
    event.preventDefault();
    if (!searchText.value && categories.isError) return
    if (categories.data) {
        const matchedCategories = getMatchedCategories(searchText.value, categories.data)
        if (matchedCategories.length === 0) return
        if (!activeChoice.category) {
            activeChoice.category = matchedCategories[0]
        }
        updateActiveCategory(activeChoice.category)
        clearSearchBar()
    }
}
function clearSearchBar() {
    activeChoice.category = undefined
    activeChoice.key = -1
    searchText.value = ""
}

function getSelectedCategory(categoryElements: HTMLLIElement[]) {
    const categoryElement = categoryElements.find(el => {
        const key = el.getAttribute("data-key")
        if (key) {
            return parseInt(key, 10) === activeChoice.key
        }
        return false
    })
    if (!categoryElement) return
    const categoryId = categoryElement.dataset.categoryId
    if (!categoryId) return
    return categories.data?.find(cat => cat.id === parseInt(categoryId, 10))
}

function handleKeyDown(event: KeyboardEvent) {
    switch (event.key) {
        case "ArrowDown":
            if (activeChoice.key <= 8) {
                activeChoice.key += 1
                activeChoice.category = getSelectedCategory(matchedCategoryElements.value)
            }
            break;
        case "ArrowUp":
            if (activeChoice.key >= 1) {
                activeChoice.key -= 1
                activeChoice.category = getSelectedCategory(matchedCategoryElements.value)
            }
            break;

        default:
            break;
    }
}

</script>
<template>
    <div class="search-bar">
        <form @submit="handleFormSubmit" action="get">
            <input id="search-bar__autocomplete" autocomplete="off" dir="ltr" spellcheck="false" autocorrect="off"
                autocapitalize="off" tabindex="1" v-model="searchText" type="text" :onkeydown="handleKeyDown" />
            <button type="submit"><img :src="SearchIcon" /></button>
        </form>
        <div v-if="matchedCategories.length > 0 && searchText.length >= MIN_CHARACTERS_TO_START" class="suggestions">
            <ul>
                <li v-for="(category, index) in matchedCategories" :class="{ active: index === activeChoice.key }"
                    :key="category.id" :data-key="index" ref="matchedCategoryElements" :data-category-id="category.id"> {{
                        category.fullName.toLowerCase() }} </li>
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

.search-bar__label {
    font-family: "Space Grotesk";
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