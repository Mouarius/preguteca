import { reactive } from "vue";
import { ActivePanel, BaseCategory, MenuPage, TCategory } from "./types";

type Store = {
  isCategoryContainerVisible: boolean;
  activeCategory: string | null;
  activeMenuPage: MenuPage | null;
  activePanel: ActivePanel | null;
};

export const store = reactive<Store>({
  isCategoryContainerVisible: false,
  activeCategory: "el_mercado",
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
  name: string | null
) {
  store.activeCategory = name;
  window.location.hash = name ?? "";
}
