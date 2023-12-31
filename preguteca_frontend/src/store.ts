import { reactive } from "vue";
import { ActivePanel, TCategory } from "./types";


type Store = {
  isCategoryContainerVisible: boolean,
  activeCategory: TCategory | null,
  activePanel: ActivePanel
}

export const store = reactive<Store>({
  isCategoryContainerVisible: false,
  activeCategory: null,
  activePanel: "home",
});

export function toggleCategoryContainer() {
  return (store.isCategoryContainerVisible = !store.isCategoryContainerVisible);
}

export function updateActivePanel(panel: ActivePanel) {
  return store.activePanel = panel
}

export function updateActiveCategory(
  category: TCategory | null | undefined
): TCategory | null {
  if (!category) return (store.activeCategory = null);
  store.activeCategory = category;
  return store.activeCategory;
}
