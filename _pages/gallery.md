---
layout: page
permalink: /gallery/
title: Gallery
description: Moments from the lab — events, outings, and milestones with students.
nav: false
nav_order: 10
---

<style>
  .gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.5rem;
    margin-top: 1.5rem;
  }
  .gallery-card {
    border: 1px solid #ddd;
    border-radius: 10px;
    overflow: hidden;
    background: #fff;
    box-shadow: 0 2px 8px rgba(0,0,0,0.07);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .gallery-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 18px rgba(0,0,0,0.12);
  }
  .gallery-card img {
    width: 100%;
    height: 220px;
    object-fit: cover;
    display: block;
  }
  .gallery-card-body {
    padding: 0.85rem 1rem 1rem;
  }
  .gallery-card-title {
    font-weight: 700;
    font-size: 0.95rem;
    color: var(--global-theme-color);
    margin: 0 0 0.2rem;
  }
  .gallery-card-date {
    font-size: 0.78rem;
    color: #999;
    margin: 0 0 0.5rem;
  }
  .gallery-card-caption {
    font-size: 0.88rem;
    color: #444;
    margin: 0;
    line-height: 1.5;
  }
</style>

<div class="gallery-grid">
  {% for item in site.data.gallery %}
    <div class="gallery-card">
      <a href="{{ '/assets/img/gallery/' | append: item.image | relative_url }}" data-lightbox="gallery" data-title="{{ item.caption }}">
        <img
          src="{{ '/assets/img/gallery/' | append: item.image | relative_url }}"
          alt="{{ item.title | default: item.caption }}"
          loading="lazy"
          onerror="this.onerror=null; this.style.height='120px'; this.style.objectFit='contain'; this.style.padding='1rem'; this.src='{{ '/assets/img/Lab_Logo.jpg' | relative_url }}';"
        />
      </a>
      <div class="gallery-card-body">
        {% if item.title %}
          <p class="gallery-card-title">{{ item.title }}</p>
        {% endif %}
        {% if item.date %}
          <p class="gallery-card-date">{{ item.date }}</p>
        {% endif %}
        <p class="gallery-card-caption">{{ item.caption }}</p>
      </div>
    </div>
  {% endfor %}
</div>

<p style="margin-top: 2.5rem; font-size: 0.85rem; color: #aaa; text-align: center;">
  Photos are added periodically. Check back for updates!
</p>
