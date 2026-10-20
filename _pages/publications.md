---
layout: page
permalink: /publications/
title: Publications
description: Our work spans three connected research areas. Choose an area below, or search by title, author, venue or year.
nav: true
nav_order: 3
---

<!-- _pages/publications.md -->
<!-- Areas live in _data/publication_themes.yml; each bib entry lists its keys in themes={...}. -->
<!-- Tiles: _includes/publication_theme_card.liquid. Paper rows: _layouts/bib.liquid. -->
<!-- Filtering and search: assets/js/publications-filter.js. Styles: _sass/_publications.scss. -->

<div class="publications pub-themed" id="publications">

<section class="pub-areas" aria-labelledby="pub-areas-heading">
  <div class="pub-areas-head">
    <h2 id="pub-areas-heading" class="pub-section-title">Research areas</h2>
    {%- if site.scholar_userid -%}
      <a class="pub-scholar" href="https://scholar.google.com/citations?user={{ site.scholar_userid }}" title="Google Scholar" aria-label="Google Scholar profile">
        <i class="ai ai-google-scholar" aria-hidden="true"></i>
      </a>
    {%- endif -%}
  </div>
  <div class="pub-area-grid">
    {%- for theme in site.data.publication_themes -%}
      {%- unless theme.wide -%}
        {% include publication_theme_card.liquid theme=theme %}
      {%- endunless -%}
    {%- endfor -%}
  </div>
  {%- for theme in site.data.publication_themes -%}
    {%- if theme.wide -%}
      {% include publication_theme_card.liquid theme=theme %}
    {%- endif -%}
  {%- endfor -%}
</section>

<section class="pub-controls" aria-label="Search and filter publications">
  <div class="pub-controls-row">
    <label for="pub-q" class="pub-control-label">Search</label>
    <input id="pub-q" type="search" placeholder="title, author, venue or year" autocomplete="off">
    <label for="pub-type" class="pub-control-label">Type</label>
    <select id="pub-type">
      <option value="all">all types</option>
      <option value="journal">journals &amp; A* conferences</option>
      <option value="conference">conferences &amp; workshops</option>
      <option value="magazine">magazine articles</option>
      <option value="thesis">theses</option>
    </select>
  </div>
  <div class="pub-filter-row" role="group" aria-label="Research area">
    <span class="pub-filter-name">Area:</span>
    <button type="button" class="pub-option" data-theme-filter="all" data-label="All areas" aria-pressed="true">all</button>
    {%- for theme in site.data.publication_themes -%}
      <span class="pub-sep" aria-hidden="true">/</span>
      <button type="button" class="pub-option" data-theme-filter="{{ theme.key }}" data-label="{{ theme.name }}" aria-pressed="false">{{ theme.label }}</button>
    {%- endfor -%}
  </div>
  <div class="pub-filter-row pub-filter-row-split">
    <div role="group" aria-label="Status">
      <span class="pub-filter-name">Status:</span>
      <button type="button" class="pub-option" data-status-filter="all" aria-pressed="true">all</button>
      <span class="pub-sep" aria-hidden="true">/</span>
      <button type="button" class="pub-option" data-status-filter="published" aria-pressed="false">published</button>
      <span class="pub-sep" aria-hidden="true">/</span>
      <button type="button" class="pub-option" data-status-filter="preprint" aria-pressed="false">preprints</button>
    </div>
    <button type="button" class="pub-clear" hidden>clear filters</button>
  </div>
  <p class="pub-result sr-only" aria-live="polite">Showing <span class="pub-result-label">All areas</span></p>
</section>

<div class="pub-list">
  <section class="pub-group" aria-labelledby="pub-group-preprints">
    <h2 id="pub-group-preprints" class="pub-group-title">Preprints</h2>
    {% bibliography --group_by none --query @*[keywords=submitted] %}
  </section>
  <section class="pub-group" aria-labelledby="pub-group-journals">
    <h2 id="pub-group-journals" class="pub-group-title">Journals &amp; A* Conferences</h2>
    {% bibliography --query @*[keywords=journal] %}
  </section>
  <section class="pub-group" aria-labelledby="pub-group-conferences">
    <h2 id="pub-group-conferences" class="pub-group-title">Conferences</h2>
    {% bibliography --query @*[keywords=conference] %}
  </section>
  <section class="pub-group" aria-labelledby="pub-group-other">
    <h2 id="pub-group-other" class="pub-group-title">Theses &amp; Articles</h2>
    {% bibliography --query @*[keywords=thesis||keywords=magazine] %}
  </section>
</div>

<div class="pub-empty" hidden>
  <p>No works match these filters.</p>
  <button type="button" class="pub-clear">clear filters</button>
</div>

</div>

<script defer src="{{ '/assets/js/publications-filter.js' | relative_url }}"></script>
