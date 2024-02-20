import { reactive } from "vue";
import { ActivePanel, MenuPage, TCategory } from "./types";

type Store = {
  isCategoryContainerVisible: boolean;
  activeCategory: TCategory | null;
  activeMenuPage: MenuPage | null;
  activePanel: ActivePanel | null;
};

export const store = reactive<Store>({
  isCategoryContainerVisible: false,
  activeCategory: null,
  activeMenuPage: null,
  activePanel: "home",
});

export function toggleCategoryContainer() {
  return (store.isCategoryContainerVisible = !store.isCategoryContainerVisible);
}

export function updateActivePanel(panel: ActivePanel | null) {
  if (store.activePanel === "category" && panel !== "category") {
    window.location.hash = "";
  }
  return (store.activePanel = panel);
}

export function updateActiveMenuPage(menuPage: MenuPage) {
  return (store.activeMenuPage = menuPage);
}

export function updateActiveCategory(
  category: TCategory | null | undefined
): TCategory | null {
  if (!category) return (store.activeCategory = null);
  store.activeCategory = category;
  window.location.hash = category.name;
  return store.activeCategory;
}
