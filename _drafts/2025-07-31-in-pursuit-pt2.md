---
layout: page
title: "In Pursuit of Perfection Salad, Part Two"
date: 2025-07-31
tags: recipes text analysis jello python
author: Erin
excerpt: Searching for a classic domestic science recipe using Python
image: tx715-2-m53-c6636x-1940-ocr-tesseract-missed.jpg
---

## Where We Left Off

In [Part One](https://emanderson811.github.io/computers-reading-cookbooks/2025/04/02/in-pursuit-perfection-salad.html), I attempted to identify recipes in my test corpus (the first 100 Iowa community cookbooks digitized out of an eventual 200) resembling the popular domestic-science-era concoction "Perfection Salad" using several common text analysis tools. By using both Voyant and AntConc I was able to find many examples, but each had limitations that prevented a thorough search. I had begun preparing a Python Jupyter Notebook that could search a wider context window for instances of "cabbage" co-occuring with "gelatin," "gelatine," or "jello" and print a snippet of the text for quality control purposes. Now I'll walk through the steps I have taken using Python to create a list of Perfection-salad-like recipes as well as explore a few anomalies in my corpus which this process helped to uncover.

## Setting up the Jupyter Notebook

## Results

Python identified 75 matches based on the search perimeters outlined above and generated a csv with the file name and 50-word snippet for each result. I was then able to review each snippet to see whether the generated results matched my definition of a Perfection-Salad-like recipe. 

In all, I was able to identify 50 individual recipes resembling Perfection Salad in my test corpus of 100 cookbooks. 

## Examining Some Anomolies

Some of the returned results were easily discarded because they were duplicates that occurred because one result was generated for each instance of cabbage occurring near the gelatine terms, so if cabbage appeared more than once in the same recipe and near enough to the other words, that recipe was returned twice in the search results. I was also able to discard results that were simply recipe names from a cookbook's table of contents rather than the full recipe.

Other incorrect results required a little more investigation. One example appears in the 1940 Ladies Aid Society of Christian Church cookbook from Delta, Iowa. The python results identified one recipe from this book called "Vegetable Salad," but when I looked for that recipe in the digitized cookbook I noticed another recipe on the same page called "Perfection Salad" that python did not catch, and I was very curious why. 

{% include image.html objectid="/assets/post-images/tx715-2-m53-c6636x-1940-pdf-52.jpg;/assets/post-images/tx715-2-m53-c6636x-1940-pdf-52-missed.jpg" caption="Vegetable Salad recipe identified by Python;Perfection Salad recipe Python missed" %}

I programmed Python to search within 15 words on either side of the word "cabbage" for occurences of "gelatin," "gelatine," or "jello." The Perfection Salad recipe in the digitized image has the word "gelatine" occuring 12 words from the word "cabbage" on the left and 10 words from "cabbage" on the right. 

{% include image.html objectid="/assets/post-images/tx715-2-m53-c6636x-1940-ocr-abbyy-missed.jpg;/assets/post-images/tx715-2-m53-c6636x-1940-ocr-tesseract-missed.jpg" caption="Recipe OCR'd with ABBYYFineReader;Recipe OCR'd by Tesseract" %}

