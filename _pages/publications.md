---
layout: page
permalink: /publications/
title: Publications
description: A simple list of publications, arranged chronologically within each section.
nav: true
nav_order: 3
---

<!-- _pages/publications.md -->
<!-- Bibsearch Feature -->
<!-- {% include bib_search.liquid %} -->

<div class="publications">

  <h3 style="font-weight: bold; color: #ff6600;">Pre-Prints</h3>
  <div class="submitted">
    {% bibliography --query @*[keywords=submitted] %}
  </div>

  <h3 style="font-weight: bold; color: #ff6600;">Journal Papers & A* Conferences</h3>
  <div class="journal">
    {% bibliography --query @*[keywords=journal] %}
  </div>

  <h3 style="font-weight: bold; color: #ff6600;">Conference Papers</h3>
  <div class="conference">
    {% bibliography --query @*[keywords=conference] %}
  </div>

  <h3 style="font-weight: bold; color: #ff6600;">Thesis</h3>
  <div class="thesis">
    {% bibliography --query @*[keywords=thesis] %}
  </div>

</div>
