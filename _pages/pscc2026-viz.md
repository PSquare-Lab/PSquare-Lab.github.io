---
layout: page
title: PSCC 2026 Cluster Map
permalink: /pscc2026-viz/
description: An interactive cluster map exploring the accepted papers of PSCC 2026.
nav: true
nav_order: 11
---

<p>
  Drag to pan, scroll to zoom, and use the search box to find a paper. Click a point to open its
  abstract, or open the visualization in its own tab for a distraction-free, full-screen view.
</p>

<p>
  All full papers can be found in the PSCC repository at
  <a href="https://pscc-central.epfl.ch/papers-repo" target="_blank" rel="noopener">pscc-central.epfl.ch/papers-repo</a>.
</p>

<p>
  <a href="{{ '/assets/PSCC2026_Viz/index.html' | relative_url }}" target="_blank" rel="noopener">
    Open full-screen &#8599;
  </a>
</p>

<style>
  .pscc-viz-frame-wrap {
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    width: 100vw;
    margin-top: 1rem;
  }
  .pscc-viz-frame {
    display: block;
    width: 100%;
    height: 82vh;
    min-height: 520px;
    border: 0;
  }
</style>

<div class="pscc-viz-frame-wrap">
  <iframe
    class="pscc-viz-frame"
    src="{{ '/assets/PSCC2026_Viz/index.html' | relative_url }}"
    title="PSCC 2026 Cluster Map"
    loading="lazy"
  ></iframe>
</div>
