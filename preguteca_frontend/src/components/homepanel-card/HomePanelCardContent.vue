<script setup lang="ts">
import { ref } from "vue";
import type { TVideoEntry } from "../../types";
import PlayButton from "../../assets/play-button--orange.svg";

type Props = {
  video: TVideoEntry | null;
  content: string;
};
defineProps<Props>();

const isVideoVisible = ref(false);

const setVideoVisible = () => {
  isVideoVisible.value = !isVideoVisible.value;
};
</script>
<template>
  <div v-if="video" class="row url">
    <a :href="video.videoUrl">{{ video.videoUrl }}</a>
  </div>
  <div v-if="video" class="video__viewport">
    <iframe
      v-if="isVideoVisible"
      class="video__viewport__iframe"
      type="text/html"
      width="100%"
      height="100%"
      allow="autoplay; fullscreen; accelerometer; gyroscope; picture-in-picture"
      frameborder="0"
      :src="`https://www.youtube.com/embed/${video.youtubeId}?autoplay=1`"
    ></iframe>
    <template v-else>
      <button class="video__viewport__button" @click="setVideoVisible">
        <img :src="PlayButton" alt="" />
      </button>
      <img
        v-if="video.thumbnailUrl"
        class="video__viewport__thumbnail"
        :src="video.thumbnailUrl"
        alt="Video Thumbnail"
        height="360"
        width="480"
      />
    </template>
  </div>
  <div class="details">
    <div v-if="video" class="row details__header">
      <div class="details__header__element details__header__element--title">
        {{ video.title }}
      </div>
      <div class="details__header__element details__header__element--duration">
        {{ video.duration }}
      </div>
    </div>
    <div class="row details__content text-content">
      <span v-dompurify-html="content"></span>
    </div>
  </div>
</template>
<style scoped>
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
  display: flex;
  align-items: center;
  justify-content: center;
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

.details {
  display: flex;
  flex-direction: column;
  flex: 1;
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

.details__content {
  height: 100%;
  flex: 1;
  display: flex;
  align-items: start;
  padding: 8px;
}

.text-content {
  font-style: normal;
  font-size: 14px;
  line-height: 1.5;
}

.text-content span a {
  color: var(--text);
  font-weight: 600;
  word-break: break-all !important;
}
</style>
