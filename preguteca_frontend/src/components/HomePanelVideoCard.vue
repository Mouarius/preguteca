<script setup lang="ts">
import { ref } from "vue";
import { HomepageVideoPost, } from "../types";
import PlayButton from "../assets/play-button--orange.svg";
import HomePanelCard from "./homepanel-card/HomePanelCard.vue";

type Props = {
  videoPost: HomepageVideoPost
};
defineProps<Props>();

const isVideoVisible = ref(false);

const setVideoVisible = () => {
  isVideoVisible.value = !isVideoVisible.value;
};
</script>
<template>
  <HomePanelCard :header-title="videoPost.headerTitle"
    :header-supplementary-information="videoPost.headerSupplementaryInformation"
    :footer-left-name="videoPost.footerLeftName" :footer-left-value="videoPost.footerLeftValue"
    :footer-right-name="videoPost.footerRightName" :footer-right-value="videoPost.footerRightValue">

    <div class="row url">
      <a :href="videoPost.video.videoUrl">{{ videoPost.video.videoUrl }}</a>
    </div>
    <div class="row video__viewport">
      <iframe v-if="isVideoVisible" class="video__viewport__iframe" type="text/html" width="100%" height="100%"
        allow="autoplay; fullscreen; accelerometer; gyroscope; picture-in-picture" frameborder="0"
        :src="`${videoPost.video.videoEmbedUrl}?autoplay=1`"></iframe>
      <template v-else>
        <button class="video__viewport__button" @click="setVideoVisible">
          <img :src="PlayButton" alt="" />
        </button>
        <img v-if="videoPost.video.thumbnailUrl" class="video__viewport__thumbnail" :src="videoPost.video.thumbnailUrl"
          alt="Video Thumbnail" height="360" width="480" />
      </template>
    </div>
    <div class="details">
      <div class="row details__header">
        <div class="details__header__element details__header__element--title">
          {{ videoPost.video.title }}
        </div>
        <div class="details__header__element details__header__element--duration">
          {{ videoPost.video.duration }}
        </div>
      </div>
    </div>
    <div class="row content">
      {{ videoPost.content }}
    </div>
  </HomePanelCard>
</template>
<style scoped>
.url {
  font-style: normal;
  font-family: "Open Sans", Arial, Helvetica, sans-serif;
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
  font-family: "Open Sans", Arial, Helvetica, sans-serif;
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

.content {
  height: 100%;
  flex: 1;
}

.details__content {
  height: fit-content;
  padding: 8px;
  text-align: justify;
  font-family: "Open Sans", Arial, Helvetica, sans-serif;
  font-style: normal;
}
</style>
