import { API_BASE_URL } from "./config";

export function dimmElement(el: HTMLElement | null) {
  if (!el) return;
  el.style.filter = "brightness(60%) grayscale(50%)";
}

export function undimmElement(el: HTMLElement | null) {
  if (!el) return;
  el.style.filter = "";
}

export const fetchApi = async <T>(url: string, options?: RequestInit): Promise<T> => {
  const response = await fetch(`${API_BASE_URL}/api${url}`, { method: "GET", headers: { "Content-Type": "application/json", ...options?.headers }, ...options });
  const data = await response.json();
  return data;
}

