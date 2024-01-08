<script setup lang="ts">
import { MenuPage } from '../types';

type MenuPanelProps = {
  menuPage: MenuPage | null
}

defineProps<MenuPanelProps>()

</script>
<template>
  <section class="aside-container">
    <div class="aside-header">
      <span class="header__title">
        {{ menuPage?.title }}
      </span>
    </div>
    <div class="aside-content">
      <span v-html="menuPage?.content"></span>
    </div>

  </section>
</template>
<style scoped>
.aside-container {
  width: 100%;
  grid-area: aside;
  display: flex;
  flex-direction: column;
  font-style: italic;
  border: solid 1px var(--border-color);
  overflow: scroll;
}

.aside-header {
  padding: 8px;
  padding-left: 10px;
  padding-right: 12px;
  background: var(--white);
  color: var(--black);
  display: grid;
  gap: 8px;
  grid-template-columns: 1fr;
}

.aside-header .header__title {
  font-size: 24px;
  cursor: pointer;
  font-weight: 600;
  height: 100%;
  font-family: var(--font-title);
}

.aside-content {
  width: 100%;
  padding: 8px;
  gap: 8px;
  overflow-y: scroll;
}
</style>
