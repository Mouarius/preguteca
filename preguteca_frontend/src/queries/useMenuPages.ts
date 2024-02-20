import { useQuery } from "@tanstack/vue-query";
import type { MenuPage } from "../types/index.ts";
import { fetchApi } from "../utils.ts";

async function fetchMenuPages() {
  return fetchApi<MenuPage[]>("/menu_pages");
}

export function useMenuPages() {
  return useQuery({
    queryKey: ["menu-page"],
    queryFn: fetchMenuPages,
  });
}
