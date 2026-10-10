/* Viewer state only. The delivered SVG bytes and scientific content are not edited. */
"use strict";
for (const figure of document.querySelectorAll("[data-svg-viewer]")) {
  const viewport = figure.querySelector(".series-viewer");
  const image = viewport.querySelector("img");
  const controls = figure.querySelector("[data-viewer-controls]");
  const output = controls.querySelector("output");
  let zoom = 1;
  function update() {
    image.style.width = `${viewport.clientWidth * zoom}px`;
    output.value = `${Math.round(zoom * 100)}%（幅基準）`;
    controls.querySelector('[data-action="out"]').disabled = zoom <= 1;
    controls.querySelector('[data-action="in"]').disabled = zoom >= 8;
  }
  controls.addEventListener("click", event => {
    const button = event.target.closest("button[data-action]");
    if (!button) return;
    const oldZoom = zoom;
    const x = viewport.scrollLeft, y = viewport.scrollTop;
    zoom = button.dataset.action === "fit" ? 1 : Math.min(8, Math.max(1, zoom * (button.dataset.action === "in" ? 1.5 : 1 / 1.5)));
    update();
    viewport.scrollLeft = x * zoom / oldZoom;
    viewport.scrollTop = y * zoom / oldZoom;
  });
  image.addEventListener("error", () => {
    figure.querySelector("[data-image-error]").hidden = false;
    controls.hidden = true;
  });
  if (image.complete && image.naturalWidth === 0) {
    figure.querySelector("[data-image-error]").hidden = false;
  } else {
    controls.hidden = false;
    new ResizeObserver(update).observe(viewport);
    update();
  }
}
