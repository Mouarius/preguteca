import { createApp } from "vue";
import { VueQueryPlugin } from "@tanstack/vue-query";
import App from "./App.vue";
import VueDOMPurifyHTML from "vue-dompurify-html";

const app = createApp(App);

app.use(VueDOMPurifyHTML);
app.use(VueQueryPlugin);

app.mount("#app");
