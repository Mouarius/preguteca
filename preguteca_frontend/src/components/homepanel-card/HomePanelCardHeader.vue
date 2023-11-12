<script setup lang="ts">

type HomePanelCardHeaderProps = {
  title: string,
  supplementaryInformation?: string | null
}

defineProps<HomePanelCardHeaderProps>()
  
</script>
<template>
    <div class="row header">
      <div class="header__element header__element--title">
        {{ title }}
      </div>
      <div v-if="supplementaryInformation" class="header__element header__element--type">
        {{supplementaryInformation}}</div>
    </div>
</template>
