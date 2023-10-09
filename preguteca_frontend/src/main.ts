import { createApp } from "vue";
import { VueQueryPlugin } from "@tanstack/vue-query";
import App from "./App.vue";
import axios from "axios";
import { API_BASE_URL } from "./config";

const app = createApp(App);
export const axiosInstance = axios.create({
  baseURL: `${API_BASE_URL}api/`,
  headers: {
    "Content-Type": "application/json",
  },
});

app.use(VueQueryPlugin);
app.provide("axios", axiosInstance);

app.mount("#app");
