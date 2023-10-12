<script setup lang="ts">
import HomePanelCard from './HomePanelCard.vue';
</script>
<template>
    <div class="container">
        <div class="header">
            <div class="header__section hearder__part--building">
                <div class="header__title">El Parlamento</div>
                <div class="separator separator--header"></div>
                <div class="header__subtitle">Edificio del mes</div>
            </div>
            <div class="header__section hearder__part--question">
                <div class="header__keywords">Separacion de poderes, democracia, representacion, libertad politica
                    colectiva...</div>
                <div class="separator separator--header"></div>
                <div class="header__subtitle">Palabras clave</div>
            </div>
        </div>
        <div class="subheader">
            <div class="subheader__section">
                <p class="subheader__general-questions"> uhqsdfqsd qfsd qsdf e f sdfqsdf qsdfqsd e fef jlksdfgsdf qsdgqsdg
                </p>
            </div>
            <div class="subheader__section">
                <div class="question-of-the-day">¿Has separacion de poderes en Espana? </div>
                <div class="separator separator--subheader"></div>
                <div class="subheader__subtitle">Question del dia</div>
            </div>

        </div>
        <div class="content">
            <HomePanelCard />
        </div>

    </div>
</template>
<style scoped>
.content {
    display: grid;
    grid-template-columns: 1fr;
    padding: 8px;
    gap: 8px;
}

@media screen and (min-width: 1000px) {
    .content {
        grid-template-columns: 1fr 1fr;
    }
}

.container {
    width: 100%;
    grid-area: aside;
    display: flex;
    flex-direction: column;
    font-family: 'Times New Roman', Times, serif;
    font-style: italic;
    border: solid 1px var(--border-color);

}

.header {
    padding: 8px;
    padding-left: 10px;
    min-height: 64px;
    padding-right: 12px;
    background: var(--white);
    color: var(--black);
    display: grid;
    grid-template-columns: 2fr 3fr;
}

.header__section {
    display: flex;
    align-items: end;
}

.separator {
    width: 0px;
    height: 100%;
    margin-left: 10px;
    margin-right: 10px;
    border: solid 1px black;
    transform: skewX(-15deg);
}

.separator--header {
    border: solid 1px black;
}

.separator--subheader {
    border: solid 1px var(--border-color);
}

.header__title {
    font-size: 24px;
    font-weight: 600;
    height: 100%;
}


.header__subtitle,
.subheader__subtitle {
    font-size: 14px;
}

.subheader__subtitle {
    color: var(--border-color);
    place-self: end;
}

.subheader {
    color: var(--border-color);
    background-color: var(--black);
    display: grid;
    grid-template-columns: 1fr 1fr;
    min-height: 64px;
    align-items: start;
    border-bottom: solid 1px var(--border-color);
}

.subheader__section {
    display: flex;
    padding: 8px;
    height: 100%;

}

.subheader__section:last-child {
    border-left: solid 1px var(--border-color);
}

.question-of-the-day {
    font-family: "Open Sans", Arial, Helvetica, sans-serif;
    font-weight: 600;
    font-style: normal;
}

.header__keywords {
    font-weight: 600;
    word-break: break-word;
    height: 100%;
}
</style>