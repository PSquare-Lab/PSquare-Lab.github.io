module.exports = {
  content: ["_site/**/*.html", "_site/**/*.js"],
  css: ["_site/assets/css/*.css"],
  output: "_site/assets/css/",
  skippedContentGlobs: ["_site/assets/**/*.html"],
  // Classes added at runtime by medium-zoom (loaded from a CDN, so not in _site) would otherwise be stripped.
  safelist: [/^medium-zoom/],
};
