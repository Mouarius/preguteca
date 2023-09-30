import { createApp } from "vue";
import { VueQueryPlugin } from "@tanstack/vue-query";
import App from "./App.vue";
import axios from "axios";

const app = createApp(App);
export const axiosInstance = axios.create({
  baseURL: `api/`,
  headers: {
    "Content-Type": "application/json",
  },
});

app.use(VueQueryPlugin);
app.provide("axios", axiosInstance);

app.mount("#app");
