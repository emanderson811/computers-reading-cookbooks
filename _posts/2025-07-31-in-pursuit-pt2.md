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

In [Part One](https://emanderson811.github.io/computers-reading-cookbooks/2025/04/02/in-pursuit-perfection-salad.html), I attempted to identify recipes in my test corpus (the first 100 Iowa community cookbooks digitized out of an eventual 200) resembling the popular domestic-science-era concoction "Perfection Salad" using several common text analysis tools. By using both Voyant and AntConc I was able to find many examples, but each tool had limitations that prevented a thorough search. I had begun preparing a Python Jupyter Notebook that could search a wider context window for instances of "cabbage" co-occurring with "gelatin," "gelatine," or "jello." Now I'll walk through the steps I have taken using Python to create a list of Perfection-salad-like recipes as well as explore a few anomalies in my corpus which this process helped to uncover.

## Setting up the Jupyter Notebook

I have used Python and the Natural Language Toolkit to search for words and create a concordance before, but I have not ever used it to identify collocates, so I used ChatGPT to help me think through the steps necessary in Python and refine my code.  The code excerpt below shows variables defined for the target word "cabbage" as well as the gelatin collocates or "trigger words" and the context window size of 15. While reviewing the results of my first test with this code I realized that the 15-word context window was not enough text for me to tell whether the recipe was truly a match, so I decided to print larger 50-word snippets for each result to make reviewing easier. The image below also shows my function "find_proximity_matches" which applies my defined variables, finds matches, and returns the filenames and text snippets. 

{% include image.html objectid="/assets/post-images/jupyter-cabbage-collocates-function.jpg" caption="Excerpt from Python notebook" %}

The code goes on to cycle through each cookbook txt file in my corpus folder, opening each, tokenizing each using NLTK's word_tokenize, and creating a list of matches. The first version of this notebook simply displayed the filenames and snippets on-screen which was great for making sure the function was working but not practical for reviewing all results. So, I added code to output all results to a csv. 


One additional step I am considering is to merge the title, date, and organization from my metadata spreadsheet into the csv export of results so that I can easily see more information about the cookbooks without having to go to the image files. This extra information wasn't necessary for this analysis since I needed to review the images anyway, but for a more polished workshop-ready Jupyter notebook I think this would be really helpful. 

## Examining and Cleaning the Python Output

Python identified 75 matches based on the search perimeters outlined above and generated a csv with the file name and 50-word snippet for each result. I was then able to review each snippet to see whether the generated results matched my definition of a Perfection-Salad-like recipe.

Some of the returned results were easily discarded because they were duplicates that occurred because one result was generated for each instance of cabbage occurring near the gelatin terms, so if cabbage appeared more than once in the same recipe and near enough to the other words, that recipe was returned twice in the search results. I was also able to discard results that were simply recipe names from a cookbook's table of contents rather than the full recipe.

Other incorrect results required a little more investigation. One example appears in the 1940 Ladies Aid Society of the Christian Church cookbook from Delta, Iowa. The Python results identified one recipe from this book called "Vegetable Salad," but when I looked for that recipe in the digitized cookbook I noticed another recipe on the same page called "Perfection Salad" that Python did not catch, and I was very curious why. 

{% include image.html objectid="/assets/post-images/tx715-2-m53-c6636x-1940-pdf-52.jpg;/assets/post-images/tx715-2-m53-c6636x-1940-pdf-52-missed.jpg" caption="Vegetable Salad recipe identified by Python;Perfection Salad recipe missed by Python" %}

I programmed Python to search within 15 words on either side of the word "cabbage" for occurrences of "gelatin," "gelatine," or "jello." The Perfection Salad recipe in the digitized image has the word "gelatin" occurring 12 words from the word "cabbage" on the left and 10 words from "cabbage" on the right. To determine why this recipe was not recognized, I took a look at the OCR txt file produced by ABBYY FineReader and noticed that the recipe for Perfection Salad is a mess in the OCR. Several recipes are garbled together and some words are missing entirely which has effected the number of words between "gelatin" and "cabbage" causing Python to miss this recipe. I have been using ABBYY FineReader OCR files for all analysis so far, but for the sake of testing and comparison, I have also been producing OCR files using Tesseract OCR. The image on the right below is the Tesseract version of the same Perfection Salad recipe. *Much* better. Throughout this project there has not been a consistant "winner" as far as OCR quality between ABBYY and Tesseract. Each do some things better than the other, but in this case the difference in OCR output quality was enough to effect my analysis - something I'll need to consider how to manage as I continue with this project. 

{% include image.html objectid="/assets/post-images/tx715-2-m53-c6636x-1940-ocr-abbyy-missed.jpg;/assets/post-images/tx715-2-m53-c6636x-1940-ocr-tesseract-missed.jpg" caption="Recipe OCR'd with ABBYY FineReader;Recipe OCR'd by Tesseract" %}

Below is one final example of a recipe that Python missed even though it fits my ingredient criteria for Perfection Salad: 

{% include image.html objectid="/assets/post-images/tx715-2-m53-f3863x-1979-ocr-abbyy-missed.jpg;/assets/post-images/tx715-2-m53-f3863x-1979-pdf-16-missed.jpg" caption="OCR for Coleslaw Parfait' Salad recipe;Coleslaw Parfait' Salad Recipe" %}

In this case, there are multiple occurrences of the word "gelatin" but all of them are outside of our context window of 15 words left or right of "cabbage." Widening the context window would help catch examples like this; however, it would also identify many more recipes that I would have to discard because they do not qualify. For example, widening the context window could identify recipes that contain jello or gelatin that are next to other recipes that contain cabbage. Earlier I mentioned I used NLTK's word_tokenize which splits a long text string into a list of tokens or "words." Word_tokenize counts punctuation and numbers as "words." So, an alternative to changing the context window would be to remove all numbers and punctuation from the text, lessening the number of "words" between ingredients in many cases and therefore bringing more occurrences within the current context window.

## Final Results

After reviewing and cleaning the results, I was able to identify 50 individual recipes resembling Perfection Salad in my test corpus of 100 cookbooks. Some are more true to the original molded salad, and some are more similar to the variation described in Part One where gelatin is used as a thickener for the slaw dressing. You'll also notice some have titles that may have made them identifiable at a glance while others have more ambiguous titles that would have made identifying by human visual search much more difficult. Below are a few examples of recipes identified by the Python notebook:

<div class="container my-4">
  <div class="row">
    <div class="col-md-4 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-a165x-1976-pdf-111.jpg" class="img-fluid rounded shadow" alt="Ham-Cabbage Salad Molds recipe">
        <figcaption class="text-center mt-2">Ham-Cabbage Salad Molds From '76 Cookbook: Tested Recipes from Plymouth Congregational United Church of Christ, Des Moines, IA</figcaption>
      </figure>
    </div>
    <div class="col-md-4 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-b34x-1982-pdf-152.jpg" class="img-fluid rounded shadow" alt="Cabbage salad recipe">
        <figcaption class="text-center mt-2">Cabbage Salad From Bagley, Iowa Centennial Cookbook: 1882-1982</figcaption>
      </figure>
    </div>
    <div class="col-md-4 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-c69x-1973-pdf-181.jpg" class="img-fluid rounded shadow" alt="Church Dinner Cabbage Salad recipe">
        <figcaption class="text-center mt-2">Church Dinner Cabbage Salad From Country Kitchen Favorites: Women of Pomeroy Covenant Church</figcaption>
      </figure>
    </div>
  </div>
  <div class="row">
    <div class="col-md-4 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-c6646x-1950-pdf-29.jpg" class="img-fluid rounded shadow" alt="Garden crisp salad recipe">
        <figcaption class="text-center mt-2">Garden Crisp Salad From American Legion Auxiliary Cook Book</figcaption>
      </figure>
    </div>
    <div class="col-md-4 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-f365x-1928-pdf-14.jpg" class="img-fluid rounded shadow" alt="Perfection salad recipe">
        <figcaption class="text-center mt-2">Perfection Salad From Delaware County Farm Bureau Cook Book, 1928</figcaption>
      </figure>
    </div>
    <div class="col-md-4 mb-4">
      <figure>
        <img src="{{ site.baseurl }}/assets/post-images/tx715-2-m53-s713x-1910-pdf-4.jpg" class="img-fluid rounded shadow" alt="Breath of Spring Salad recipe">
        <figcaption class="text-center mt-2">Breath of Spring Salad From St. John's Lutheran Church Ladies' Aid Society, Jefferson, Iowa </figcaption>
      </figure>
    </div>
  </div>
</div>

  

