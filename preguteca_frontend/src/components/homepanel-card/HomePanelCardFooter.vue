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
      <div v-if="leftName && rightName" class="row details__footer">
        <div class="details__footer__element">
          <span class="footer__element__key">{{leftName}}</span>
          <span class="footer__element__value">{{leftValue}}</span>
        </div>
        <div class="details__footer__element">
          <span class="footer__element__key">{{rightName}}</span>
          <span class="footer__element__value">{{rightValue}}</span>
        </div>
      </div>
</template>
