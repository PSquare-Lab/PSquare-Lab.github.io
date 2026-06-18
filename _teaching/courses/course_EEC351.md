---
title: "EEC 351: Fundamentals of AI/ML"
permalink: /teaching/course_EEC351/
layout: page
status: current
description: "Autumn 2026-27 · Department of Electrical Engineering, IIT Roorkee"
semester: "Autumn 2026-27"
nav: false
---

<style>
.course-hero { display: flex; flex-wrap: wrap; gap: 10px; margin: 0.2rem 0 1.6rem; }
.quick-link {
  font-size: 0.85rem; font-weight: 500; color: var(--global-theme-color);
  border: 1px solid var(--global-divider-color); border-radius: 999px;
  padding: 5px 14px; text-decoration: none; transition: background 0.15s ease;
}
.quick-link:hover { background: rgba(14, 116, 144, 0.10); text-decoration: none; }

.course-section {
  color: var(--global-theme-color); font-weight: 600; font-size: 1.18rem;
  margin: 2.4rem 0 1rem; padding-bottom: 0.45rem;
  border-bottom: 2px solid var(--global-divider-color);
}

.course-meta { display: grid; grid-template-columns: max-content 1fr; gap: 0.5rem 1.4rem; margin: 0; }
.course-meta .k { color: var(--global-text-color-light); font-weight: 600; }
.course-meta .v { color: var(--global-text-color); }

.course-note {
  background: var(--global-card-bg-color); border: 1px solid var(--global-divider-color);
  border-left: 3px solid var(--global-theme-color); border-radius: 6px;
  padding: 0.75rem 1rem; margin: 0.9rem 0; font-size: 0.95rem;
}

.table-no-hover table { border-collapse: separate; border-spacing: 0; width: 100%; table-layout: fixed; }
.table-no-hover table th, .table-no-hover table td {
  border: 1px solid var(--global-divider-color); text-align: center; vertical-align: middle; padding: 8px;
}
.table-no-hover table th { font-weight: 600; }
.table-no-hover table th:nth-child(1), .table-no-hover table td:nth-child(1) { width: 5%; }
.table-no-hover table th:nth-child(2), .table-no-hover table td:nth-child(2) { width: 21%; }
.table-no-hover table th:nth-child(3), .table-no-hover table td:nth-child(3) { width: 9%; }
.table-no-hover table th:nth-child(4), .table-no-hover table td:nth-child(4) { width: 29%; }
.table-no-hover table th:nth-child(5), .table-no-hover table td:nth-child(5) { width: 27%; }
.table-no-hover table th:nth-child(6), .table-no-hover table td:nth-child(6) { width: 9%; }
.table-no-hover table * { transition: none !important; }
.table-no-hover table tr:hover, .table-no-hover table td:hover, .table-no-hover table th:hover {
  background: inherit !important; color: inherit !important; font-weight: inherit !important;
  transform: none !important; box-shadow: none !important; text-decoration: none !important;
}
</style>

<div class="course-hero">
  <a class="quick-link" href="/teaching/course_EEC351_2025/">Previous offering · Autumn 2025-26</a>
</div>

<h4 class="course-section">Course information</h4>

<div class="course-meta">
  <span class="k">Semester</span><span class="v">Autumn 2026–27</span>
  <span class="k">Instructor</span><span class="v">Parikshit Pareek · pareek [at] ee.iitr.ac.in</span>
  <span class="k">Lectures</span><span class="v">TBA</span>
  <span class="k">Office hours</span><span class="v">TBA · 214A, EE</span>
  <span class="k">Piazza</span><span class="v">TBA</span>
  <span class="k">Teaching assistant</span><span class="v">TBA</span>
</div>

<h4 class="course-section">Announcements</h4>

- **2026‑06‑18** — Course website for the Autumn 2026-27 offering is live. Announcements are posted here regularly; email is sent **only** when something is urgent.

<h4 class="course-section">Course objectives</h4>

- Comprehend the historical evolution and foundational concepts of AI/ML.
- Build mathematical intuition for machine-learning principles.
- Explore core theoretical frameworks and evaluation strategies.

<h4 class="course-section">Course content</h4>

<div class="table-no-hover">
{% assign lectures = site.data.Courses.eec351_content %}
<table>
  <thead>
    <tr>
      <th>#</th>
      <th>Topic</th>
      <th>Slides</th>
      <th>Essential reading</th>
      <th>Additional</th>
      <th>Homework</th>
    </tr>
  </thead>
  <tbody>
    {% for lec in lectures %}
    <tr>
      <td>{% for num in lec.lecture %}{{ num }}{% unless forloop.last %}, {% endunless %}{% endfor %}</td>
      <td>{{ lec.topic }}</td>
      <td>{% if lec.slides contains "http" or lec.slides contains "/" %}<a href="{{ lec.slides }}">Slides</a>{% else %}{{ lec.slides }}{% endif %}</td>
      <td>{% if lec.essential %}{% for item in lec.essential %}<a href="{{ item.link }}">{{ item.text }}</a>{% unless forloop.last %}, {% endunless %}{% endfor %}{% else %}--{% endif %}</td>
      <td>{% if lec.additional %}{% for item in lec.additional %}<a href="{{ item.link }}">{{ item.text }}</a>{% unless forloop.last %}, {% endunless %}{% endfor %}{% else %}--{% endif %}</td>
      <td>{% if lec.homework contains "https" or lec.homework contains "/" %}<a href="{{ lec.homework }}">HW</a>{% else %}{{ lec.homework }}{% endif %}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
</div>

{% unless lectures and lectures.size > 0 %}
<div class="course-note">The weekly schedule will appear here as the term begins. Material from the previous run is on the <a href="/teaching/course_EEC351_2025/">Autumn 2025-26 page</a>.</div>
{% endunless %}

<h4 class="course-section">Assignments</h4>

- Assignments will be posted here as they are released. _TBA._
- **Python** is the default programming language for the course; use it unless a task explicitly allows otherwise.
- Submit via Moodle, Google Form, or GitHub — as specified in each assignment.
- **Honor code:** any copying earns a zero on the assignment; more severe penalties may follow.
- **Late submissions** incur penalties as announced with each assignment.

<h4 class="course-section">References & resources</h4>

**Recommended texts**

- *Probabilistic Machine Learning: An Introduction* — Kevin Murphy, MIT Press, 2022/2023.
- *Learning from Data: A Short Course* — Yaser S. Abu-Mostafa, Malik Magdon-Ismail & Hsuan-Tien Lin, AMLBook, 2017.

**Supplementary**

- Coursera ML (Andrew Ng)
- Relevant paper links shared on Piazza

<h4 class="course-section">Grading policy</h4>

- **CWS — 30 marks:** announced & surprise quizzes; assignments & peer discussions.
- **MTE — 30 marks:** written exam (any format).
- **ETE — 40 marks:** written exam (any format).

<h4 class="course-section">Exam papers</h4>

- Papers for this offering will be posted here after the exams. _TBA._
- Past papers: see the [Autumn 2025-26 offering](/teaching/course_EEC351_2025/).
