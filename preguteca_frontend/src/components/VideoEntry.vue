<script setup lang="ts">

</script>

<template>
    <li class="video-entry border-thin">
        <header class="video-entry_header video-entry_row">
            <div class="video-entry_header_number">1/12</div>
            <div class="video-entry_header_url"><a>https://www.youtube.com/watch?v=7gkB2DjHZu8</a>
            </div>
            <div class="video-entry_header_duration">53:12</div>
        </header>
        <div class="video-entry_iframe"></div>
        <div class="video-entry_detail video-entry_row">
            <div class="video-entry_detail_title">La Education en la epoca franquista</div>
            <div class="video-entry_detail_language">ES</div>
        </div>
        <div class="video-entry_detail video-entry_row">
            <div class="video-entry_detail_channel">De : Youtube Channel</div>
            <div class="video-entry_detail_pub-date">11/04/2023</div>
        </div>
        <div class="video-entry_description">
            <div class="video-entry_description_questions">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
                    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
                    nostrud
                    exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute
                    irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                    nulla
                    pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
                    officia
                    deserunt mollit anim id est laborum.</p>
            </div>
            <div class="video-entry_description_tag-list">
                <span class="tag">Conferencia</span>
                <span class="tag">Videoclip</span>
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

.video-entry > * {
    border-bottom: solid 1px var(--border-color);
}

.video-entry_row {
    width: 100%;
    height: 32px;
    display: flex;
    flex-direction: row;
    align-items: stretch;
}

.video-entry_row > * {
    height: 100%;
    display: flex;
    align-items: center;
    padding-left: 12px;
    padding-right: 12px;
}

.video-entry_row > *:not(:first-child) {
    border-left: solid 1px var(--white);
}

.video-entry_header_url, .video-entry_detail_channel, .video-entry_detail_title {
    flex: 1;
}

.video-entry_iframe {
    height: auto;
    width: 100%;
    aspect-ratio: 16/9;
    background: red;
    border-bottom: solid 1px;
}

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