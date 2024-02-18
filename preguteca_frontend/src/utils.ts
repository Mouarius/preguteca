export function dimmElement(el: HTMLElement | null) {
  if (!el) return;
  el.style.filter = "brightness(60%) grayscale(50%)";
}

export function undimmElement(el: HTMLElement | null) {
  if (!el) return;
  el.style.filter = "";
}
