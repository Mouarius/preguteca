<script setup lang="ts">
type HomePanelCardHeaderProps = {
  title: string;
  supplementaryInformation?: string | null;
  isVideoPost: boolean;
};

defineProps<HomePanelCardHeaderProps>();
</script>
<template>
  <div class="header">
    <div class="header__element header__element--title">
      {{ title }}
    </div>
    <div
      v-if="supplementaryInformation && isVideoPost"
      class="header__element header__element--type"
    >
      {{ supplementaryInformation }}
    </div>
  </div>
</template>
<style>
.header {
  display: flex;
  min-height: 32px;
  padding: 0px 8px;
  line-height: 1.8;
  height: fit-content;
  align-items: center;
}

.header__element {
  height: 100%;
  padding: 8px 0px;
  box-sizing: content-box;
  min-height: 32px;
  display: flex;
  align-items: center;
}

.header__element--title {
  flex: 1;
  min-width: 66%;
  font-size: 18px;
  font-style: normal;
  font-weight: 600;
  font-family: var(--font-title);
  height: 100%;
}

.header__element--type {
  font-size: 14px;
  display: flex;
  height: 100%;
  justify-content: center;
  border-left: solid 1px var(--border-color);
  padding-left: 8px;
}
</style>
