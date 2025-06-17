---
layout: page
permalink: /Team/
title: Team
page_title: Team
description: 
nav: true
nav_order: 7
---

<!-- Lab Logo + PI Info Side by Side -->
<div style="display: flex; align-items: center; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-bottom: 2rem;">
  <!-- Lab Logo -->
  <!-- <div>
    <img src="{{ '/assets/img/Lab_Logo.jpg' | relative_url }}" alt="Lab Logo" style="width: 180px;" />
  </div> -->
  
  <!-- PI Info -->
  <div style="display: flex; align-items: center; gap: 1rem;">
    <img src="{{ '/assets/img/parikshit_zoomed.jpg' | relative_url }}" alt="Parikshit Pareek" style="width: 120px; border-radius: 50%;" />
    <div>
      <h3 style="margin: 0;"><a href="https://psquare-lab.github.io" style="text-decoration: none;">Parikshit Pareek</a></h3>
      <p style="margin: 0;">Principal Investigator<br>Assistant Professor, Electrical Engineering<br>Indian Institute of Technology Roorkee</p>
    </div>
  </div>
</div>

#### ⚡ Current Members

{% assign category_order = "Research Scholars|Masters Researchers|Undergraduate Researchers|Summer Interns" | split: "|" %}
{% assign current_members = "" | split: "" %}
{% for cat in category_order %}
  {% assign members = site.data.team | where: "category", cat | where: "status", "current" %}
  {% assign current_members = current_members | concat: members %}
{% endfor %}

<div style="display: flex; flex-wrap: wrap; gap: 1rem; margin-bottom: 2rem;">
  {% for member in current_members %}
    <div style="display: flex; align-items: center; gap: 1rem; flex: 1 1 35%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 8px;">
      <img src="{{ '/assets/img/' | append: member.image | relative_url }}"
           alt="{{ member.name }}"
           style="width: 120px; height: 120px; object-fit: cover; border-radius: 50%; transition: transform 0.3s ease;"
           onmouseover="this.style.transform='scale(1)'"
           onmouseout="this.style.transform='scale(1)'"
           onerror="this.onerror=null; this.src='{{ '/assets/img/Lab_Logo.jpg' | relative_url }}';" />
      <div>
        <h4 style="margin: 0;">
          {% if member.url %}
            <a href="{{ member.url }}" target="_blank">{{ member.name }}</a>
          {% elsif member.github %}
            <a href="{{ member.github }}" target="_blank">{{ member.name }}</a>
          {% else %}
            {{ member.name }}
          {% endif %}
        </h4>
        {% if member.degree %}
          <p style="margin: 0;"><em>{{ member.degree }}</em></p>
        {% endif %}
        <p style="margin: 0;"><strong>{{ member.role }}</strong></p>
        <p style="margin: 0;">{{ member.description }}</p>
        {% if member.note %}
          <p style="margin: 0; font-style: italic;">{{ member.note }}</p>
        {% endif %}
      </div>
    </div>
  {% endfor %}
</div>

<!-- Wrapper to align everything to the left -->
<div style="max-width: 1300px; margin: 0 auto 2rem auto; padding-left: 1rem; text-align: left;">

#### 🏁 Past Team
<ul style="list-style-type: disc; padding-left: 1.5rem;">
  {% assign past_members = "" | split: "" %}
  {% for cat in category_order %}
    {% assign members = site.data.team | where: "category", cat | where: "status", "past" %}
    {% assign past_members = past_members | concat: members %}
  {% endfor %}

  {% for member in past_members %}
    <li style="margin-bottom: 0.75rem;">
      {% if member.url %}
        <a href="{{ member.url }}" target="_blank">{{ member.name }}</a>
      {% elsif member.github %}
        <a href="{{ member.github }}" target="_blank">{{ member.name }}</a>
      {% else %}
        {{ member.name }}
      {% endif %}
      — {{ member.role }}
      {% if member.degree %} | {{ member.degree }}{% endif %}
      {% if member.period %} | {{ member.period }}{% endif %}
      {% if member.now %} | Now: {{ member.now }}{% endif %}
    </li>
  {% endfor %}
</ul>

#### 🤝 Collaborators
<ul style="list-style-type: disc; padding-left: 1.5rem;">
  <li style="margin-bottom: 0.75rem;"><a href="https://sidhantmisra.github.io" target="_blank">Dr. Sidhant Misra</a> — Staff Scientist, Theoretical Division T-5 (Applied Mathematics), Los Alamos National Laboratory, USA</li>
  <li style="margin-bottom: 0.75rem;"><a href="https://energy.mit.edu/profile/deepjyoti-deka/" target="_blank">Dr. Deepjyoti Deka</a> — Research Scientist, MIT Energy Initiative, USA</li>
  <li style="margin-bottom: 0.75rem;"><a href="https://biryani.github.io" target="_blank">Dr. Abhijth Jayakumar</a> — Staff Scientist, Theoretical Division T-5 (Applied Mathematics), Los Alamos National Laboratory, USA</li>
  <li style="margin-bottom: 0.75rem;"><a href="https://sites.google.com/view/vishvendra" target="_blank">Prof. Vishvendra Punia</a> — Associate Professor, Electronics and Communication Engineering, IIT Roorkee</li>
  <li style="margin-bottom: 0.75rem;"><a href="https://molzahn.github.io" target="_blank">Prof. Daniel K. Molzahn</a> — Associate Professor, Electrical and Computer Engineering, Georgia Tech, USA</li>
  <li style="margin-bottom: 0.75rem;"><a href="https://public.lanl.gov/rbent/" target="_blank">Dr. Russell Bent</a> — Staff Scientist, Theoretical Division T-5 (Applied Mathematics), Los Alamos National Laboratory, USA</li>
  <li style="margin-bottom: 0.75rem;"><a href="https://abudhabi.iitd.ac.in/averma" target="_blank">Prof. Ashu Verma</a> — Professor, Energy Science and Engineering, IIT Delhi</li>
</ul>

#### 🛰️ External Mentees
<ul style="list-style-type: disc; padding-left: 1.5rem;">
  <li style="margin-bottom: 0.75rem;"><a href="#" target="_blank">Sonam Gupta</a> — Research Scholar, Energy Science and Engineering, IIT Delhi, India</li>
  <li style="margin-bottom: 0.75rem;"><a href="#" target="_blank">Michael A. Boateng</a> — Research Scholar, Electrical and Computer Engineering, Georgia Tech, USA</li>
</ul>

</div>
