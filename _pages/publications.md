---
layout: page
permalink: /publications/
title: Publications
description: List of Publications.
nav: true
nav_order: 2
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->
{% include bib_search.liquid %}

<div class="publications">

  <h3 style="font-weight: bold; color: #002691;">Submitted Papers</h3>
  <div class="submitted">
    {% bibliography --query @*[keywords=submitted] %}
  </div>

  <h3 style="font-weight: bold; color: #002691;">Journal Papers</h3>
  <div class="journal">
    {% bibliography --query @*[keywords=journal] %}
  </div>

  <h3 style="font-weight: bold; color: #002691;">Conference Papers</h3>
  <div class="conference">
    {% bibliography --query @*[keywords=conference] %}
  </div>

</div>
