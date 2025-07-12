---
title: "EEC 351: Fundamentals of AI/ML"
permalink: /teaching/course_EEC351/
layout: page
status: current
description:
nav: false
---


##### <span style="color: #0faddd;; font-weight: bold;">Course Information</span>


- **Semester:** Autumn Semester 2025  
- **Instructor:** Parikshit Pareek (email: pareek AT ee.iitr.ac.in)  
- **Lectures:** Thu • 03:00–03:55 PM;  Fri • 4:05–5:00 PM; (Venue: GB205)
- **Office Hours:** Tue • 4:05–5:00 PM;  (Venue: 214A, EE)
- **Piazza:** [https://piazza.com/indian_institute_of_technology_roorkee/fall2025/eec351](https://piazza.com/indian_institute_of_technology_roorkee/fall2025/eec351)
- **TA:** Rajdeep R. Dwivedi (email: rajdeep_rd AT ece.iitr.ac.in)

---

##### <span style="color: #0faddd;; font-weight: bold;"> 📌 Announcements</span>

- **2025‑07‑13**: Course Announcements will be posted here regularly. Email notifications will **only** be sent if information is urgent.
<!-- - **2025‑07‑01**: Course Announcements will be posted here regularly. Email notifications will **only** be sent if information is urgent. -->
<!-- - **2025‑06‑20**: First assignment released! Due July 1. Check the Assignments section below. -->
- **2025‑07‑12**: Course website launched.


---

##### <span style="color: #0faddd;; font-weight: bold;"> 🎯 Course Objectives</span>

- Comprehend the historical evolution and foundational concepts of AI/ML. 
- Build mathematical intuition for machine learning principles.
- Explore core theoretical frameworks and evaluation strategies.

---

##### <span style="color: #0faddd;; font-weight: bold;"> 📅 Cource Content</span>

<style>
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
  {% assign lectures = site.data.Courses.eec351_content %}

  <table>
    <thead>
      <tr>
        <th>Lecture No.</th>
        <th>Topic</th>
        <th>Slides</th>
        <th>Essential Reading</th>
        <th>Additional Reading</th>
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
        <td>{{ lec.essential }}</td>
        <td>{{ lec.additional }}</td>
        <td>
          {% if lec.homework contains "http" or lec.homework contains "/" %}
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

##### <span style="color: #0faddd;; font-weight: bold;"> 📝 Assignments</span>

- **Python** is the default programming languages for the course. You should use it for programming your assignments unless otherwise explicitly allowed.
- Submit via Moodle or GitHub—- as specified in each assignment. 
- **Honor Code:** Any cases of copying will be awarded a zero on the assignment. More severe penalties may follow.
- **Late submissions** will incur penalties, as annouced with assignment. 


<!-- - **Assignment 1**: Released Feb 4, due Feb 14 — linear regression, CNN basics.  
- **Assignment 2**: Naïve Bayes & SVMs — released Feb 18, due Mar 17.  
- **Assignment 3**: Gradient-based methods — released Mar 31, due Apr 10.  
- **Assignment 4**: Deep Learning assignment — released Apr 13, due May 9.  
- Detailed instructions and submission links are available via Piazza. -->

---

##### <span style="color: #0faddd;; font-weight: bold;"> 📚 References & Resources</span>

- **Recommended Texts:**  
  - Probabilisitic Machine Learning: An Introduction, Kevin Murphy. MIT Press, 2022/2023. 

- **Supplementary Resources:**  
  - Coursera ML (Andrew Ng)  
  - Relevant paper links on Piazza

---

##### <span style="color: #0faddd;; font-weight: bold;"> 🧾 Grading Policy</span> 

- CWS (30 Marks)
  - Announced & Surprise Quizzes
  - Assignments & Peer Discussions
- MTE (30 Marks)
  - Written Exam (any format)
- ETE (40 Marks)
  - Written Exam (any format)