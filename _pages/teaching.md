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
.selfml-card {
  border: 1px solid var(--global-divider-color);
  border-radius: 10px;
  background: var(--global-card-bg-color);
  padding: 1rem 1.25rem;
  margin-top: 1rem;
}
.selfml-head { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem; }
.selfml-title { font-weight: 600; font-size: 1.05rem; color: var(--global-theme-color); }
.selfml-btn {
  font-size: 0.85rem; font-weight: 500;
  color: var(--global-hover-text-color); background: var(--global-theme-color);
  border-radius: 6px; padding: 5px 13px; text-decoration: none;
}
.selfml-btn:hover { background: var(--global-hover-color); color: var(--global-hover-text-color); text-decoration: none; }
.selfml-desc { font-size: 0.95rem; color: var(--global-text-color); line-height: 1.55; margin: 0.7rem 0 0; }
</style>

#### Current Courses
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

<div style="margin-top: 2.5rem;"></div>

#### Self-Study Resources

<div class="selfml-card">
  <div class="selfml-head">
    <span class="selfml-title">Self-Learning Machine Learning</span>
    <a class="selfml-btn" href="/assets/pdf/Self_ML.pdf" target="_blank" rel="noopener">Open / download PDF</a>
  </div>
  <p class="selfml-desc">A one-page, curated roadmap for learning machine learning from scratch. It lists the best free resources in the order I'd suggest working through them — the probability, linear-algebra, and programming prerequisites first, then core machine-learning and deep-learning courses, and finally how to move into projects and research. Put together by the lab for students starting out; please feel free to share it, with acknowledgement.</p>
</div>

<div class="selfml-card">
  <div class="selfml-head">
    <span class="selfml-title">Optimization Modeling for Engineers</span>
    <a class="selfml-btn" href="https://laurentlessard.com/teaching/5374-optimization-modeling/" target="_blank" rel="noopener">Open course</a>
  </div>
  <p class="selfml-desc">An openly available course (ME 5374) by <a href="https://laurentlessard.com/" target="_blank" rel="noopener">Prof. Laurent Lessard</a>, Northeastern University. It teaches how to turn real engineering problems into optimization models — linear, quadratic, convex, and mixed-integer / non-convex programs — solve them with modern tools, and interpret the results through sensitivity and trade-off analysis. Lecture slides, Julia notebooks, and project examples are all public. This is an external resource shared here for self-study; full credit to the author.</p>
</div>
