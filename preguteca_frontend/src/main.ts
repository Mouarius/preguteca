import { createApp } from "vue";
import { VueQueryPlugin } from "@tanstack/vue-query";
import App from "./App.vue";
import axios from "axios";
import { BASE_URL } from "./settings";

const app = createApp(App);
export const axiosInstance = axios.create({
  baseURL: `${BASE_URL}api/`,
  headers: {
    "Content-Type": "application/json",
  },
});

app.use(VueQueryPlugin);
app.provide("axios", axiosInstance);

app.mount("#app");
