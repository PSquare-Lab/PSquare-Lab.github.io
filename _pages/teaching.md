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
  color: var(--global-theme-color);
  text-decoration: none;
}
.course-sem {
  font-size: 0.95rem;
  color: var(--global-text-color-light);
  margin-left: 0.4rem;
}
</style>

##### Current Courses
{% assign current_courses = site.teaching | where: "status", "current" %}
<ul>
  {% for course in current_courses %}
    <li><a class="course-link" href="{{ course.url }}">{{ course.title }}</a>{% if course.semester %}<span class="course-sem">{{ course.semester }}</span>{% endif %}</li>
  {% endfor %}
</ul>

<div style="margin-top: 2rem;"></div>  <!-- Spacer -->

#### Past Courses
{% assign past_courses = site.teaching | where: "status", "past" %}
<ul>
  {% for course in past_courses %}
    <li><a class="course-link" href="{{ course.url }}">{{ course.title }}</a>{% if course.semester %}<span class="course-sem">{{ course.semester }}</span>{% endif %}</li>
  {% endfor %}
</ul>
