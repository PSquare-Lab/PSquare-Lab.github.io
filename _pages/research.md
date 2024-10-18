---
layout: page
permalink: /research/
title: Research
description: 
nav: true
nav_order: 6
---



<!-- <span style="color: #ff6600; font-size: 24px;">Selected Research Works</span> -->
My research interests lie in exploring solutions at the intersection of power systems, optimization, machine learning, and more recently, quantum computing, to address the challenges of modern energy networks, particularly under uncertainty. Below is a brief non-rigorous summary and the associated papers related to my three main research themes.


<span style="color: #ff6600; font-size: 20px;">#1 Closed-form Power Flow & Applications</span>

Closed-form power flow (CFPF) framework aim to provide **explicit** mathematical expressions for solving AC power flow equations: $$V = f(\mathbf{s})$$ (Node voltage as a function of injection vector). The core idea is to bypas iterative numerical techniques like Newton-Raphson and replace these with **function evaluation**. Unlike linearizations, CFPF is a general framework which allows to tailor complexity of $$f(\mathbf{s})$$ based on target application. Desired features of CFPF are:

- **Flexible Forms** $$\implies$$ Non-linear forms with *complexity-accuracy* trade-off
- **Easy to Evaluate Forms** $$\implies$$ Faster numerical calculations
- **Non-parametric Forms** $$\implies$$ Works within a power injection range or hypercube
- **Differentiability of Forms** $$\implies$$ Can be fed into optimization problems
- **Interpretability of Forms** $$\implies$$ Should provide insights into the physical system

The CFPF framework is build using **Gaussian Process** (GPs) to achieve these desired features. Beyond direct applications, **Vertex-Degree-Kernel** (VDK) design has been proposed for scaling the GPs to larger grid. Some key innovations involve designing a  **Network-Swipe Active Learning algorithm**, **Multi-Task VDK GP** and **Theoretical Learning Bounds for Risk Analysis**.

**Related Papers:** 
1) [Basic CFPF Frameworl](https://drive.google.com/file/d/1GfyVgx-ca9QEpgm7mg8yHzbKsYY3ifnE/view)
2) [Vertex-Degree Kernel and Network-Swipe Algorithm for Fast Risk Assessment](https://arxiv.org/abs/2308.07867)
3) [Multi-Task VDK GP for Network Contingencies](https://arxiv.org/abs/2310.00763)
4) [Critical Prosumer Identification](https://dr.ntu.edu.sg/bitstream/10356/170911/2/Locating%20Critical%20Prosumers%20in%20P2P%20Dominant%20Grids%20Using%20State-Sensitivity%20Function.pdf)
5) [Privacy-preserving Feasibility Assessment](https://www.researchgate.net/profile/Parikshit-Pareek-2/publication/358660003_Privacy-Preserving_Feasibility_Assessment_for_P2P_Energy_Trading_and_Storage_Integration/links/62207ee1e474e407ea1e1e6e/Privacy-Preserving-Feasibility-Assessment-for-P2P-Energy-Trading-and-Storage-Integration.pdf)


<span style="color: #ff6600; font-size: 20px;">#2 Optimal Power Flow (OPF) Proxies</span>

Details will be updated soon!

<span style="color: #ff6600; font-size: 20px;">#3 Potential Quantum Advantage Analysis in Power Systems</span>

Details will be updated soon!
