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

  <h3 style="font-weight: bold; color: #ff6600;">Pre-Prints</h3>
  <div class="submitted">
    {% bibliography --query @*[keywords=submitted] %}
  </div>

  <h3 style="font-weight: bold; color: #ff6600;">Journal Papers</h3>
  <div class="journal">
    {% bibliography --query @*[keywords=journal] %}
  </div>

  <h3 style="font-weight: bold; color: #ff6600;">Conference Papers</h3>
  <div class="conference">
    {% bibliography --query @*[keywords=conference] %}
  </div>

</div>