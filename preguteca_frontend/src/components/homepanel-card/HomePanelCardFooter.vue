<script setup lang="ts">
type HomePanelCardFooterProps = {
  leftName?: string | null
  leftValue?: string | null
  rightName?: string | null
  rightValue?: string | null
}
defineProps<HomePanelCardFooterProps>()
</script>
<template>
  <div v-if="leftName && rightName" class="footer">
    <div class="footer__element">
      <span class="footer__element__key">{{ leftName }}</span>
      <span class="footer__element__value">{{ leftValue }}</span>
    </div>
    <div class="footer__element">
      <span class="footer__element__key">{{ rightName }}</span>
      <span class="footer__element__value">{{ rightValue }}</span>
    </div>
  </div>
</template>
<style>
.footer {
  padding: 0px 8px;
  display: flex;
  justify-content: space-between;
  min-height: 32px;
  flex-shrink: 0;
  height: fit-content;
}

.footer__element {
  font-size: 12px;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 4px;
  align-items: baseline;
  padding: 8px 0;
}

.footer__element:last-child {
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

</style>
