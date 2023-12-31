import { useQuery } from "@tanstack/vue-query";
import { axiosInstance as axios } from "../main.ts";
import type { MenuPage } from "../types/index.ts";

async function fetchMenuPage() {
  return axios
    .get("/pages")
    .then((response) => response.data as MenuPage[]);
}

export function useMenuPage() {
  return useQuery<MenuPage[], Error>({
    queryKey: ["menu-page"],
    queryFn: fetchMenuPage,
  });
}
