import { useQuery } from "@tanstack/vue-query";
import { HomePage } from "../types/index.ts";
import { fetchApi } from "../utils.ts";

async function fetchHomePage() {
  const result = await fetchApi<HomePage[]>("/home_page");
  return result[0];
}

export function useHomePage() {
  return useQuery<HomePage, Error>({
    queryKey: ["home-page"],
    queryFn: fetchHomePage,
  });
}
