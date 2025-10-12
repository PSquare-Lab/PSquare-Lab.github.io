---
title: Teaching
permalink: /teaching/
layout: default
page_title: Teaching
description: Details about teaching activities of present and past semesters
nav: true
nav_order: 6
---

<style>
.course-link {
  font-size: 1.2rem;
  color: #0faddd;
  text-decoration: none;
}
</style>

##### 📘 Current Courses: Autumn 2025-26
{% assign current_courses = site.teaching | where: "status", "current" %}
<ul>
  {% for course in current_courses %}
    <li><a class="course-link" href="{{ course.url }}">{{ course.title }}</a></li>
  {% endfor %}
</ul>

<div style="margin-top: 2rem;"></div>  <!-- Spacer -->

#### 📕 Past Courses
{% assign past_courses = site.teaching | where: "status", "past" %}
<ul>
  {% for course in past_courses %}
    <li><a class="course-link" href="{{ course.url }}">{{ course.title }}</a></li>
  {% endfor %}
</ul>
