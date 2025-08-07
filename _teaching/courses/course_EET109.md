---
title: "EET 109: Power and Energy Management I"
permalink: /teaching/course_EET109/
layout: page
status: current
---

##### <span style="color: #0faddd;; font-weight: bold;"> Course Information </span>

- **Semester:** Autumn Semester 2025  
- **Instructor:** Parikshit Pareek (email: pareek AT ee.iitr.ac.in)  
- **Lectures:**  Wed • 02:00 PM – 4:00 PM  (Main Lecture, @ AKB 504)
                 Wed • 10:00 AM – 11:00 AM  (Additional Lecture- When Needed @ AKB-301)
<!-- - **Venue:** EED 109 -->
- **Piazza:** [https://piazza.com/indian_institute_of_technology_roorkee/summer2025/eet109](https://piazza.com/indian_institute_of_technology_roorkee/summer2025/eet109)
<!-- - **TAs:** Rajdeep R. Dwivedi (rajdeep_rd AT ece.iitr.ac.in) -->

---

##### <span style="color: #0faddd;; font-weight: bold;"> 📌 Announcements </span>

- **2025‑08-07**: Assignment#1 is Annouced: Deadline 18th August 11AM. 
- **2025‑07-31**: Class room change for main and additional lectures. 
- **2025‑07‑23**: First Coding Quiz: Friday 11AM  Room EED 109. Team of Two, Bring Charged Laptops. -- Update (25th July) _Quiz & Assignment Material is Available on Piazza_
- **2025‑07‑23**: First handout released, Piazza link shared.
- **2025‑07‑12**: Course website launched.

---

##### <span style="color: #0faddd;; font-weight: bold;"> 🎯 Course Objectives </span>

This is not a traditional classroom-based course, nor is it a lab course focused on running experiments. This is a **TEC: Talent Enhancement Course**.

Designed for individuals who are already highly capable, this course aims to challenge your thinking and expand your potential. It will be largely hands-off in terms of direct implementation, encouraging independent exploration, creative problem-solving, and pushing beyond your current limits. Briefly, our objectives in this course are:

1. Develop a solid understanding of algorithms behind operations of power grid.  
2. Implement various power flow solvers on CPU and GPU with parallelization capabilities for speed & accuracy.
3. Explore advanced ML methods for power system operations.

---

##### <span style="color: #0faddd;; font-weight: bold;"> 📅 Course Content </span>

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
  {% assign eet109 = site.data.Courses.eet109_content %}

  <table>
    <thead>
      <tr>
        <th>Index</th>
        <th>Topic</th>
        <th>Material</th>
      </tr>
    </thead>
    <tbody>
      {% for lec in eet109 %}
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
          <a href="{{ lec.slides }}">PDF</a>
        {% else %}
          {{ lec.slides }}
        {% endif %}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>


---
##### <span style="color: #0faddd;; font-weight: bold;"> 📝 Assignments </span> 
- **Assignment #1** is due on **18th August,11AM**. Please read the instructions carefully—the required links are embedded within the PDF. Make sure to _explore all available resources_ and _troubleshoot thoroughly before reaching out to the instructor or TA_. [Assignment#1](/assets/pdf/EET109/Assignment_1.zip)
- **Python** and **Julia** are default programming languages for the course. You should use any of these for programming your assignments unless otherwise explicitly allowed.
- Submit via Moodle or GitHub—- as specified in each assignment. 
- **Viva** will accompany each assignment — your explanation during the viva carries significant weight in grading.
- **Honor Code:** Any cases of copying will be awarded a zero on the assignment. More severe penalties may follow.
- **Late submissions** will incur penalties, as annouced with assignment. 
- **Scrible Assigment** See introduction slides for details.

---

##### <span style="color: #0faddd;; font-weight: bold;"> 📚 References & Resources</span>

* Numerical Analysis, L. Ridgway Scott, Princeton University Press.
* Computational Methods for Electric Power Systems, Mariesa L. Crow, CRC Press.


---


##### <span style="color: #0faddd;; font-weight: bold;"> 🧾 Grading Policy (Tentative) </span>

* **PRS (50 Marks)**
  * Individual Coding Tasks
  * Assignments & Peer Discussions

* 💻 **Coding Tasks Breakdown (Part of PRS)**
  * **Coding Task 1**: DC Power Flow Approximation — * ~7 marks*
  * **Coding Task 1.1**: Fast Decoupled Load Flow — * ~5 marks*
  * **Coding Task 2**: Newton-Raphson Load Flow — * ~9 marks*
  * **Coding Task 3**: Economic Dispatch Modeling — * ~10 marks*
  * **Coding Task 4**: Gaussian Process for Power Flow — * ~9 marks*
  * Each task can be subdivided into several different tasks. 



🔔 **Note**: Further instructions, deadlines, and submission guidelines will be shared along with each task under the [Assignments](#📝-assignments) section.

* **PRE (50 Marks)**
  * Term Paper