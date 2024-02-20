<script setup lang="ts">
import { reactive, ref } from "vue";
import { useMenuPages } from "../queries/useMenuPages";
import { MenuPage } from "../types";

const props = defineProps<{ setActiveMenu: (menu: MenuPage) => void }>();

const menuPages = useMenuPages();

const dropdownHidden = ref(true);
type SVGLineCoords = {
  x1: number;
  y1: number;
  x2: number;
  y2: number;
};
const defaultLineCoords: SVGLineCoords[] = [
  {
    x1: 0,
    y1: 1,
    x2: 32,
    y2: 1,
  },
  {
    x1: 0,
    y1: 15,
    x2: 32,
    y2: 15,
  },
  {
    x1: 0,
    y1: 29,
    x2: 32,
    y2: 29,
  },
];
const initialLineCoords: SVGLineCoords[] = [
  {
    x1: 0,
    y1: 1,
    x2: 32,
    y2: 1,
  },
  {
    x1: 0,
    y1: 15,
    x2: 32,
    y2: 15,
  },
  {
    x1: 0,
    y1: 29,
    x2: 32,
    y2: 29,
  },
];

const lineCoords = reactive([...initialLineCoords]);

function menuButtonToBurger() {
  for (let i = 0; i < lineCoords.length; i++) {
    for (const key of Object.keys(lineCoords[i])) {
      lineCoords[i][key as keyof SVGLineCoords] =
        defaultLineCoords[i][key as keyof SVGLineCoords];
    }
  }
}

function menuButtonToCross() {
  lineCoords[0].y2 = 29;
  lineCoords[1].x1 = 16;
  lineCoords[1].x2 = 16;
  lineCoords[2].y2 = 1;
}

function goToClickedMenu(_event: MouseEvent, slug: MenuPage) {
  props.setActiveMenu(slug)
  toggleDropdownHidden();
}

function toggleDropdownHidden() {
  dropdownHidden.value = !dropdownHidden.value;

  if (dropdownHidden.value) {
    menuButtonToBurger();
  } else {
    menuButtonToCross();
  }
}
</script>
<template>
  <div class="bar-container" @click="toggleDropdownHidden">
    <svg height="30" width="32">
      <line v-for="(lineCoord, key) in lineCoords" :key="`line${key}`" :x1="lineCoord.x1" :y1="lineCoord.y1"
        :x2="lineCoord.x2" :y2="lineCoord.y2" style="stroke: white; stroke-width: 1" />
    </svg>
  </div>
  <ul v-if="!dropdownHidden && menuPages.data" class="dropdown">
    <li v-for="menuPage in menuPages.data.value" v-bind:key="menuPage.slug"
      @click="(event) => goToClickedMenu(event, menuPage)">
      {{ menuPage.title }}
    </li>
  </ul>
</template>

<style scoped>
.bar-container {
  display: flex;
  flex-direction: column;
  aspect-ratio: 1;
  justify-content: space-between;
  height: 30px;
  width: 32px;
  cursor: pointer;
}

.dropdown {
  position: absolute;
  background: var(--black);
  width: 304px;
  right: -1px;
  border: solid 1px var(--border-color);
  margin-top: 10px;
  z-index: 10;
  display: flex;
  flex-direction: column;
}

.dropdown li {
  width: 100%;
  padding: 8px;
}

.dropdown li:not(:last-child) {
  border-bottom: solid 1px rgba(255, 255, 255, 0.554);
}

.dropdown li:hover {
  background-color: white;
  color: var(--black);
  font-weight: 500;
  cursor: pointer;
  border: solid 1px var(--black);
}
</style>
