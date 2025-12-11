---
layout: page
title: "Measuring and Visualizing Cookbook Similarity, Part Two"
date: 2025-12-01
tags:
author: Erin
excerpt: Exploring a network graph of cosine distances built with D3.js
image: first100-network.jpg
---

## Where We Left Off: 
In my last post, I explored several different methods for measuring similarity of cookbooks and visualized the results of those methods as scatter plots. I found that using the Tf-idf vectorizer along with cosine distance was the most useful way to cluster similar texts, but a static scatter plot quickly becomes unreadable the more cookbooks are added. I wanted to explore another way of visualizing those results that would be interactive, visually appealing, and more appropriate for the web, so I turned to the popular Javascript library D3 to build a network graph.

## Preparing My Data for Visualization

I used ChatGPT to help pull information from both my cosine distance matrix and my metadata spreadsheet and format it into json for use with D3.js. I then checked and cleaned up the results where ChatGPT had missed data or created formatting errors. My first network visualization included only the filenames, but that requires a user to reference the metadata seperately in order to see the cookbook's title. So, I added a field to my json for the cookbook's title and author organization. I also added a "decade" field so that I could color each cookbook node by decade and see whether cookbooks tended to cluster together by date. 

## Iowa Community Cookbook Collection Network

The graph below represents the cosine distances of the first 100 cookbooks digitized for this project. Each dot or "node" on the graph represents a cookbook in the dataset. Cookbooks with a similarity score over 0.5 (lower distance) are connected by a line or "edge."

To interact with the network you can hover over nodes to see cookbook information, mouse-scroll to zoom in and out, click and drag to see other sections, and click and drag nodes to put the network back in motion.

{% include cookbook-network.html %}