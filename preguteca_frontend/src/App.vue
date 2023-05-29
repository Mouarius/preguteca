<script setup lang="ts">
import VideoEntry from "./components/VideoEntry.vue";
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
            <ul id="video-entry-list">

                <VideoEntry/>
                <VideoEntry/>
                <VideoEntry/>
                <VideoEntry/>
            </ul>
        </section>
    </div>
</template>

<style>
#app {
    max-height: 100vh;
    width: 100vw;
    left: 0;
    top: 0;
    right: 0;
    bottom: 0;
    padding: 8px;
    display: grid;
    grid-template-columns: 1fr;
    column-gap: 8px;
    row-gap: 8px;
    grid-template-rows: 52px minmax(0, 1fr);
    grid-template-areas: "header" "content";
    overflow: hidden;
}

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
    position: relative;
    box-sizing: border-box;
    grid-area: content;
    display: grid;
    bottom: 0;
    grid-template-columns: repeat(5, 1fr);
    grid-template-rows: minmax(0, 1fr);
    grid-template-areas: "main-scroll main-scroll aside aside aside";
}

#main-scroll {
    grid-area: main-scroll;
}


#category-container {
    grid-area: aside;
    border-left: solid 1px var(--border-color);
    position: relative;
    display: flex;
    flex-direction: column;
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


#video-entry-list {
    padding: 8px;
    display: flex;
    flex-direction: column;
    align-self: stretch;
    align-items: center;
    justify-content: flex-start;
    width: 100%;
    height: 100%;
    position: relative;
    overflow: scroll;
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
