<script setup lang="ts">
import VideoEntry from "./VideoEntry.vue";
import { store } from "../store";
import MainPanel from "./MainPanel.vue";
import { onMounted, ref, watch } from "vue";

const videoEntryListRef = ref<HTMLElement | null>(null)

function resetVideoListScroll() {
  if (videoEntryListRef.value) {
    videoEntryListRef.value.scroll(0, 0)
  }
}

watch(() => store.activeCategory, () => resetVideoListScroll())

onMounted(() => {
  resetVideoListScroll()
})

</script>

<template>
  <MainPanel :title="store.activeCategory?.fullName">
    <ul id="video-entry-list" class="video-entry-list scrollable" ref="videoEntryListRef">
      <VideoEntry v-for="(video_entry, index) in store.activeCategory?.videoEntries" :key="video_entry.id"
        :video-entry="video_entry" :videos-in-category="store.activeCategory?.videoEntries.length"
        :index-in-category="index" class="video-entry" />
    </ul>
  </MainPanel>
</template>

<style scoped>
.video-entry {
  scroll-snap-align: start;
}

.video-entry-list {
  scroll-padding-top: 8px;
  scroll-snap-type: y mandatory;
  overflow-y: scroll;
  max-height: 100%;
  padding: 8px;
  display: flex;
  flex-direction: column;
  align-self: stretch;
  align-items: center;
  justify-content: flex-start;
  width: 100%;
  height: 100%;
  position: relative;
}
</style>
