---
layout: page
title: Blog
nav: Blog
nav_order: 1
---

<style>
.post-list {
  list-style: none;
  padding: 0;
}
.post-list li {
  margin-bottom: 0.5em;
}
.post-card {
  background: #fff;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  overflow: hidden;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  gap: 1.5em;
  padding: 0.5em;
  flex-wrap: wrap;
}
.post-card-image {
  width: 240px;
  max-width: 40vw;
  height: 240px;
  object-fit: contain;
  border-radius: 6px;
  flex-shrink: 0;
}
.post-card-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.post-card-content h2 {
  margin: 0 0 0.5em 0;
  font-size: 1.2em;
  padding: 0;
}
.post-card-content p {
  margin: 0.5em 0;
}
.post-tags {
  font-size: 0.95em;
  color: #666;
}
.post-meta {
  font-size: 0.9em;
  color: #999;
  margin-top: 0.5em;
}
@media (max-width: 1024px) {
  .post-card {
    gap: 1em;
    padding: 0.5em;
  }
  .post-card-image {
    width: 120px;
    height: 120px;
    max-width: 30vw;
  }
}
@media (max-width: 767px) {
  .post-card {
    flex-direction: column;
    align-items: stretch;
    padding: 0.5em;
  }
  .post-card-image {
    width: 100%;
    height: 240px;
    margin-bottom: 0.5em;
    max-width: 100%;
  }
}
</style>

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
        <img src="{{ '/assets/' | append: post.image | relative_url }}" class="post-card-image" alt="{{ post.image-alt }}"> 
        {% endif %}
        <div class="post-card-content">
          <h2>
            <a class="post-link" href="{{ post.url | relative_url }}">
              {{ post.title | escape }}
            </a>
          </h2>
          {%- if site.show_excerpts -%}
            <p>{{ post.excerpt | markdownify }}</p>
          {%- endif -%}
          {%- if post.tags -%}
            <p class="post-tags">Tags: {% for tag in post.tags %}<a href="{{ '/tags/' | append: tag | relative_url }}" class="post-tag" class="text-decoration-underline">{{ tag }}</a>{% if forloop.last == false %}, {% endif %}{% endfor %}
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