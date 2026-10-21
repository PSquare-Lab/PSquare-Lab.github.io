// Initialize medium zoom.
$(document).ready(function () {
  // Overlay colour = the theme background at 93% opacity. The CSS variable can be minified to a
  // 3-digit hex (e.g. #fff), where appending "ee" gives an invalid colour and a see-through overlay,
  // so let the browser resolve it to rgb() first.
  var probe = document.createElement("span");
  probe.style.backgroundColor = "var(--global-bg-color)";
  document.body.appendChild(probe);
  var rgb = (getComputedStyle(probe).backgroundColor.match(/\d+(\.\d+)?/g) || ["255", "255", "255"]).slice(0, 3);
  probe.remove();
  medium_zoom = mediumZoom("[data-zoomable]", {
    background: "rgba(" + rgb.join(", ") + ", 0.93)",
    margin: 24, // keep the zoomed image clear of the window edges
  });
});
