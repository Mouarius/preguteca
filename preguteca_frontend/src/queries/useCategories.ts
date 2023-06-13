import {useQuery} from "@tanstack/vue-query";
import {axiosInstance} from "../main.ts";

export default () => {
    const axios = axiosInstance
    const {isLoading, isError, data: categories, error} =
        useQuery({
            queryKey: ["category-list"],
            queryFn: () => axios.get("/categories"),
            select: (response) => response.data
        })
    return {
        isLoading, isError, categories, error
    }
}
