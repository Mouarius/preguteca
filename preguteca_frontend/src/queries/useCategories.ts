import { useQuery, UseQueryReturnType } from "@tanstack/vue-query";
import { axiosInstance as axios } from "../main.ts";
import { TCategory } from "../types";

function fetchCategories(): Promise<TCategory[]> {
  return axios.get("/categories").then((response) => response.data);
}

export function useCategories(): UseQueryReturnType<TCategory[], Error> {
  return useQuery({
    queryKey: ["category-list"],
    queryFn: fetchCategories,
  });
}
