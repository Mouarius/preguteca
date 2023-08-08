import {reactive} from "vue"
import { TCategory } from "./types"

export const store = reactive({
    activeCategory: null as TCategory | null
})

export function updateActiveCategory(category: TCategory):TCategory | null{
    if (!category) return null;
    store.activeCategory = category
    return store.activeCategory
}