---
layout: page
title: Student Blogs
permalink: /blogs/
nav: true
nav_order: 9
---

Welcome to the Student Blogs page! This section hosts articles written by students who have worked with me on various academic projects—including term papers, course projects, and summer research experiences. These posts showcase their learning journey and findings.

**Disclaimer:** Please note that these blogs are *not* peer-reviewed publications. They have only passed a basic sanity check by me and may contain errors or inaccuracies. If you find any bugs or errors, please feel free to email the author directly (with a copy to me) so we can correct them.

## All Posts

<style>
.blog-cards { list-style: none; padding: 0; margin: 1.2rem 0 0; display: flex; flex-direction: column; gap: 1rem; }
.blog-card { background: var(--global-card-bg-color); border: 1px solid var(--global-divider-color); border-radius: 10px; padding: 1rem 1.25rem; }
.blog-card .bc-title { font-size: 1.22rem; font-weight: 600; color: var(--global-theme-color); text-decoration: none; letter-spacing: -0.01em; }
.blog-card .bc-title:hover { text-decoration: underline; }
.bc-badge { font-size: 0.72rem; font-weight: 600; color: #8a5a00; background: #fbeccd; padding: 2px 9px; border-radius: 999px; margin-left: 0.45rem; vertical-align: middle; white-space: nowrap; }
.bc-meta { font-size: 0.85rem; color: var(--global-text-color-light); margin: 0.4rem 0 0.55rem; }
.bc-summary { font-size: 0.98rem; color: var(--global-text-color); margin: 0; line-height: 1.55; }
.bc-more { display: inline-block; margin-top: 0.75rem; font-size: 0.9rem; font-weight: 500; color: var(--global-theme-color); text-decoration: none; }
.bc-more:hover { text-decoration: underline; }
</style>

<ul class="blog-cards">
{% assign sorted_blogs = site.blogs | sort: 'date' | reverse %}
{% for post in sorted_blogs %}
  {% if post.published == false %}{% continue %}{% endif %}
  <li class="blog-card">
    <a class="bc-title" href="{{ post.url | relative_url }}">{{ post.title }}</a>{% if post.category == "Term Paper" %}<span class="bc-badge">term paper · unreviewed</span>{% endif %}
    <div class="bc-meta">
      {{ post.date | date: "%B %-d, %Y" }}{% if post.author %} · {{ post.author }}{% endif %}{% if post.course %} · {{ post.course }}{% elsif post.category %} · {{ post.category }}{% endif %}
    </div>
    <p class="bc-summary">{% if post.description %}{{ post.description }}{% else %}{{ post.content | strip_html | truncatewords: 30 }}{% endif %}</p>
    <a class="bc-more" href="{{ post.url | relative_url }}">{% if post.category == "Term Paper" %}View paper{% else %}Read{% endif %}</a>
  </li>
{% endfor %}
</ul>
