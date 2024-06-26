<script setup lang="ts">
import { TVideoEntry } from "../types";
import PlayButton from "../assets/play-button--orange.svg";
import { ref } from "vue";

interface VideoEntryProps {
  videoEntry: TVideoEntry;
  videosInCategory?: number;
  indexInCategory?: number;
}

const isVideoVisible = ref(false);
const lastQuestionsVisible = ref(false);

function setVideoVisible() {
  isVideoVisible.value = true;
}

const getIndividualQuestions = (questions: string) => {
  let presplittedQuestions = questions.replace(/\? ¿/g, "?|¿");
  const splittedQuestions = presplittedQuestions.split("|");

  return splittedQuestions;
};

const getFirstQuestionsFormatted = (questions: string) => {
  const splittedQuestions = getIndividualQuestions(questions);
  const firstQuestions = splittedQuestions.slice(0, 3).join(" ");

  return firstQuestions;
};
const getLastQuestionsFormatted = (questions: string) => {
  const splittedQuestions = getIndividualQuestions(questions);
  const lastQuestions = splittedQuestions.slice(4).join(" ");

  return lastQuestions;
};

const toggleLastQuestionsVisibility = () => {
  lastQuestionsVisible.value = !lastQuestionsVisible.value;
};

defineProps<VideoEntryProps>();
</script>

<template>
  <li class="video-entry border-thin">
    <header class="video-entry__header video-entry__row">
      <div class="video-entry__header__number">
        {{ (indexInCategory ?? 0) + 1 }}/{{ videosInCategory ?? 0 }}
      </div>
      <div class="video-entry__header__url">
        <a :href="`https://www.youtube.com/watch?v=${videoEntry.youtubeId}`"
          >https://www.youtube.com/watch?v={{ videoEntry.youtubeId }}</a
        >
      </div>
      <div class="video-entry__header__duration">{{ videoEntry.duration }}</div>
    </header>
    <div class="video-entry__viewport">
      <iframe
        v-if="isVideoVisible && videoEntry.videoEmbedUrl"
        class="video-entry__viewport__iframe"
        type="text/html"
        width="100%"
        height="100%"
        allow="autoplay; fullscreen; accelerometer; gyroscope; picture-in-picture"
        frameborder="0"
        :src="`${videoEntry.videoEmbedUrl}?autoplay=1`"
      ></iframe>
      <template v-else>
        <button class="video-entry__viewport__button" @click="setVideoVisible">
          <img :src="PlayButton" alt="" />
        </button>
        <img
          v-if="videoEntry.thumbnailUrl"
          class="video-entry__viewport__thumbnail"
          :src="videoEntry.thumbnailUrl"
          alt="Video Thumbnail"
          height="360"
          width="480"
        />
      </template>
    </div>
    <div class="video-entry__detail video-entry__row">
      <div class="video-entry__detail__title">{{ videoEntry.title }}</div>
      <div class="video-entry__detail__language">ES</div>
    </div>
    <div class="video-entry__detail video-entry__row">
      <div class="video-entry__detail__channel">
        <a
          :href="`https://www.youtube.com/channel/${videoEntry.ytChannelId}`"
          >{{ videoEntry.author }}</a
        >
      </div>
      <div class="video-entry__detail__pub-date">
        {{ new Date(videoEntry.ytPublishTime).toLocaleDateString() }}
      </div>
    </div>
    <div class="video-entry__description">
      <div class="video-entry__description__questions">
        <span class="video-entry__questions__visible-questions">
          {{ getFirstQuestionsFormatted(videoEntry.questions) }}
          <button
            v-if="!lastQuestionsVisible"
            class="see-more-button"
            aria-label="See more"
            @click="toggleLastQuestionsVisibility"
          >
            <span class="circle"></span>
            <span class="circle"></span>
            <span class="circle"></span>
          </button>
        </span>
        <span
          v-if="lastQuestionsVisible"
          class="video-entry__questions__hidden-questions"
        >
          {{ getLastQuestionsFormatted(videoEntry.questions) }}
        </span>
      </div>
      <div class="video-entry__description__tag-list">
        <span
          v-for="videoType in videoEntry.videoTypes"
          :key="videoType.name"
          class="tag"
          >{{ videoType.fullName }}</span
        >
      </div>
    </div>
  </li>
</template>

<style scoped>
.video-entry {
  position: relative;
  width: 100%;
  display: flex;
  flex-direction: column;
  margin-bottom: 16px;
  box-shadow: 3px 3px var(--orange);
}

.see-more-button {
  display: inline-flex;
  position: relative;
  gap: 4px;
  background: none;
  border: none;
  font-size: 12px;
  color: var(--border-color);
  cursor: pointer;
}

.see-more-button .circle {
  border-radius: 100%;
  height: 6px;
  width: 6px;
  background-color: var(--border-color);
}

a {
  color: var(--white);
}

.video-entry > *:not(:last-child) {
  border-bottom: solid 1px var(--border-color);
}

.video-entry__row {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: stretch;
}

.video-entry__row > * {
  height: 100%;
  display: flex;
  padding: 8px 0px;
  align-items: center;
  padding-left: 12px;
  padding-right: 12px;
}

.video-entry__row > *:not(:first-child) {
  border-left: solid 1px var(--white);
}

.video-entry__header {
  color: var(--text);
  font-size: 14px;
}

.video-entry__header__url {
  position: relative;
  font-style: normal;
  font-size: 14px;
  display: block;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
}

.video-entry__header__url a {
  width: 100%;
  color: var(--text);
  max-width: 100%;
  text-overflow: ellipsis;
  overflow: hidden;
}

.video-entry__detail {
  font-size: 14px;
}

.video-entry__header__url,
.video-entry__detail__channel,
.video-entry__detail__title {
  flex: 1;
}

.video-entry__detail__title {
  font-size: 18px;
  font-weight: bold;
}

.video-entry__detail__channel,
.video-entry__detail__pub-date,
.video-entry__detail__language {
  color: var(--dimmed-text);
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

.video-entry__description {
  padding: 16px 12px;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.2rem;
  color: var(--dimmed-text);
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

.video-entry__description__questions {
  margin-bottom: 24px;
  text-align: justify;
}
</style>
