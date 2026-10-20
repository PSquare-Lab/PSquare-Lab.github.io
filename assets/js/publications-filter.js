// Research-area / status / type filters and text search for the /publications/ page.
// Each entry rendered by _layouts/bib.liquid carries data-themes, data-status and data-kind.
(function () {
  "use strict";

  var root = document.getElementById("publications");
  if (!root) return;

  var list = root.querySelector(".pub-list");
  var searchInput = root.querySelector("#pub-q");
  var typeSelect = root.querySelector("#pub-type");
  var themeButtons = root.querySelectorAll("[data-theme-filter]");
  var statusButtons = root.querySelectorAll("[data-status-filter]");
  var cards = root.querySelectorAll("[data-theme-card]");
  var clearButtons = root.querySelectorAll(".pub-clear");
  var resultLabel = root.querySelector(".pub-result-label");
  var resultClear = root.querySelector(".pub-controls .pub-clear");
  var emptyState = root.querySelector(".pub-empty");
  var controls = root.querySelector(".pub-controls");

  var THEME_KEYS = ["all"];
  Array.prototype.forEach.call(root.querySelectorAll(".pub-option[data-theme-filter]"), function (option) {
    var key = option.getAttribute("data-theme-filter");
    if (THEME_KEYS.indexOf(key) < 0) THEME_KEYS.push(key);
  });

  var entries = Array.prototype.map.call(list.querySelectorAll(".pub-entry"), function (el) {
    var text = [".title", ".author", ".periodical"]
      .map(function (sel) {
        return Array.prototype.map
          .call(el.querySelectorAll(sel), function (node) {
            return node.textContent;
          })
          .join(" ");
      })
      .join(" ");
    return {
      li: el.closest("li") || el,
      themes: (el.getAttribute("data-themes") || "").split(/\s+/).filter(Boolean),
      status: el.getAttribute("data-status") || "",
      kind: el.getAttribute("data-kind") || "",
      // data-authors keeps every author searchable, including ones folded under "N more authors";
      // data-venue keeps the venue abbreviation searchable when a figure replaces the venue box.
      text: [text, el.getAttribute("data-authors") || "", el.getAttribute("data-venue") || "", el.getAttribute("data-year") || ""]
        .join(" ")
        .toLowerCase()
        .replace(/\s+/g, " "),
    };
  });

  var state = { theme: "all", status: "all", type: "all", q: "" };

  function themeLabel(key) {
    var option = root.querySelector('.pub-option[data-theme-filter="' + key + '"]');
    return option ? option.getAttribute("data-label") : "All areas";
  }

  function matches(entry, terms) {
    var themeOk = state.theme === "all" || entry.themes.indexOf(state.theme) >= 0;
    var statusOk = state.status === "all" || entry.status === state.status;
    var typeOk = state.type === "all" || entry.kind === state.type;
    var textOk = terms.every(function (t) {
      return entry.text.indexOf(t) >= 0;
    });
    return themeOk && statusOk && typeOk && textOk;
  }

  function render() {
    var terms = state.q.toLowerCase().split(/\s+/).filter(Boolean);
    var shown = 0;
    entries.forEach(function (entry) {
      var ok = matches(entry, terms);
      entry.li.hidden = !ok;
      if (ok) shown++;
    });

    // Hide year headings whose list has nothing left to show.
    Array.prototype.forEach.call(list.querySelectorAll("ol.bibliography"), function (ol) {
      var any = !!ol.querySelector(":scope > li:not([hidden])");
      ol.hidden = !any;
      var heading = ol.previousElementSibling;
      if (heading && heading.matches("h2.bibliography")) heading.hidden = !any;
    });
    // ...and whole sections (Preprints, Journals, ...) that end up empty.
    Array.prototype.forEach.call(list.querySelectorAll(".pub-group"), function (group) {
      group.hidden = !group.querySelector("ol.bibliography > li:not([hidden])");
    });

    Array.prototype.forEach.call(themeButtons, function (btn) {
      btn.setAttribute("aria-pressed", String(btn.getAttribute("data-theme-filter") === state.theme));
    });
    Array.prototype.forEach.call(statusButtons, function (btn) {
      btn.setAttribute("aria-pressed", String(btn.getAttribute("data-status-filter") === state.status));
    });
    Array.prototype.forEach.call(cards, function (card) {
      var active = card.getAttribute("data-theme-card") === state.theme;
      card.classList.toggle("is-active", active);
      var cta = card.querySelector(".pub-theme-cta");
      if (cta) cta.textContent = cta.getAttribute(active ? "data-active" : "data-idle");
    });
    if (typeSelect.value !== state.type) typeSelect.value = state.type;
    if (searchInput.value !== state.q) searchInput.value = state.q;

    var filtered = state.theme !== "all" || state.status !== "all" || state.type !== "all" || terms.length > 0;
    var statusText = { all: "", published: " · Published only", preprint: " · Preprints only" }[state.status];
    resultLabel.textContent = themeLabel(state.theme) + statusText;
    resultClear.hidden = !filtered;
    emptyState.hidden = shown > 0;

    var hash = state.theme === "all" ? "" : "#theme=" + state.theme;
    if (window.location.hash !== hash) {
      history.replaceState(null, "", window.location.pathname + window.location.search + hash);
    }
  }

  function setTheme(key, scroll) {
    state.theme = state.theme === key && key !== "all" ? "all" : key;
    render();
    if (scroll && controls) controls.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  Array.prototype.forEach.call(themeButtons, function (btn) {
    btn.addEventListener("click", function () {
      // Area tiles sit above the list, so bring the results into view.
      setTheme(btn.getAttribute("data-theme-filter"), btn.classList.contains("pub-theme-toggle"));
    });
  });
  Array.prototype.forEach.call(statusButtons, function (btn) {
    btn.addEventListener("click", function () {
      state.status = btn.getAttribute("data-status-filter");
      render();
    });
  });
  typeSelect.addEventListener("change", function () {
    state.type = typeSelect.value;
    render();
  });
  searchInput.addEventListener("input", function () {
    state.q = searchInput.value;
    render();
  });
  Array.prototype.forEach.call(clearButtons, function (btn) {
    btn.addEventListener("click", function () {
      state = { theme: "all", status: "all", type: "all", q: "" };
      render();
      searchInput.focus();
    });
  });

  var fromHash = /^#theme=([\w-]+)$/.exec(window.location.hash);
  if (fromHash && THEME_KEYS.indexOf(fromHash[1]) >= 0) state.theme = fromHash[1];
  render();
})();
