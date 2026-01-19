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

<div class="row">
    <div class="col-sm-12">
        <ul class="post-list">
        {% assign sorted_blogs = site.blogs | sort: 'date' | reverse %}
        {% for post in sorted_blogs %}
            {% if post.published == false %}{% continue %}{% endif %}
            <li>
                <h3>
                    <a class="post-title" href="{{ post.url | relative_url }}">{{ post.title }}</a>
                </h3>
                <p class="post-meta">
                    {{ post.date | date: "%B %-d, %Y" }}
                    {% if post.author %} • {{ post.author }}{% endif %}
                    {% if post.category %} • {{ post.category }}{% endif %}
                </p>
                <p class="post-summary">
                    {% if post.description %}
                        {{ post.description }}
                    {% else %}
                        {{ post.content | strip_html | truncatewords: 30 }}
                    {% endif %}
                </p>
            </li>
        {% endfor %}
        </ul>
    </div>
</div>
