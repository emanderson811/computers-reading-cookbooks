---
layout: page
title: Blog
nav: Blog
nav_order: 1
---

   {% if site.paginate %}
    {% assign posts = paginator.posts %}
  {% else %}
    {% assign posts = site.posts %}
  {% endif %}


{%- if posts.size > 0 -%}
  {%- if page.list_title -%}
    <h2 class="post-list-heading">{{ page.list_title }}</h2>
  {%- endif -%}
  <ul class="post-list">
    {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
    {%- for post in posts -%}
    <li>
      <div class="post-card">
        {% if post.image %}
        <div class="post-card-art">
          <img src="{{ '/assets/' | append: post.image | relative_url }}" class="post-card-image" alt="{{ post.image-alt | default: post.alt | default: post.title | escape }}" loading="lazy" decoding="async">
        </div>
        {% endif %}
        <div class="post-card-content">
          <h2>
            <a class="post-link" href="{{ post.url | relative_url }}">
              {{ post.title | escape }}
            </a>
          </h2>
          {%- if site.show_excerpts -%}
            <div class="post-excerpt">{{ post.excerpt | markdownify }}</div>
          {%- endif -%}
          {%- if post.tags -%}
            <p class="post-tags">Tags: {% for tag in post.tags %}<a href="{{ '/tags/' | append: tag | relative_url }}" class="post-tag text-decoration-underline">{{ tag }}</a>{% if forloop.last == false %}, {% endif %}{% endfor %}
            </p>
          {%- endif -%}
          <span class="post-meta">{{ post.date | date: date_format }}</span>
        </div>
      </div>
    </li>
    {%- endfor -%}
  </ul>
{%- endif -%}

{% if site.paginate %}
  <div class="pager">
    <ul class="pagination">
      {%- if paginator.previous_page -%}
        <li><a href="{{ paginator.previous_page_path | relative_url }}" class="previous-page">{{ paginator.previous_page }}</a></li>
      {%- else -%}
        <li><div class="pager-edge">•</div></li>
      {%- endif -%}
      <li><div class="current-page">{{ paginator.page }}</div></li>
      {%- if paginator.next_page -%}
        <li><a href="{{ paginator.next_page_path | relative_url }}" class="next-page">{{ paginator.next_page }}</a></li>
      {%- else -%}
        <li><div class="pager-edge">•</div></li>
      {%- endif -%}
    </ul>
  </div>
{% endif %}
