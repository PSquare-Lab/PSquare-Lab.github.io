---
title: "EEC 351: Fundamentals of AI/ML"
permalink: /teaching/course_EEC351_2025/
layout: page
status: past
description: "Archived course page — Autumn Semester 2025-2026 offering"
semester: "Autumn 2025-26"
nav: false
---

> This is the **archived page for the Autumn 2025-26 offering**. For the current offering, see [EEC 351: Fundamentals of AI/ML](/teaching/course_EEC351/).


<h4 class="course-section">Course Information</h4>


- **Semester:** Autumn Semester 2025-2026  
- **Instructor:** Parikshit Pareek (email: pareek AT ee.iitr.ac.in)  
- **Lectures:** Thu • 03:00–03:55 PM;  Fri • 4:05–5:00 PM; (Venue: GB205)
- **Office Hours:** Tue • 4:05–5:00 PM;  (Venue: 214A, EE)
- **Piazza:** [https://piazza.com/indian_institute_of_technology_roorkee/fall2025/eec351](https://piazza.com/indian_institute_of_technology_roorkee/fall2025/eec351)
- **TA:** Rajdeep R. Dwivedi (email: rajdeep_rd AT ece.iitr.ac.in)


---

<h4 class="course-section">Announcements</h4>
- **2025‑09-26**: **Assignment #1** is due on **Thursday, 9th October, 5 PM**.
- **2025‑08-22**: Additional Class on 26th August, Wednesday.
- **2025‑07‑13**: Course Announcements will be posted here regularly. Email notifications will **only** be sent if information is urgent.
<!-- - **2025‑07‑01**: Course Announcements will be posted here regularly. Email notifications will **only** be sent if information is urgent. -->
<!-- - **2025‑06‑20**: First assignment released! Due July 1. Check the Assignments section below. -->
- **2025‑07‑12**: Course website launched.


---

<h4 class="course-section">Course Objectives</h4>

- Comprehend the historical evolution and foundational concepts of AI/ML. 
- Build mathematical intuition for machine learning principles.
- Explore core theoretical frameworks and evaluation strategies.

---

<h4 class="course-section">Cource Content</h4>

<style>
.table-no-hover table {
  border-collapse: separate;
  border-spacing: 0;
  width: 100%;
  table-layout: fixed;
}

.table-no-hover table th,
.table-no-hover table td {
  border: 1px solid #ccc;
  text-align: center;
  vertical-align: middle;
  padding: 5px;
}

/* Set specific column widths */
.table-no-hover table th:nth-child(1),
.table-no-hover table td:nth-child(1) {
  width: 4%;
}

.table-no-hover table th:nth-child(2),
.table-no-hover table td:nth-child(2) {
  width: 20%;
}

.table-no-hover table th:nth-child(3),
.table-no-hover table td:nth-child(3) {
  width: 8%;
}

.table-no-hover table th:nth-child(4),
.table-no-hover table td:nth-child(4) {
  width: 30%;
}

.table-no-hover table th:nth-child(5),
.table-no-hover table td:nth-child(5) {
  width: 26%;
}

.table-no-hover table th:nth-child(6),
.table-no-hover table td:nth-child(6) {
  width: 8%;
}

/* Optional: header styling */
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
  {% assign lectures = site.data.Courses.eec351_2025_content %}

<table>
  <thead>
    <tr>
      <th>Index</th>
      <th>Topic</th>
      <th>Content</th>
      <th>Essential Reading</th>
      <th>Additional</th>
      <th>Homework</th>
    </tr>
  </thead>
  <tbody>
    {% for lec in lectures %}
    <tr>
      <td>
        {% for num in lec.lecture %}
          {{ num }}{% if forloop.last == false %}, {% endif %}
        {% endfor %}
      </td>
      <td>{{ lec.topic }}</td>
      <td>
        {% if lec.slides contains "http" or lec.slides contains "/" %}
          <a href="{{ lec.slides }}">Slides</a>
        {% else %}
          {{ lec.slides }}
        {% endif %}
      </td>
      <td>
        {% if lec.essential %}
          {% for item in lec.essential %}
            <a href="{{ item.link }}">{{ item.text}}</a>{% if forloop.last == false %}, {% endif %}
          {% endfor %}
        {% else %}
          --
        {% endif %}
      </td>
      <td>
        {% if lec.additional %}
          {% for item in lec.additional %}
            <a href="{{ item.link }}">{{ item.text }}</a>{% if forloop.last == false %}, {% endif %}
          {% endfor %}
        {% else %}
          --
        {% endif %}
      </td>
      <td>
        {% if lec.homework contains "https" or lec.homework contains "/" %}
          <a href="{{ lec.homework }}">HW</a>
        {% else %}
          {{ lec.homework }}
        {% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
</div>
---

<h4 class="course-section">Assignments</h4>
- **Assignment #1** is due on **Thursday, 9th October, 5 PM**. Please read the instructions carefully—the required links are embedded within the PDF. Make sure to _explore all available resources_ and _troubleshoot thoroughly before reaching out to the instructor or TA_. [Assignment#1](/assets/pdf/EEC351/Assignment_1.pdf)-- [Boilerplate Code](/assets/pdf/EEC351/EEC351_Assignment_BoilerCode.zip)
- **Python** is the default programming languages for the course. You should use it for programming your assignments unless otherwise explicitly allowed.
- Submit via Moodle, Google Form or GitHub—- as specified in each assignment. 
- **Honor Code:** Any cases of copying will be awarded a zero on the assignment. More severe penalties may follow.
- **Late submissions** will incur penalties, as annouced with assignment. 


<!-- - **Assignment 1**: Released Feb 4, due Feb 14 — linear regression, CNN basics.  
- **Assignment 2**: Naïve Bayes & SVMs — released Feb 18, due Mar 17.  
- **Assignment 3**: Gradient-based methods — released Mar 31, due Apr 10.  
- **Assignment 4**: Deep Learning assignment — released Apr 13, due May 9.  
- Detailed instructions and submission links are available via Piazza. -->

---

<h4 class="course-section">References & Resources</h4>

- **Recommended Texts:**  
  - Probabilistic Machine Learning: An Introduction, Kevin Murphy. MIT Press, 2022/2023. 
  - Learning from Data: A Short Course, Yaser S. Abu-Mostafa, Malik Magdon-Ismail, Hsuan-Tien Lin. AMLBook, 2017.

- **Supplementary Resources:**  
  - Coursera ML (Andrew Ng)  
  - Relevant paper links on Piazza

---

<h4 class="course-section">Grading Policy</h4>

- CWS (30 Marks)
  - Announced & Surprise Quizzes
  - Assignments & Peer Discussions
- MTE (30 Marks)
  - Written Exam (any format)
- ETE (40 Marks)
  - Written Exam (any format)

<h4 class="course-section">Exam Papers</h4>

- [Mid-Term Examination Autumn 2025](/assets/pdf/EEC351/MTE.pdf)
- [End-Term Examination Autumn 2025](/assets/pdf/EEC351/ETE.pdf)
