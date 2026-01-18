---
layout: page
permalink: /research/
title: Research
description: AI + Optimization + Physics for Resilient Energy Grids
nav: true
nav_order: 6
---

At **$$\mathcal{P}^2$$-LAB**, we explore solutions at the intersection of power systems, optimization, and machine learning to address the challenges of modern energy networks. Our work focuses on developing "thoughtful AI"—physics-inspired methodologies that optimize and secure power system operations and planning under the volatility of decentralized, renewable-heavy grids.

---

### <span style="color: #ff6600; font-size: 20px;">#1 Foundational Models for EV-Rich Distribution Grids</span>

Traditional machine learning applications in power systems often suffer from "topology-dependence," requiring expensive retraining whenever the grid structure changes or new charging stations are added. We are shifting this paradigm by developing **Foundational Models for Power Systems** based on **Prior-Data Fitted Networks (PFNs)**. By leveraging a novel **Decoupled-Value Attention (DVA)** mechanism, our models perform **In-Context Learning**, allowing them to solve power flow and security problems for entirely new network configurations instantly, without any gradient updates. 

This foundational approach is the cornerstone of our onging work on **Secure EV-Rich Distribution Grid Operations** (supported by **ANRF PMECRG 2025-2028**). Here, we apply these generalizable surrogates to manage the stochastic volatility of high-penetration EV charging in unbalanced multiphase networks. By extending these models to handle the complexities of distribution grid physics, we aim to provide real-time stability and feasibility assessments for the evolving Indian prosumer landscape.

<div style="border-top: 1px solid #e0e0e0; margin-top: 15px; padding-top: 10px;">
  <strong>Related Materials:</strong> 
  <a href="https://arxiv.org/abs/2509.20950">[Decoupled-Value Attention for PFNs (2025)]</a> | 
  <a href="/assets/pdf/PFN_NITJ.pdf">[Bayesian Inference via PFNs (NITJ 2025)]</a> | 
</div>

---

### <span style="color: #ff6600; font-size: 20px;">#2 Optimal Power Flow (OPF): From Data-Efficiency to AC Feasibility</span>

While Optimal Power Flow (OPF) is the backbone of grid operations, its non-convex nature makes real-time implementation difficult. Our research seeks to bridge the gap between "fast" optimization and "physical" feasibility. We address the data-hunger of modern ML-solvers by using **Semi-Supervised Bayesian Neural Networks** that learn the underlying physical manifold of the grid from limited labeled data. This ensures that our **Optimization Proxies** (as presented at **ICML 2025**) remain accurate even when optimal training samples are scarce.

Beyond just speed, we focus on the **AC Feasibility** of dispatch decisions. This involves developing frameworks that ensure linear approximations (like DCOPF) do not lead to voltage or thermal violations in the actual AC network. This holistic view of optimization extends to the **TSO-DSO interface**, where we use convexification techniques to identify flexibility areas. This allows for the risk-averse integration of prosumers and storage into multimarket environments while ensuring that the physical limits of the grid are never compromised.

<div style="border-top: 1px solid #e0e0e0; margin-top: 15px; padding-top: 10px;">
  <strong>Related Materials:</strong> 
  <a href="https://arxiv.org/abs/2410.03085">[Data-Efficient Proxies (ICML 2025)]</a> | 
  <a href="https://arxiv.org/abs/2511.14725">[AC Feasibility of DCOPF (2025)]</a> | 
  <a href="https://doi.org/10.1109/TIA.2024.3481350">[Convexified Flexibility Area (IEEE TIA)]</a> | 
  <a href="https://doi.org/10.1016/j.energy.2024.133422">[Storage Participation (Energy 2024)]</a> |
  <a href="https://arxiv.org/abs/1911.12001">[Stability Constrained OPF (IEEE TCNS)]</a>
</div>

---

### <span style="color: #ff6600; font-size: 20px;">#3 Closed-form Surrogates & Network Sensitivity Analysis</span>

A core pillar of our work is the **Closed-form Power Flow (CFPF)** framework, which replaces iterative numerical solvers with explicit mathematical expressions: $$V = f(\mathbf{s})$$. By utilizing **Gaussian Processes** with specialized **Vertex-Degree Kernels (VDK)**, we turn the power grid into a differentiable function. This shift from numerical black-boxes to analytical surrogates allows us to scale probabilistic analysis to large-scale networks without the computational cost of traditional Monte Carlo simulations.

Once the grid is represented as a differentiable surrogate, we can perform advanced **Network Sensitivity Analysis**. This enables the **Network-Swipe Active Learning** algorithm to identify "worst-case" contingencies and critical voltage risks in seconds. Furthermore, these analytical forms provide explicit state-sensitivity functions that are instrumental in identifying critical prosumers and establishing privacy-preserving feasibility boundaries for Peer-to-Peer (P2P) energy trading.

<div style="border-top: 1px solid #e0e0e0; margin-top: 15px; padding-top: 10px;">
  <strong>Related Materials:</strong> 
  <a href="https://arxiv.org/abs/2308.07867">[VDK for Risk Assessment (2025)]</a> | 
  <a href="https://arxiv.org/abs/2310.00763">[Multi-Task GP for Contingencies (SEGAN 2025)]</a> | 
  <a href="https://doi.org/10.1109/TSG.2023.3323080">[Critical Prosumer Identification (IEEE TSG)]</a> | 
  <a href="https://arxiv.org/abs/2504.21260">[Multiphase Power Flow (PESGM 2025)]</a>|
  <a href="https://dr.ntu.edu.sg/handle/10356/164950">[PhD Thesis (NTU)]</a>
</div>

---

### <span style="color: #ff6600; font-size: 20px;">#4 Demystifying the Quantum Advantage in Power Systems</span>

Quantum computing offers a theoretical leap for grid problems, yet its practical utility remains a subject of intense scrutiny. We take a **realist’s approach** to this emerging field by investigating the scalability of quantum linear system solvers when applied to the non-linearities of power systems. By comparing fault-tolerant quantum algorithms against state-of-the-art classical sparse solvers, our work identifies the true crossover points where quantum speedups might actually be realized. Rather than following the hype, we aim to scrutinize and advance the boundaries of what is possible, ensuring that quantum research in our domain is grounded in rigorous complexity analysis and classical benchmarking.

<div style="border-top: 1px solid #e0e0e0; margin-top: 15px; padding-top: 10px;">
  <strong>Related Materials:</strong> 
  <a href="https://arxiv.org/abs/2402.08617">[Limitations of Quantum Solvers for Power Flow (IEEE TPWRS 2025)]</a> | 
</div>
