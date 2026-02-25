---
title: Computers Reading Cookbooks
layout: default
---

{% include jumbotron.html heading=site.title text="A project blog documenting the digitization and analysis of the Iowa Community Cookbook Collection" button-text="Learn More" button-link="pages/about.html" button-color="info" text-color="white" bg-image="assets/cookbook-banner.jpg" %}

# News and Updates
<!---
This is pulling one card per blog post. Use this code later to change to news items and updates. Need to create a News collection in config
-->
<div class="container">
    <div class="row">
        {% assign sorted_posts = site.posts | sort: 'date' | reverse %}
        {% assign recent_posts = sorted_posts | slice: 0, 3 %}
        {% for post in recent_posts %}
            <div class="col-md-4 d-flex mb-4">
                {% include card.html 
                    text=post.excerpt 
                    header=post.title 
                    img=post.image 
                    alt=post.alt 
                    width="100" 
                    url=post.url %}
            </div>
        {% endfor %}
    </div>
</div>
