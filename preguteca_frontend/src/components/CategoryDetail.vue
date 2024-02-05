<script setup lang="ts">
import VideoEntry from "./VideoEntry.vue";
import { store } from "../store";
import MainPanel from "./MainPanel.vue";
import ChevronLeft from "../assets/chevron-left.svg"
import { StyleValue, onMounted, reactive, ref, watch } from "vue";

const videoEntryListRef = ref<HTMLElement | null>(null)
const descriptionRef = ref<HTMLElement | null>(null)
const descriptionHidden = ref(false)

function resetVideoListScroll() {
  if (videoEntryListRef.value) {
    videoEntryListRef.value.scroll(0, 0)
  }
}

watch(() => store.activeCategory, () => resetVideoListScroll())

onMounted(() => {
  resetVideoListScroll()
})

const toggleDescription = () => {
  descriptionHidden.value = !descriptionHidden.value
}

</script>

<template>
  <MainPanel :title="store.activeCategory?.fullName">
    <div class="content"
      :style="{ 'transform': descriptionHidden && descriptionRef ? `translateY(-${descriptionRef?.offsetHeight + 12}px)` : 'translate(0)' }">
      <div class="description">
        <p ref="descriptionRef">
          {{ store.activeCategory?.description }}
        </p>
        <button type="button" @click="toggleDescription">
          <svg class="toggle-icon" :class="{ 'toggle-icon--close': descriptionHidden }" height="12" width="12">
            <line x1="0" y1="0" x2="12" y2="12" style="stroke: white; stroke-width: 1px;"
              :opacity="descriptionHidden ? 1 : 0"></line>
            <line x1="0" y1="12" x2="12" y2="0" style="stroke: white; stroke-width: 1px;"></line>
          </svg>

        </button>

      </div>
      <ul id="video-entry-list" ref="videoEntryListRef" class="video-entry-list scrollable">
        <VideoEntry v-for="( video_entry, index ) in  store.activeCategory?.videoEntries " :key="video_entry.id"
          :video-entry="video_entry" :videos-in-category="store.activeCategory?.videoEntries.length"
          :index-in-category="index" class="video-entry" />
      </ul>

    </div>
  </MainPanel>
</template>

<style scoped>
.description {
  display: flex;
  flex-direction: column;
  padding: 8px;
  padding-top: 12px;
  border-bottom: solid 1px var(--border-color);
  line-height: 1.3;
  overflow: hidden;
}

.content {
  transition: transform 0.5s ease-in;
  height: 100%
}


button {
  cursor: pointer;
  background: none;
  border: none;
  display: flex;
  width: 100%;
  justify-content: space-between;
  padding: 0;
  margin-top: 8px;
  padding-left:2px;
  margin-left: auto;
  color: white;
}

.toggle-icon {
  transition: all 0.2s ease;
  transform: rotate(45deg);
}

.toggle-icon--close {
  transform: rotate(-45deg);
}


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
