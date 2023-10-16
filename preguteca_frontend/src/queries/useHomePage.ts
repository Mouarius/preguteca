import { useQuery, UseQueryReturnType } from "@tanstack/vue-query";
import { axiosInstance as axios } from "../main.ts";
import { HomePage } from "../types/index.ts";

function fetchHomePage() {
  return axios
    .get("/home_page")
    .then((response) => response.data[0] as HomePage);
}

export function useHomePage() {
  return useQuery<HomePage, Error>({
    queryKey: ["home-page"],
    queryFn: fetchHomePage,
  });
}
