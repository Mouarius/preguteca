import { axiosInstance } from "../main.ts";
import { useQuery } from "@tanstack/vue-query";

export const useCategory = (name: string) => {
  const axios = axiosInstance;
  const {
    isLoading,
    isError,
    data: category,
    error,
  } = useQuery({
    queryKey: ["category-list", name],
    queryFn: () => axios.get(`/categories/${name}`),
    select: (response) => response.data,
  });
  return {
    isLoading,
    isError,
    category,
    error,
  };
};
