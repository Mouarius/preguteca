<script setup lang="ts">
import MenuButton from "./MenuButton.vue";
import SearchBar from "./SearchBar.vue";
</script>

<template>
  <header>
    <div class="logo-title__container">
      <div class="logo-container">
        <img src="/src/assets/preguteca_logo_120.svg" alt="logo" id="logo" height="120" width="120" />
      </div>
      <div class="title__container">
        <h1 id="page-title">PREGUTECA</h1>
        <div class="subtitle">/ Explorando alternativas</div>
      </div>
    </div>
    <div class="search-bar__label">
      <label for="page-header__search-category" class="sr-only">Buscar</label>
    </div>
    <div class="search-bar__container">
      <SearchBar />
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
}

.search-bar__container {
  padding: 8px;
  height: 100%;
}

@media (min-width: 768px) {
  #preguteca-menu-button {
    display: none;
  }

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
  font-size: 32px;
  font-weight: 500;
  margin: 0px 8px;
}
</style>
