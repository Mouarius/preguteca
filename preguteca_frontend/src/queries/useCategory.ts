import { useQuery } from "@tanstack/vue-query";
import { fetchApi } from "../utils.ts";
import { TCategory } from "../types/index.ts";
import { store } from "../store.ts";

export const useCategory = () => {
  const {
    isLoading,
    isError,
    isSuccess,
    data: category,
    error,
  } = useQuery({
    queryKey: ["category-list", store.activeCategory],
    queryFn: () => fetchApi<TCategory>(`/categories/${store.activeCategory}`),
    refetchOnWindowFocus: false,
    staleTime: Infinity,
  });
  return {
    isLoading,
    isSuccess,
    isError,
    category,
    error,
  };
};
