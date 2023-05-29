<script setup lang="ts">
</script>

<template>
    <header id="page-header" class="border-thin">
        <h1 id="page-title">PREGUTECA</h1>
    </header>
    <div id="page-content" class="border-thin">
        <section id="main-scroll">
            <div id="scroll-illustration">

            </div>

        </section>
        <section id="category-container">
            <header>
                <h2>LA ESCUELA</h2>
            </header>
            <section class="container">
                <ul class="video-entry-list">
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
                </ul>
            </section>
        </section>
    </div>
</template>

<style scoped>

#page-header {
    position: relative;
    top: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding-left: 16px;
    grid-area: header;
}

#page-title {
    font-size: 32px;
    font-weight: 500;
}

#page-content {
    width: 100%;
    position: relative;
    grid-area: content;
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-template-areas: "main-scroll main-scroll aside aside aside";
    overflow: hidden;
}

#main-scroll {
    grid-area: main-scroll;
}

#category-container {
    grid-area: aside;
    border-left: solid 1px var(--border-color);

}

#category-container > header {
    background: var(--white);
    padding-left: 16px;
    height: 42px;
    width: 100%;
    color: var(--text);
    display: flex;
    justify-content: flex-start;
    align-items: center;
}

#category-container > section.container {
    padding: 8px;
    overflow: scroll;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    width: 100%;
    height: 100%;
    position: relative;
}

#category-container ul {
    position: relative;
    width: 100%;
}

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

.border-thin {
    border: solid 1px var(--border-color)
}


h1 {
    font-family: "Space Grotesk", "Arial Black", sans-serif;
    font-size: 2.4rem;
    font-weight: 600;
}

h2 {
    font-family: "Space Grotesk", "Arial Black", sans-serif;
    font-size: 24px;
    font-weight: 600;
}

h3 {
    font-size: 1.4rem;
    font-weight: 600;
}

li {
    list-style-type: none;
}


.container {
    display: block;
    position: relative;
    width: 100%;
}
</style>
