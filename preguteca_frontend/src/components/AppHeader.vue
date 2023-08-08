<script setup lang="ts">
import SearchBar from './SearchBar.vue';


</script>

<template>
  <header>
    <div class="page-title__container">
      <h1 id="page-title">PREGUTECA</h1>
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
header {
  height: 100%;
  display: grid;
  flex-direction: row;
  align-items: center;
  justify-items: stretch;
  grid-template-columns: repeat(5, 1fr);
  grid-area: header;
  border: solid 1px var(--border-color);
}

header>* {
  height: 100%;
  align-items: center;
  display: flex;
  padding: 8px 8px;
}

.page-title__container {
  grid-column: 1 / 3;
  padding-left: 16px;
}


@media (min-width: 768px) {
  header {
    grid-template-columns: repeat(5, 1fr);
  }

  .page-title__container {
    grid-column: 1 / 3;
    padding-left: 16px;
  }

  .search-bar__label {
    grid-column: 3 / 4;
  }

  .search-bar__container {
    grid-column: 4 / 6;
  }
}


#page-title {
  font-size: 32px;
  font-weight: 500;
  margin: 0;
}
</style>
