import { useQuery } from "@tanstack/vue-query";
import { BaseCategory } from "../types";
import { fetchApi } from "../utils";
import { initialCategories } from "../data/initialCategories";

async function fetchCategories(): Promise<BaseCategory[]> {
  return fetchApi("/categories");
}

export function useCategories() {
  return useQuery({
    queryKey: ["category-list"],
    queryFn: fetchCategories,
    refetchOnWindowFocus: false,
    staleTime: Infinity,
    placeholderData: initialCategories,
  });
}
