<script setup lang="ts">
import { ref } from 'vue';

type MenuButtonState = "IDLE" | "OPEN" | "HOVER"

const state = ref<MenuButtonState>("IDLE")
</script>
<template>
    <div class="bar-container">
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
    </div>
</template>
<style scoped>
.bar-container {
    display: flex;
    flex-direction: column;
    aspect-ratio: 1;
    justify-content: space-between;
    height: 30px;
    width: 32px;
    margin-right: 8px;
}

.bar {
    height: 2px;
    background-color: white;
    width: 100%;
}
</style>