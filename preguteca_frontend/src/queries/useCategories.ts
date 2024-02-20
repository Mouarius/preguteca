import { useQuery } from "@tanstack/vue-query";
import { TCategory } from "../types";
import { fetchApi } from "../utils";
import { initialCategories } from "../data/initialCategories";

async function fetchCategories(): Promise<TCategory[]> {
  return fetchApi("/categories");
}

export function useCategories() {
  return useQuery({
    queryKey: ["category-list"],
    queryFn: fetchCategories,
    initialData: initialCategories,
  });
}
