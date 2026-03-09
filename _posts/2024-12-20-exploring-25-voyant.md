---
layout: page
title: Exploring the First 25 with Voyant
date: 2024-12-20
tags:
- recipes
- text analysis
author: Erin
excerpt: Visualizing and analyzing the first 25 scanned cookbooks using Voyant-Tools
image: first-25-top-cloud.JPG
---

## What is Voyant-Tools?

Voyant-Tools is an open-source text analysis environment available as a browser tool at voyant-tools.org or as a desktop tool that runs on a local server. It is very simple to load your corpus and get started and can handle a variety of file formats - plain text, PDF, HTML, XML, RDF, Word - which makes it a great platform for teaching and for gaining quick insights on your data. 

The default “skin” contains five different visualization tools that interact with one another as you select different words and options, and there are many more tools available beyond the default. Visualizations are shareable and embeddable and you can also export your current view as a URL.


## Word Frequencies

Voyant provides several different options for exploring word frequencies in your corpus. The word cloud (or "Cirrus") and the line graph (or "Trends") are two simple ways to visualize the most frequently occuring words, and the line graph provides the additional benefit of breaking word frequencies out by document to show differences among texts in your corpus. 

{% include image.html objectid="/assets/post-images/first-25-top-cloud.JPG;/assets/post-images/first-25-top-words.JPG" caption="Most frequent words in the first 25 cookbooks;Top 5 word frequencies in the first 25 cookbooks" %}



## Collocates

The collocates tool identifies the words that occur most frequently within a designated context window from your defined search term. Tool windows within Voyant interact with one another, so when you search for frequency of the word "cream" in the Trends tool, the Collocates tool updates to show results for "cream." From the results below, we can see that butter, sugar, and shortening are likely from the common instruction to "cream" butter or shortening and sugar together. The frequent mentions of "soup" are likely the very common "cream of" soups in casserole dishes (mushroom, celery, chicken, etc.).

{% include image.html objectid="/assets/post-images/first-25-cream.JPG;/assets/post-images/first-25-cream-collocates.JPG" caption="Frequency of 'cream' in first 25 cookbooks;Most frequent co-occuring words with 'cream'" %}

## Entity Recognition

Voyant performs named entity recognition using SpaCy and highlights results within the Reader pane with a dropdown list of entity categories arranged by frequency including: event, facility, geopolitical entity, language, person, and more. For community cookbooks, this tool can be useful for identifying recipe contributors who provided the most recipes to a particular cookbook. 

{% include image.html objectid="/assets/post-images/first-25-entity-recognition.JPG" caption="Entity recognition for the First Congregational Church of Forest City cookbook" %}


## Document Clustering

Voyant provides a tool for visualizing document similarity which is helpful for getting an idea of possible clusters of texts; however, the options for modification are limited, and the visualization becomes much harder to interpret as the number of texts increases. 
{% include image.html objectid="/assets/post-images/first-25-scatter.JPG" caption="Document similarity scatter plot, TF-IDF frequencies" %}