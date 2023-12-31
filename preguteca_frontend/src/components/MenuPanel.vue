<script setup lang="ts">
type CustomPanelProps = {
  // title: string,
  // content: string
}

defineProps<CustomPanelProps>()

</script>
<template>
  <section class="container">
    <div class="header">Title</div>
    <div class="content">
      <p>Some content</p>
    </div>

  </section>
</template>
<style scoped>
.container {
  width: 100%;
}

.header {
  width: 100%;

}

.content {
  width: 100%;
}
</style>
