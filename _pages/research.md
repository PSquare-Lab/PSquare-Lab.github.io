---
layout: page
permalink: /research/
title: Research
description: AI + Optimization + Physics for Resilient Energy Grids
nav: true
nav_order: 6
---

<!-- _pages/research.md -->
<!-- One card per research area, in the same order as _data/publication_themes.yml; paper counts come from the bib's themes={...}. -->
<!-- Animated figures: _includes/research_figure_*.liquid. Styles and animations: _sass/_research.scss. -->

<div class="research-page">
  <p class="research-intro">
    At P²-LAB we work where power systems, optimization and machine learning meet. Our aim is thoughtful AI: physics-inspired methods that keep
    grid operation and planning secure as networks turn decentralised and renewable-heavy.
  </p>

  <p class="research-jump">
    <span class="research-jump-label">Areas:</span>
    <a href="#sdfm">structured-data FMs</a>
    <span class="research-jump-sep" aria-hidden="true">/</span>
    <a href="#aips">AI for power systems</a>
    <span class="research-jump-sep" aria-hidden="true">/</span>
    <a href="#l4o">learning for optimization</a>
    <span class="research-jump-sep" aria-hidden="true">/</span>
    <a href="#other">power systems &amp; other</a>
  </p>

  <section id="sdfm" class="research-area">
    <div class="research-area-head">
      <h2 class="research-area-name">Structured-Data Foundation Models</h2>
      <span class="research-area-count">{% bibliography_count --query @*[themes~=sdfm] %} papers</span>
    </div>
    <div class="research-area-body">
      {% include research_figure_sdfm.liquid %}
      <div class="research-text">
        <p>
          Prior-data fitted networks that learn in context. With Decoupled-Value Attention, one pretrained model solves power flow on network
          configurations it has never seen — no retraining, no gradient updates — and the same idea carries to tabular science beyond the grid.
        </p>
        <p class="research-note">Supported by ANRF PMECRG 2025–2028.</p>
        <div class="research-papers">
          <span class="research-papers-label">Selected papers</span>
          <ul>
            <li>
              <a href="https://arxiv.org/abs/2509.20950">Decoupled-Value Attention for Prior-Data Fitted Networks: GP Inference for Physical Equations</a>
              <em class="research-venue">arXiv, 2025</em>
            </li>
            <li>
              <a href="https://arxiv.org/abs/2607.12241">Gradient-Free Topology Adaptation for Power Flow Surrogates via In-Context Whitening</a>
              <em class="research-venue">arXiv, 2026</em>
            </li>
            <li>
              <a href="https://arxiv.org/abs/2601.21731">Mechanistic Evidence for Spectral Structures in Prior-Data Fitted Networks</a>
              <em class="research-venue">arXiv, 2026</em>
            </li>
          </ul>
        </div>
        <a class="research-more" href="{{ '/publications/' | relative_url }}#theme=sdfm">show all papers in this area ›</a>
      </div>
    </div>
  </section>

  <section id="aips" class="research-area">
    <div class="research-area-head">
      <h2 class="research-area-name">AI for Power Systems</h2>
      <span class="research-area-count">{% bibliography_count --query @*[themes~=aips] %} papers</span>
    </div>
    <div class="research-area-body">
      {% include research_figure_aips.liquid %}
      <div class="research-text">
        <p>
          Gaussian-process surrogates that turn power flow into a closed-form, differentiable map, V = f(s). From it come probabilistic voltage
          envelopes, contingency screening in seconds and guarantees on voltage risk — without Monte Carlo.
        </p>
        <div class="research-papers">
          <span class="research-papers-label">Selected papers</span>
          <ul>
            <li>
              <a href="https://doi.org/10.1016/j.epsr.2026.113619">Learning Power Flow with Confidence: A Probabilistic Guarantee Framework for Voltage Risk</a>
              <em class="research-venue">Electric Power Systems Research, 2027</em>
            </li>
            <li>
              <a href="https://doi.org/10.1016/j.apenergy.2025.126995">Gaussian Processes in Power Systems: Techniques, Applications, and Future Works</a>
              <em class="research-venue">Applied Energy, 2026</em>
            </li>
            <li>
              <a href="https://doi.org/10.1109/TSTE.2021.3116544">A Framework for Analytical Power Flow Solution Using Gaussian Process Learning</a>
              <em class="research-venue">IEEE Trans. Sustainable Energy, 2022</em>
            </li>
          </ul>
        </div>
        <a class="research-more" href="{{ '/publications/' | relative_url }}#theme=aips">show all papers in this area ›</a>
      </div>
    </div>
  </section>

  <section id="l4o" class="research-area">
    <div class="research-area-head">
      <h2 class="research-area-name">Learning for Optimization</h2>
      <span class="research-area-count">{% bibliography_count --query @*[themes~=l4o] %} papers</span>
    </div>
    <div class="research-area-body">
      {% include research_figure_l4o.liquid %}
      <div class="research-text">
        <p>
          Learned optimization proxies that return near-optimal, physically feasible dispatch from only a few labelled solves — and language models
          that write hard MILP instances and tune hyperparameters themselves.
        </p>
        <div class="research-papers">
          <span class="research-papers-label">Selected papers</span>
          <ul>
            <li>
              <a href="https://arxiv.org/abs/2410.03085"
                >Optimization Proxies using Limited Labeled Data and Training Time — A Semi-Supervised Bayesian Neural Network Approach</a
              >
              <em class="research-venue">ICML, 2025</em>
            </li>
            <li>
              <a href="https://arxiv.org/abs/2609.37356">Teaching LLMs to Generate Challenging MILP Instances via Solver Feedback</a>
              <em class="research-venue">arXiv, 2026</em>
            </li>
            <li>
              <a href="https://openreview.net/forum?id=FMF0oUvNYP">Small LLMs with Expert Blocks Are Good Enough for Hyperparameter Tuning</a>
              <em class="research-venue">ICLR Workshop, 2026</em>
            </li>
          </ul>
        </div>
        <a class="research-more" href="{{ '/publications/' | relative_url }}#theme=l4o">show all papers in this area ›</a>
      </div>
    </div>
  </section>

  <section id="other" class="research-area research-area-wide">
    {% include research_figure_other.liquid %}
    <div class="research-wide-main">
      <h2 class="research-area-name">Power Systems &amp; Other Works</h2>
      <p>Optimal power flow and AC feasibility, small-signal stability, TSO–DSO flexibility and storage, and a realist’s look at quantum power flow.</p>
    </div>
    <div class="research-wide-side">
      <p>
        <span>Recent:</span>
        <a href="https://doi.org/10.1109/TPWRS.2025.3613139">Limitations of Fault-Tolerant Quantum Linear System Solvers for Quantum Power Flow</a>;
        <a href="https://doi.org/10.1016/j.epsr.2026.113652">Towards AC Feasibility of DCOPF Dispatch</a>;
        <a href="https://doi.org/10.1109/TIA.2024.3481350">Convexified Flexibility Area Identification at TSO–DSO Interface</a>
      </p>
      <a class="research-more" href="{{ '/publications/' | relative_url }}#theme=other"
        >show all {% bibliography_count --query @*[themes~=other] %} papers ›</a
      >
    </div>
  </section>
</div>
