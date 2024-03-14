<script setup lang="ts">
import { updateActivePanel } from "../store";
import SearchBar from "./SearchBar.vue";
import MenuButton from "./MenuButton.vue";
import { MenuPage } from "../types";
defineProps<{
  setActiveMenu: (menu: MenuPage) => void;
  setActiveCategory: (name: string) => void;
}>();
</script>

<template>
  <header>
    <div class="logo-title__container" @click="() => updateActivePanel('home')">
      <div class="logo-container">
        <img
          id="logo"
          src="/src/assets/preguteca_logo_120.svg"
          alt="logo"
          height="120"
          width="120"
        />
      </div>
      <div class="title__container">
        <h1 id="page-title">SONDEO</h1>
        <div class="subtitle">/ Explorando alternativas</div>
      </div>
    </div>
    <div class="search-bar__label">
      <label for="page-header__search-category" class="sr-only">Buscar</label>
    </div>
    <div class="search-bar__container">
      <SearchBar :set-active-category="setActiveCategory" />
    </div>
    <div class="menu-button__container">
      <MenuButton :set-active-menu="setActiveMenu" />
    </div>
  </header>
</template>

<style scoped>
#preguteca-menu-button {
  display: flex;
}

.logo-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  padding: 4px;
  border-right: solid 1px var(--border-color);
}

.title__container {
  display: none;
  align-items: baseline;
}

.subtitle {
  display: none;
  font-family: "Rethink Sans", Arial, Helvetica, sans-serif;
  font-size: 14px;
  color: var(--dimmed-text);
  position: relative;
  bottom: 2px;
}

#logo {
  height: 40px;
  width: 40px;
  object-fit: cover;
}

header {
  height: 100%;
  display: flex;
  position: relative;
  flex-direction: row;
  align-items: center;
  justify-items: stretch;
  grid-area: header;
  box-sizing: border-box;
  border: solid 1px var(--border-color);
}

.logo-title__container {
  display: flex;
  flex: 1;
  height: 100%;
  align-items: center;
  overflow: visible;
  cursor: pointer;
}

.search-bar__container {
  padding: 8px;
  height: 100%;
}

.menu-button__container {
  margin-right: 8px;
  margin-left: 8px;
}

@media (min-width: 768px) {
  .title__container {
    display: flex;
    align-items: baseline;
  }

  .subtitle {
    display: block;
    font-style: italic;
  }
}

#page-title {
  font-family: "Dela Gothic One", Times, serif;
  font-size: 40px;
  position: relative;
  font-weight: 500;
  margin: 0px 8px;
  bottom: 2px;
}
</style>
