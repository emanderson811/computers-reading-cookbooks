---
layout: page
title: "Lexos Discovers the Grapefruit Diet"
date: 2025-08-25
tags: recipes text analysis lexos
author: Erin
excerpt: Using Lexos to uncover unexpected trends using Top Words analysis
image: first100-Lexos-top-grapefruit.jpg
---

## Exploring the First 100 Cookbook Corpus with Lexos

### Overview and Set-up

### Top Words Analysis 

One of Lexos' features that I find most useful is the Top Words tool. 

### Why so much grapefruit?

Among the large spreadsheet of numbers that resulted from the Top Words analysis for each book compared to the whole corpus, I noticed what seemed like an unusual number of books with high proportions of the word "grapefruit" compared to the corpus - five books to be exact. Grapefruit is not a common recipe ingredient, and while this analysis is meant to highlight unique words within specific books, I would have expected perhaps one or two "grapefruit" books, not five. Why all the grapefruit?

The answer was quickly discovered upon viewing the digitized cookbooks, but I think the results demonstrate the value of this type of exploratory text analysis and are therefore worth sharing. I opened the first pdf, hit "ctrl-f" for "grapefruit," and found all 31 mentions of grapefruit clustered in one section, the diet section. Three more cookbooks after that contained the exact same section produced by the exact same Dr. Orr. The 18-Day Reducing Diet, more commonly known as the Grapefruit Diet, includes one grapefruit half with every meal for 18 days and became popular in 1930s Hollywood before spreading across the U.S. and reamerging several times in different forms throughout the twentieth century. 
<div class="container my-4">
  <div class="row">
    <div class="col-md-3 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-b485x-1952-dr-orr.jpg" class="img-fluid rounded shadow" alt="Image 1">
        <figcaption class="text-center mt-2">Dr. Orr Cookbook, 1952</figcaption>
      </figure>
    </div>
    <div class="col-md-3 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-b685x-1951-dr-orr.jpg" class="img-fluid rounded shadow" alt="Image 2">
        <figcaption class="text-center mt-2">Dr. Orr Cookbook, 1951</figcaption>
      </figure>
    </div>
    <div class="col-md-3 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-s713x-1910-dr-orr.jpg" class="img-fluid rounded shadow" alt="Image 3">
        <figcaption class="text-center mt-2">Dr. Orr Cookbook, 1910</figcaption>
      </figure>
    </div>
    <div class="col-md-3 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-w5322x-1948-dr-orr.jpg" class="img-fluid rounded shadow" alt="Image 4">
        <figcaption class="text-center mt-2">Dr. Orr Cookbook, 1948</figcaption>
      </figure>
    </div>
  </div>
  <div class="row">
    <div class="col-md-3 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-b485x-1952-diet.jpg" class="img-fluid rounded shadow" alt="Image 5">
        <figcaption class="text-center mt-2">Grapefruit Diet Page, 1952</figcaption>
      </figure>
    </div>
    <div class="col-md-3 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-b685x-1951-diet.jpg" class="img-fluid rounded shadow" alt="Image 6">
        <figcaption class="text-center mt-2">Grapefruit Diet Page, 1951</figcaption>
      </figure>
    </div>
    <div class="col-md-3 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-s713x-1910-diet.jpg" class="img-fluid rounded shadow" alt="Image 7">
        <figcaption class="text-center mt-2">Grapefruit Diet Page, 1910</figcaption>
      </figure>
    </div>
    <div class="col-md-3 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-w5322x-1948-diet.jpg" class="img-fluid rounded shadow" alt="Image 8">
        <figcaption class="text-center mt-2">Grapefruit Diet Page, 1948</figcaption>
      </figure>
    </div>
  </div>
</div>

One additional book had a similarly high proportion of "grapefruit" occurences but did not contain this same diet section. 

{% include image-float.html objectid="/assets/post-images/tx715-2-m53-p452x-1948-pella.jpg" caption="Vegetable Salad recipe identified by Python" width="25" float="start" %}

<div class="container my-4">
  <div class="row">
    <div class="col-md-6 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-p452x-1948-crab.jpg" class="img-fluid rounded shadow" alt="Image 1">
        <figcaption class="text-center mt-2">Dr. Orr Cookbook, 1952</figcaption>
      </figure>
    </div>
    <div class="col-md-6 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-p452x-1948-pie.jpg" class="img-fluid rounded shadow" alt="Image 2">
        <figcaption class="text-center mt-2">Dr. Orr Cookbook, 1951</figcaption>
      </figure>
    </div>
  </div>
  <div class="row">
    <div class="col-md-6 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-p452x-1948-salad.jpg" class="img-fluid rounded shadow" alt="Image 5">
        <figcaption class="text-center mt-2">Grapefruit Diet Page, 1952</figcaption>
      </figure>
    </div>
    <div class="col-md-6 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-p452x-1948-more-salad.jpg" class="img-fluid rounded shadow" alt="Image 6">
        <figcaption class="text-center mt-2">Grapefruit Diet Page, 1951</figcaption>
      </figure>
    </div>
  </div>
</div>

In the next post I will dive deeper with Lexos to identify clusters of similar cookbooks using the K-Means tool and investigate what makes each cluster unique with the Top Words tool. Stay tuned!



