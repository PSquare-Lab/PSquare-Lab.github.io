---
title: "EET 110: Power and Energy Management II"
permalink: /teaching/course_EET110/
layout: page
status: current
---

##### <span style="color: #0faddd;; font-weight: bold;"> Course Information </span>

- **Semester:** Spring Semester 2025  
- **Instructor:** Parikshit Pareek (email: pareek AT ee.iitr.ac.in)  
- **Lectures:** Tue • 09:00 AM – 11:00 AM; 05:00 PM – 07:00 PM  @ EED 109 
- **Venue:** EED 109
- **Piazza:** Same as EET 109 Course
<!-- [https://piazza.com/indian_institute_of_technology_roorkee/summer2025/eet109](https://piazza.com/indian_institute_of_technology_roorkee/summer2025/eet109) -->
- **TA:** Ayushi Jolotia(ayushi_j AT ee.iitr.ac.in)

---

##### <span style="color: #0faddd;; font-weight: bold;"> 📌 Announcements </span>

<!-- - **2025‑10-07**: Next round of _Term Paper_ presentations are on 15th and 17th October. 
- **2025‑09-26**: Assignment#3 is Annouced: Deadline 8th October 2 PM. 
- **2025‑08-29**: Assignment#2 is Annouced: Deadline 1st September 12 Noon. 
- **2025‑08-07**: Assignment#1 is Annouced: Deadline 18th August 11 AM. 
- **2025‑07-31**: Class room change for main and additional lectures. -->
- **2025‑02‑02**: The Term Paper timeline and deliverables are published in the final section of this webpage.
- **2026‑01‑20**: Term paper form is available on Piazza. Submission deadline: next Tuesday.
- **2025‑12‑10**: Initial Course website launched.

---

##### <span style="color: #0faddd;; font-weight: bold;"> 🎯 Course Objectives </span>

This is not a traditional classroom-based course, nor is it a lab course focused on running experiments. This is a **TEC: Talent Enhancement Course**, Part II.

Designed for individuals who are already highly capable, this course aims to challenge your thinking and expand your potential. It will be largely hands-off in terms of direct implementation, encouraging independent exploration, creative problem-solving, and pushing beyond your current limits. Briefly, our objectives in this course are:

1. Develop a solid understanding of optimization algorithms behind operations of power grid.  
2. Implement various optimal power flow methods on CPU and GPU with parallelization capabilities for speed & accuracy.
3. Explore advanced ML surrogates for Constrained Optimization Problem.


---

##### <span style="color: #0faddd;; font-weight: bold;">  Course Content </span>

<style>
.table-no-hover table {
  border-collapse: separate;
  border-spacing: 0;
  width: auto;                  /* Let table size adjust to content */
  table-layout: auto;          /* Use natural column widths */
}

.table-no-hover table th,
.table-no-hover table td {
  border-left: 1px solid #ccc; /* Vertical lines only */
  border-right: 1px solid #ccc;
  border-top: none;            /* No horizontal lines */
  border-bottom: none;
  text-align: center;
  vertical-align: middle;
  padding: 10px;
}

/* Optional: remove first/last borders for clean edges */
.table-no-hover table th:first-child,
.table-no-hover table td:first-child {
  border-left: none;
}
.table-no-hover table th:last-child,
.table-no-hover table td:last-child {
  border-right: none;
}

/* Header styling */
.table-no-hover table th {
  font-weight: bold;
}

/* Disable hover effects */
.table-no-hover table * {
  transition: none !important;
}

.table-no-hover table tr:hover,
.table-no-hover table td:hover,
.table-no-hover table th:hover {
  background: inherit !important;
  color: inherit !important;
  font-weight: inherit !important;
  transform: none !important;
  box-shadow: none !important;
  text-decoration: none !important;
}

</style>

<div class="table-no-hover">
  {% assign eet110 = site.data.Courses.eet_110_content %}

  <table>
    <thead>
      <tr>
        <th>Index</th>
        <th>Topics</th>
        <th>Slides</th>
        <th>Homeworks</th>
      </tr>
    </thead>
    <tbody>
      {% for lec in eet110 %}
      <tr>
        <td>
          {% if lec.lecture.size %}
            {% for num in lec.lecture %}
              {{ num }}{% if forloop.last == false %}, {% endif %}
            {% endfor %}
          {% else %}
            {{ lec.lecture }}
          {% endif %}
        </td>
        <td>{{ lec.topic }}</td>
        <td>{% if lec.slides contains "http" or lec.slides contains "/" %}
          <a href="{{ lec.slides }}">Slides</a>
        {% else %}
          {{ lec.slides }}
        {% endif %}</td>
        <td>{% if lec.homework contains "http" or lec.homework contains "/" %}
          <a href="{{ lec.homework }}">PDF</a>
        {% else %}
          {{ lec.homework }}
        {% endif %}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>


---
##### <span style="color: #0faddd;; font-weight: bold;"> 📝 Assignments </span> 
<!-- - **Assignment #3** is due on **8st October, 12 Noon**. Please read the instructions carefully—the required links are embedded within the PDF. Make sure to _explore all available resources_ and _troubleshoot thoroughly before reaching out to the instructor or TA_. [Assignment#3](/assets/pdf/EET109/Assignment_3.pdf)
- **Assignment #2** is due on **1st September, 12 Noon**. Please read the instructions carefully—the required links are embedded within the PDF. Make sure to _explore all available resources_ and _troubleshoot thoroughly before reaching out to the instructor or TA_. [Assignment#2](/assets/pdf/EET109/Assignment_2.zip)
- **Assignment #1** is due on **18th August,11 AM**. Please read the instructions carefully—the required links are embedded within the PDF. Make sure to _explore all available resources_ and _troubleshoot thoroughly before reaching out to the instructor or TA_. [Assignment#1](/assets/pdf/EET109/Assignment_1.zip) -->
- **Python** and **Julia** are default programming languages for the course. You should use any of these for programming your assignments unless otherwise explicitly allowed.
- Submit via Moodle or GitHub—- as specified in each assignment. 
- **Viva** will accompany each assignment — your explanation during the viva carries significant weight in grading.
- **Honor Code:** Any cases of copying will be awarded a zero on the assignment. More severe penalties may follow.
- **Late submissions** will incur penalties, as annouced with assignment. 
<!-- - **Scrible Assigment** See introduction slides for details. -->

---

##### <span style="color: #0faddd;; font-weight: bold;"> 📚 References & Resources</span>

> **Course Material:** There is **no required textbook** for this class. Slides will be shared.

**Reference Books:**
- **S. Boyd and L. Vandenberghe.** *Convex Optimization*. Cambridge University Press, 2004.
  - Available for free: [stanford.edu/~boyd/cvxbook/](http://stanford.edu/~boyd/cvxbook/)
- **H.P. Williams.** *Model Building in Mathematical Programming*, 5th Edition. Wiley, 2013.


---


##### <span style="color: #0faddd;; font-weight: bold;"> 🧾 Grading Policy (Tentative) </span>

- **CWS+PRE+PRS (50 Marks)**
  - Lab Assignments — 20 Marks
  - Term Paper / Project — 30 Marks
- **Mid Term (20 Marks)** — Exam
- **End Term (30 Marks)** — Exam

**Lab Assignments (Coding Tasks):**
- **Lab 1:** Linear Programming (Dispatch)
- **Lab 2:** MILP (Unit Commitment)
- **Lab 3:** NLP (AC-OPF)
- **Lab 4:** Relaxations (SOCP/SDP)
- **Lab 5:** Optimization Proxies


---


##### <span style="color: #0faddd;; font-weight: bold;"> 🧾 Term Paper Timeline and Deliverables </span>

| Week (Date) | Milestone | Requirement |
| :--- | :--- | :--- |
| Week 4 (Feb 10, 2026) | Proposal | 1-page abstract + Selected “Base Paper” |
| Week 8 (Mar 10, 2026) | Update | Mathematical formulation finalized (LaTeX) |
| Week 10 (Mar 24, 2026) | Code Check | Working code (in a notebook; will be made public) |
| Week 12 (Apr 7, 2026) | Final | Final report + 10-minute presentation |

---



##### <span style="color: #0faddd;; font-weight: bold;"> 🧾 Exam Papers</span> 

- [Quiz 1](/assets/pdf/EET110/Q1.pdf)
