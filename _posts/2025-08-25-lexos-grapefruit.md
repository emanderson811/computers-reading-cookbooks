---
layout: page
title: "Lexos Discovers the Grapefruit Diet"
date: 2025-08-25
tags: recipes text analysis lexos
author: Erin
excerpt: Using Lexos to uncover unexpected trends using Top Words analysis
image: first100-Lexos-top-grapefruit.jpg
---

## Overview and Getting Started with Lexos

{% include image-float.html objectid="/assets/post-images/lexos_scrub.jpg" caption="Lexos Scrub Tool Screen" width="50" float="end" %}

Lexos is an open-source tool for corpus cleaning and analysis built by the [Lexomics Research Group](https://wheatoncollege.edu/academics/special-projects-initiatives/lexomics/) at Wheaton College. I am using the browser-based version, but there is also a version available for local installation.

Lexos provides several options for cleaning and normalizing your data prior to your analysis. Using the Scrub tool you can remove punctuation, numbers, and spaces, lowercase all text, remove a defined list of stop words and import rules for handling special characters. For this corpus, I removed punctuation and digits and made all lowercase. I also uploaded a standard set of stop words from the Natural Language Toolkit to remove common words like "the," "and," "is," etc.

Once you've applied all desired cleaning steps you can either export your cleaned corpus for use in another tool, or use it to explore a variety of visualization and analysis options within Lexos including word clouds and bubble graphs as well as dendrograms, k-means clustering, and cosine similarity measures. 

## Top Words Analysis 

{% include image-float.html objectid="/assets/post-images/lexos-topwords.jpg" caption="Lexos Top Words Results" width="50" float="end" %}

One of Lexos' features that I found most useful and have chosen to explore further is the Top Words tool. Top Words allows you to compare each individual document to the corpus as a whole to determine which words are unique to particular texts. You can choose to tokenize by tokens, characters, or n-grams and you can make a few adjustments to the number and frequency of terms to compare. If you've clustered your texts into what Lexos calls "classes" you can also compare each class of texts to all others, an option that I'll be exploring in a later post. 

To begin, I chose to compare each document to the corpus by unigram tokens. I noticed that running the tool with no frequency limits took a very long time, so I chose to limit the analysis to the top 1,500 terms rather than all terms. Lexos will output the top words for each text to a grid on the screen, but I chose to export the results to csv in order to get a better look. Terms with higher positive numbers occur more frequently compared to the corpus as a whole, and higher negative numbers occur less frequently compared to the corpus as a whole. There are a lot of questions to explore in looking at the results, so I'll share just one here that was particularly interesting to me.  

## Why so much grapefruit?

Amid the large spreadsheet of numbers, I noticed what seemed like an unusual number of books with high proportions of the word "grapefruit" compared to the corpus - five books to be exact. Grapefruit is not a common recipe ingredient, and while this analysis is meant to highlight unique words within specific books, I would have expected perhaps one or two "grapefruit" books, but not five. Why all the grapefruit?

The answer was quickly discovered upon viewing the digitized cookbooks, but I think the results demonstrate the value of this type of exploratory text analysis and are therefore worth sharing. I opened the first pdf, hit "ctrl-f" for "grapefruit," and found all 31 mentions of grapefruit clustered in one section, the diet section. Three more cookbooks after that contained the exact same section produced by the exact same Dr. Orr. The "18-Day Reducing Diet," also known as the Hollywood Diet and more commonly, the Grapefruit Diet, includes one grapefruit half with every meal for 18 days. This diet became popular in 1930s Hollywood before spreading across the U.S. and reamerging several times in different forms throughout the twentieth century. It is fairly common in community cookbooks to see standard sections of nutrition, measurements, ingredient substitutions, and household tips contributed by the publisher in addition to the community-contributed recipes. These diet sections appear to be this same type of publisher-contributed section.  
<div class="container my-4">
  <div class="row">
    <div class="col-md-3 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-b485x-1952-dr-orr.jpg" class="img-fluid rounded shadow" alt="Attribution of cookbook section to Dr. James D. orr and a medical disclaimer to consult physicion before using diet information">
        <figcaption class="text-center mt-2">Bethel Aid Society of the Evangelical United Brethren Church cookbook, 1952</figcaption>
      </figure>
    </div>
    <div class="col-md-3 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-b685x-1951-dr-orr.jpg" class="img-fluid rounded shadow" alt="Attribution of cookbook section to Dr. James D. orr and a medical disclaimer to consult physicion before using diet information">
        <figcaption class="text-center mt-2">Boone's Kitchen Secrets, 1951</figcaption>
      </figure>
    </div>
    <div class="col-md-3 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-s713x-1910-dr-orr.jpg" class="img-fluid rounded shadow" alt="Attribution of cookbook section to Dr. James D. orr and a medical disclaimer to consult physicion before using diet information">
        <figcaption class="text-center mt-2">St. John's Luthern Church cookbook, Jefferson, IA, 1910(?)</figcaption>
      </figure>
    </div>
    <div class="col-md-3 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-w5322x-1948-dr-orr.jpg" class="img-fluid rounded shadow" alt="Attribution of cookbook section to Dr. James D. orr and a medical disclaimer to consult physicion before using diet information">
        <figcaption class="text-center mt-2">What's Cookin'? in New Sharon, Iowa, 1948</figcaption>
      </figure>
    </div>
  </div>
  <div class="row">
    <div class="col-md-3 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-b485x-1952-diet.jpg" class="img-fluid rounded shadow" alt="First page of the Eighteen Day Reducing Diet section in cookbook showing breakfast, lunch, and dinner recommendations including grapefruit">
        <figcaption class="text-center mt-2">Bethel Aid Society of the Evangelical United Brethren Church cookbook, 1952</figcaption>
      </figure>
    </div>
    <div class="col-md-3 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-b685x-1951-diet.jpg" class="img-fluid rounded shadow" alt="First page of the Eighteen Day Reducing Diet section in cookbook showing breakfast, lunch, and dinner recommendations including grapefruit">
        <figcaption class="text-center mt-2">Boone's Kitchen Secrets, 1951</figcaption>
      </figure>
    </div>
    <div class="col-md-3 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-s713x-1910-diet.jpg" class="img-fluid rounded shadow" alt="First page of the Eighteen Day Reducing Diet section in cookbook showing breakfast, lunch, and dinner recommendations including grapefruit">
        <figcaption class="text-center mt-2">St. John's Luthern Church cookbook, Jefferson, IA, 1910(?)</figcaption>
      </figure>
    </div>
    <div class="col-md-3 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-w5322x-1948-diet.jpg" class="img-fluid rounded shadow" alt="First page of the Eighteen Day Reducing Diet section in cookbook showing breakfast, lunch, and dinner recommendations including grapefruit">
        <figcaption class="text-center mt-2">What's Cookin'? in New Sharon, Iowa, 1948</figcaption>
      </figure>
    </div>
  </div>
</div>

Three of the four books are from the late 1940s and early 1950s, but one book has the date 1910 in the call number which seemed out of place considering it contained the identical diet pages of the other books. To investigate this, I looked at the catalog record for this book which actually states "between 1910 and 1940?" in the Creation Date field, most likely an approximation based on the look and content since the book does not have a printed date. In this case, I think we can assume the book is from around the time of the other 3 books (~1948-1952) given the inclusion of identical diet information and even an identical image and layout to the 1952 Bethel book. 

One additional book had a similarly high proportion of "grapefruit" occurrences but did not contain this same diet section. It turns out the folks in Pella just *really* like grapefruit! Grapefruit pie, anyone?

{% include image-float.html objectid="/assets/post-images/tx715-2-m53-p452x-1948-pella.jpg" caption="Pella's Choicest Recipes, The Women's Auxiliary of Central College, 1948 " width="25" float="start" %}

<div class="container my-4">
  <div class="row">
    <div class="col-md-6 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-p452x-1948-crab.jpg" class="img-fluid rounded shadow" alt="recipe for Crab Meat and Grapefruit Cocktail with the word grapefruit highlighted">
        <figcaption class="text-center mt-2">Crab Meat and Grapefruit Cocktail</figcaption>
      </figure>
    </div>
    <div class="col-md-6 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-p452x-1948-pie.jpg" class="img-fluid rounded shadow" alt="recipe for Grapefruit Pie with the word grapefruit highlighted">
        <figcaption class="text-center mt-2">Grapefruit Pie</figcaption>
      </figure>
    </div>
  </div>
  <div class="row">
    <div class="col-md-6 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-p452x-1948-salad.jpg" class="img-fluid rounded shadow" alt="List of suggestions for salads with the word grapefruit highlighted">
        <figcaption class="text-center mt-2">Salad Suggestions</figcaption>
      </figure>
    </div>
    <div class="col-md-6 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-p452x-1948-more-salad.jpg" class="img-fluid rounded shadow" alt="Three different salad recipes including grapefruit with the word grapefruit highlighted throughout">
        <figcaption class="text-center mt-2">More Grapefruit Salads</figcaption>
      </figure>
    </div>
  </div>
</div>

In the next post I will dive deeper with Lexos to identify clusters of similar cookbooks using the K-Means tool and investigate what makes each cluster unique with the "classes" comparison in the Top Words tool. Stay tuned!



