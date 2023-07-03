<script setup lang="ts">
import SearchIcon from "../assets/search-icon.svg";

function searchCategory(event: Event) {
  event.preventDefault();
}
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
      <div class="search-bar">
        <form @submit="searchCategory" action="get">
          <input id="page-header__search-category" value="" type="text" />
          <button type="submit"><img :src="SearchIcon" /></button>
        </form>
      </div>
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

header > * {
  height: 100%;
  align-items: center;
  display: flex;
  padding: 8px 8px;
}

.page-title__container {
  grid-column: 1 / 3;
  padding-left: 16px;
}

.search-bar__label {
  font-family: "Space Grotesk";
  font-size: 18px;
}
.search-bar__container {
  grid-column: 4/6;
  width: 100%;
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
.search-bar {
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

#page-title {
  font-size: 32px;
  font-weight: 500;
  margin: 0;
}
</style>
