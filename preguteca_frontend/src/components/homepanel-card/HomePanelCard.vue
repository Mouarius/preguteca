<script setup lang="ts">
import HomePanelCardHeader from "./HomePanelCardHeader.vue";
import HomePanelCardFooter from "./HomePanelCardFooter.vue";

type Props = {
  headerTitle: string;
  headerSupplementaryInformation?: string | null;
  footerLeftName?: string | null;
  footerLeftValue?: string | null;
  footerRightName?: string | null;
  footerRightValue?: string | null;
}

defineProps<Props>()

</script>
<template>
  <div class="card-container">
    <HomePanelCardHeader :title="headerTitle" :supplementary-information="headerSupplementaryInformation" />
    <slot />
    <HomePanelCardFooter :left-name="footerLeftName" :left-value="footerLeftValue" :right-name="footerRightName"
      :right-value="footerRightValue" />
  </div>
</template>
<style>
.card-container {
  box-shadow: 4px 4px var(--orange);
  border: solid 1px var(--border-color);
  display: flex;
  flex-direction: column;
  min-width: 100%;
}

.card-container>div:not(:last-child) {
  border-bottom: solid 1px var(--border-color);
}

.row {
  padding: 0 8px;
  display: flex;
  align-items: center;
  height: 32px;
  min-height: 32px;
}

.header {
  display: flex;
  align-items: center;
}

.header__element {
  height: 100%;
  display: flex;
  align-items: center;
}

.header__element--title {
  flex: 1;
  font-size: 18px;
  font-style: normal;
  font-weight: 600;
  font-family: var(--font-title);
}

.header__element--type {
  font-size: 14px;
  display: flex;
  justify-content: center;
  border-left: solid 1px var(--border-color);
  padding-left: 8px;
}

.url {
  font-style: normal;
  height: 32px;
  padding: 8px;
  font-size: 14px;
}

.url a {
  width: 100%;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  color: rgb(218, 217, 217);
}

.video__viewport {
  height: auto;
  position: relative;
  width: 100%;
  aspect-ratio: 16/9;
  border-bottom: solid 1px;
}

.video__viewport__button {
  position: absolute;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  border: none;
  background: rgba(0, 0, 0, 0.5);
}

.video__viewport__button img {
  height: 48px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.video__viewport__button img:hover {
  transform: scale(1.1);
}

.video__viewport__thumbnail {
  object-fit: cover;
  aspect-ratio: 16/9;
  height: auto;
  width: 100%;
}

.details__header {
  border-bottom: solid 1px var(--border-color);
  position: relative;
  min-height: 32px;
  height: fit-content;
}

.details__header__element {
  display: flex;
  align-items: center;
}

.details__header__element--title {
  flex: 1;
  font-style: normal;
  font-weight: bold;
  height: auto;
  padding: 8px;
  padding-left: 0px;
  border-right: solid 1px var(--border-color);
}

.details__header__element--duration {
  justify-content: center;
  font-size: 14px;
  align-items: center;
  text-align: center;
  padding-left: 8px;
  height: 100%;
}

.details__footer {
  border-top: solid 1px var(--border-color);
  display: flex;
  justify-content: space-between;
  min-height: 32px;
  height: fit-content;
}

.details__footer__element {
  font-size: 12px;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 4px;
  align-items: baseline;
  padding: 8px 0;
}

.details__footer__element:last-child {
  border-left: solid 1px var(--border-color);
  padding-left: 8px;
  justify-content: end;
  min-width: 30%;
}

.footer__element__key {
  margin-right: 4px;
}

.footer__element__value {
  font-size: 16px;
  font-weight: 600;
  font-style: normal;
}

.details__content {
  height: fit-content;
  padding: 8px;
  text-align: justify;
  font-style: normal;
}
</style>
