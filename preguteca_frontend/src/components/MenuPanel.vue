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
    <div class="aside-content text-content">
      <span v-html="menuPage?.content"></span>
    </div>

  </section>
</template>
<style>
.aside-container {
  /* TODO: Refactor this */
  width: 100%;
  grid-area: aside;
  display: flex;
  flex-direction: column;
  font-style: italic;
  border: solid 1px var(--border-color);
  overflow: scroll;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  background-color: var(--black);
  transform: translateX(0);
  transition: all 0.4s ease-in;
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
  padding: 24px 12px;
  gap: 8px;
  overflow-y: scroll;
  font-style: normal;
}
</style>
