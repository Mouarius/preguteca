import { useQuery } from "@tanstack/vue-query";
import { fetchApi } from "../utils.ts";
import { initialCategories } from "../data/initialCategories.ts";

export const useCategory = (name: string) => {
  const {
    isLoading,
    isError,
    data: category,
    error,
  } = useQuery({
    queryKey: ["category-list", name],
    queryFn: () => fetchApi(`/categories/${name}`),
    initialData: initialCategories,
  });
  return {
    isLoading,
    isError,
    category,
    error,
  };
};
