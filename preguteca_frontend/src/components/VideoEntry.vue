<script setup lang="ts">
import { TVideoEntry } from "../types";
import PlayButton from "../assets/play-button--orange.svg";
import { ref } from "vue";

interface VideoEntryProps {
  videoEntry: TVideoEntry;
  videosInCategory: number;
  indexInCategory: number;
}

const isVideoVisible = ref(false);

function setVideoVisible() {
  isVideoVisible.value = true;
}

defineProps<VideoEntryProps>();
</script>

<template>
  <li class="video-entry border-thin">
    <header class="video-entry_header video-entry_row">
      <div class="video-entry_header_number">
        {{ indexInCategory + 1 }}/{{ videosInCategory }}
      </div>
      <div class="video-entry_header_url">
        <a :href="`https://www.youtube.com/watch?v=${videoEntry.youtubeId}`">https://www.youtube.com/watch?v={{
          videoEntry.youtubeId }}</a>
      </div>
      <div class="video-entry_header_duration">{{ videoEntry.duration }}</div>
    </header>
    <div class="video-entry__viewport">
      <iframe v-if="isVideoVisible" class="video-entry__viewport__iframe" type="text/html" width="100%" height="100%"
        allow="autoplay; fullscreen; accelerometer; gyroscope; picture-in-picture" frameborder="0"
        :src="`https://www.youtube.com/embed/${videoEntry.youtubeId}?autoplay=1`"></iframe>
      <template v-else>
        <button class="video-entry__viewport__button" @click="setVideoVisible">
          <img :src="PlayButton" alt="" />
        </button>
        <img class="video-entry__viewport__thumbnail" :src="videoEntry.thumbnailUrl" alt="Video Thumbnail" height="360"
          width="480" />
      </template>
    </div>
    <div class="video-entry_detail video-entry_row">
      <div class="video-entry_detail_title">{{ videoEntry.title }}</div>
      <div class="video-entry_detail_language">ES</div>
    </div>
    <div class="video-entry_detail video-entry_row">
      <div class="video-entry_detail_channel">
        De : {{ videoEntry.ytChannelTitle }}
      </div>
      <div class="video-entry_detail_pub-date">
        {{ new Date(videoEntry.ytPublishTime).toLocaleDateString() }}
      </div>
    </div>
    <div class="video-entry_description">
      <div class="video-entry_description_questions">
        <p>{{ videoEntry.questions }}</p>
      </div>
      <div class="video-entry_description_tag-list">
        <span v-for="videoType in videoEntry.videoTypes" class="tag" :key="videoType.name">{{ videoType.fullName }}</span>
      </div>
    </div>
  </li>
</template>

<style scoped>
.video-entry {
  font-family: "Space Grotesk", "Arial Black", sans-serif;
  position: relative;
  width: 100%;
  display: flex;
  flex-direction: column;
  margin-bottom: 16px;
}

a {
  color: var(--white);
}

.video-entry>*:not(:last-child) {
  border-bottom: solid 1px var(--border-color);
}

.video-entry_row {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: stretch;
}

.video-entry_row>* {
  height: 100%;
  display: flex;
  padding: 8px 0px;
  align-items: center;
  padding-left: 12px;
  padding-right: 12px;
}

.video-entry_row>*:not(:first-child) {
  border-left: solid 1px var(--white);
}

.video-entry_header_url,
.video-entry_detail_channel,
.video-entry_detail_title {
  flex: 1;
}

.video-entry_detail_title {
  font-weight: bold;
}

.video-entry_detail_channel {
  font-style: italic;
}

.video-entry__viewport {
  height: auto;
  position: relative;
  width: 100%;
  aspect-ratio: 16/9;
  border-bottom: solid 1px;
}

.video-entry__viewport__button {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
}

.video-entry__viewport__button img {
  height: 48px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.video-entry__viewport__button img:hover {
  transform: scale(1.1);
}

.video-entry__viewport__thumbnail {
  object-fit: cover;
  aspect-ratio: 16/9;
  height: auto;
  width: 100%;
}

.video-entry__viewport__iframe {}

.video-entry_description {
  padding: 16px 12px;
  font-size: 16px;
  font-family: "Public Sans", sans-serif;
  font-weight: 300;
  line-height: 1.3em;
}

.tag {
  font-size: 12px;
  border: solid 1px var(--border-color);
  border-radius: 100px;
  height: 20px;
  padding: 2px 8px;
  margin-right: 8px;
  cursor: default;
}

.tag:hover {
  background: var(--white);
  color: var(--black);
  font-weight: 500;
}

.video-entry_description_questions {
  margin-bottom: 24px;
}
</style>
