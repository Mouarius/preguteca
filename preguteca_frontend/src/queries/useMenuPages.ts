import { useQuery } from "@tanstack/vue-query";
import { axiosInstance as axios } from "../main.ts";
import type { MenuPage } from "../types/index.ts";

async function fetchMenuPages() {
  return axios
    .get("/menu_pages")
    .then((response) => response.data as MenuPage[]);
}

export function useMenuPages() {
  return useQuery({
    queryKey: ["menu-page"],
    queryFn: fetchMenuPages,
  });
}
