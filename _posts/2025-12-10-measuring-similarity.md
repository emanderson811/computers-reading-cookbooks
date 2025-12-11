---
layout: page
title: "Measuring and Visualizing Cookbook Similarity, Part One"
date: 2025-12-10
tags:
author: Erin
excerpt: Exploring different word vectorizers and distance measures for determining similarities among cookbooks
image: cosine-distance-scatter.jpg
---

## Measuring Similiarity: Euclidean vs Cosine Distance
A primary goal of this project is to determine which cookbooks are most similar and which are outliers with regard to their text content. Visualizing and analyzing similarity and difference will help to identify shared recipes or recipes and recipe categories that are unique to a particular community. Because cookbooks often contain other types of information, like histories of the community or organization or household tips, measuring similarity alone will not find shared or unique recipes, but it is a good early step to narrow down which books to examine in more detail.
There are many ways to measure document similarity, and I found John Ladd’s tutorial published in Programming Historian incredibly helpful in understanding and testing out a few of the most useful options for humanities work. 

The two measures I explored from Ladd's tutorial are Euclidean distance and Cosine similarity, which he provides very helpful explanations for that I won't duplicate here. Most basically, Euclidean distance measures the length of a direct line between two coordinate points on a graph and cosine distance instead measures the angle between two points if you were to draw a line from the origin to each of two points on a graph. What are the coordinate points? It depends on what you're analyzing, but in my case it is the frequency of each word in each cookbook, an x value for one word and y value for the next with additional dimensions for each word. Not graphable by hand, but thankfully, Python will do these calculations for me.

Next, in a Jupyter notebook I used scikit-learn's CountVectorizer to count every word in every text in my corpus and then SciPy to measure the Euclidean distance between each text based on that count. You can then print the results as a table of distances with each text compared to each other text. Below, I have also printed the top 5 texts closest to a chosen text (tx715-2-m53-b6638x-1960 or 'Our Favorite Recipes' compiled by Members and Friends of the First United Presbyteriam Church, Fairfield, Iowa)

{% include image.html objectid="/assets/post-images/first25-euclidean.jpg;/assets/post-images/first25-euclidean-top5.jpg" %}

Cosine distance is calculated very similarly just by changing the distance metric parameter from the default which is Euclidean to 'cosine.' Below are the five closest cosine distances for the same Fairfield text. Note that the scale for cosine distance is 0.0 - 1.0 with 0.0 being identical.

{% include image.html objectid="/assets/post-images/first25-cosine-top5.jpg" %}

## Exploring Term Frequency - Inverse Document Frequencey (Tf-idf)

Above, I used the CountVectorizer to count the raw frequencies of each word in each text in my corpus. This can be useful for some types of analysis; however, it treats every word as if it is of equal importance in the corpus, meaning "a" and "the" effect the distance measurement equally to "salad" and "mayonnaise". This may be desired if you're evaluating semantic style of different authors where differences in the usage of common words are indicators of a particular author's voice. In the case of cookbooks, I am more interested in comparing unique words. An alternative vectorizing method called Term Frequency - Inverse Document Frequency, or tf-idf, is a valuable thing to explore in this case, and the Programming Historian tutorial by Matthew Lavin is an excellent introduction to this method.

Tf-idf is a measure that takes the freqency of each term and divides it by the number of documents containing that term which assigns a weighted score that more heavily weighs terms that are more freqent in a given text than in all the other texts.

Calculating tf-idf in Python once again utilizes both SciPy and scikit-learn. The output is one csv file for each text containing a list of every word in the text and its tf-idf score. Below are the results for the 1923 book “A Collection of Choice and Tried Recipes” by the Philathea Society of the Whiting Congregational Church.

{% include image.html objectid="/assets/post-images/tf-idf-whiting.jpg" %}

A few observations from looking at these results: 
"whiting," the name of the town where the cookbook originated, is unsurpisingly the highest score.
Other terms that are clearly names of recipe contributors also scored very high ("edith," "mcbeath," "harriet," etc.).
Further down the list is an uncommon spelling of the word "cocoanut."
Notably, “gelatine” and “acidulated” scored quite high and while the age of the book could be a factor here, we have other books from this time period in the corpus, so it is worth examining this closer. "Acidulated" in particular is a strange word to occur frequently.

Inspection of the cookbook itself revealed brief, integrated advertisements for Knox gelatine on nearly every page of the book starting with the Beverages chapter (Knox comes in both “plain” and “acidulated”) as well as many recipes using Knox gelatine - an indication of a possible sponsorship of the book by the brand which is unusual for these community cookbooks.

While looking at these lists can lead you down many avenues of exploration, trying to make overal claims about the corpus by reading through the tf-idf matrices for each cookbook is time consuming and difficult to manage at-scale with 100 or more books, so this is not a very manageable analysis method on its own.

## Visualizing the First 25 Cookbooks

A next possible step for visualizing the outputs of both tf-idf measurement and cosine distance measurement is to plot them in scatter plots using matplotlib. Plotting these results can help to visualize clusters of similar cookbooks. It does not, however, explain *why* these books are similar or different. That is still up to the researcher's interpretation and requires deeper analysis. 

Tf-idf results can be plotted by graphing just the top two most unique keywords of each text (labeled below as "Principal Component 1" and "Principal Component 2").

{% include image.html objectid="/assets/post-images/first_25_abbyy_pca-tfidf_scatter_plot.png" %}

It is difficult to tell whether the clustering in this graph is working very well, and given that it is only plotting the first two most unique words for each cookbook, I suspect I'd need to do more cleanup on the texts for this method to be useful - removing all people's names, for instance. Plotting tf-idf directly may not be the best use of this method, however, as a pre-processing step for measuring cosine distance, it may be more useful.

I ran my cosine distance analysis again, but this time used tf-idf as my word vectorizor rather than the CountVectorizer I originally used. Then I plotted the new cosine distances in a scatter plot.

{% include image.html objectid="/assets/post-images/first_25_abbyy_tsne_scatter_plot.png" %}

Here we can see some clear clusters of cookbooks that make sense at least at first glance. There is a cluster of 1970s books and a cluster of 1990s books, for example. This is a visualization method I plan to continue to explore with the full 200 cookbooks, but as you can see, a static scatter plot will become difficult to interpret the more texts that are added.

In my next post, I'll share how I created a more interactive and web-friendly network graph of cosine distance results using the popular JavaScript library D3.