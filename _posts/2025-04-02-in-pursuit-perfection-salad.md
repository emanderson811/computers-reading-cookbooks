---
layout: page
title: In Pursuit of Perfection Salad
date: 2025-04-02
tags: recipes text analysis jello
author: Erin
excerpt: Searching for a classic domestic science recipe using AntConc's collocates tool
image: bhg-perfection-salad.jpg
---
## A *Very* Brief History of Domestic Science

Domestic science (alternatively home economics and later family and consumer sciences), was a large-scale women-led reform movement at the turn of the 20th century to bring order and scientific principles to domestic labor and most notably, to change how Americans cooked and what they ate. Domestic scientists opened cooking schools, published cookbooks and magazines, and organized clubs in order to promote American women's work in the home as both professional and aligned with the rapidly modernizing and industrializing American food system. 

## Origins of Perfection Salad and Popularity in Mass Market Cookbooks

The first appearance of a recipe for Perfection Salad is believed to have been written by Mrs. Mame Cooke who won 3rd place in a Knox Gelatine recipe contest in 1904 following a large Knox display at the St. Louis World's Fair. Cooke's recipe was later published in Knox’s pamphlet *Dainty Desserts for Dainty People* and in many later Knox publications. While aspics (meat in gelatin) and gelatin desserts had been popular for decades, Cooke’s Perfection Salad is credited with launching the nationwide craze for molded salads, a craze which lasted well into the 1960s (and still exists in some places). The first recipe for Perfection Salad is attributed to a home cook, but it’s aesthetic and nutritional roots are grounded in the guiding principles of the Domestic Science movement.
{% include image.html objectid="/assets/post-images/first-perfection-salad.jpg;/assets/post-images/dainty-desserts.jpg" alt="first published recipe for Perfection Salad;cover of recipe pamphlet Dainty Desserts for Dainty People featuring an image of the head of a cow and two small children holding platters of molded gelatin" caption="Mame Cooke's recipe for Perfection Salad published in Knox Gelatine's *Dainty Desserts for Dainty People*, c.1905;Cover of Knox Gelatine's *Dainty Desserts for Dainty People*, c.1905"  %}

Knox used the original name “Perfection Salad,” but many other brands including Jell-O published identical or similar recipes under a variety of different names. 
{% include image.html objectid="/assets/post-images/knox-on-camera.jpg;/assets/post-images/knox-on-camera2.jpg;/assets/post-images/knox-quickies.jpg;/assets/post-images/knox-quickies2.jpg" %}

{% include image.html objectid="/assets/post-images/jm-jello.jpg;/assets/post-images/jm-jello2.jpg;/assets/post-images/kelvinator.jpg;/assets/post-images/kelvinator2.jpg" %}
Even iconic American chef James Beard acknowledged Cooke and published her recipe in his most influential book *James Beard's American Cookery* in 1972, calling Perfection Salad "a standard in American cuisine."

## Understanding Prevalence in Community Cookbooks

It is always hard to judge the true popularity of recipes by their appearance in national cookbooks. Publication does not always or even often indicate actual widespread adoption by home cooks. A more reliable indication of the popularity of a recipe is it’s prevalence in community-generated cookbooks, collections of cherished recipes compiled to celebrate and showcase the cooking traditions of a community’s cooks.  

### Close Reading

For any text analysis project, understanding what is in your corpus and having some subject-matter expertise makes developing and honing your research questions much easier. Close reading is an important part of any text analysis process, and in my case, reading through the first 25 cookbooks and continuing to flip through each additional cookbook as they were digitized led to this particular inquiry into Perfection Salad recipes in this dataset. After encountering a few examples of Perfection Salad, I began saving images of each recipe I found. Once I had gathered around 10 examples including several with very different titles, I decided it would be a good fit for examining more systematically with text analysis tools.

{% include image.html objectid="/assets/post-images/tx715-2-m53-l482x-1984i017-perfection-salad.JPG;/assets/post-images/tx715-2-m53-o97x-1982i203-cabbage-salad.JPG;/assets/post-images/tx715-2-m53-s2539x-1998i027-lemon-cabbage-salad.JPG" alt="recipe for Perfection Salad;recipe for Cabbage Salad;recipe for Cabbage Lemon Salad" caption="tx715-2-m53-l482x-1984;tx715-2-m53-o97x-1982;tx715-2-m53-s2539x-1998"  %}

### Voyant Tools

Voyant can be used first to quickly identify the recipes throughout the corpus specifically named “Perfection Salad.” The example below shows the relative frequencies of the exact bigram "Perfection Salad" across all corpus files as well as some of the words that appear in context with "Perfection Salad." 
{% include image.html objectid="/assets/post-images/first100-voyant-perfection-salad-prize.JPG" alt="screenshot of the VoyantTools interface displaying a frequency graph and colocates list for the bigram Perfection Salad" caption="Voyant Tools Displaying Results for 'Perfection Salad' Frequecies and Colocates" width="50" %}

Searching for "Perfection Salad" is a good first step, but from looking at mass market cookbooks and community cookbooks it is clear that many recipes identical or very similar to the original Perfection Salad were published under a variety of names. For these recipes, I could not rely on a title search and instead needed to determine the best set of collocates (words occurring near one another within a set number of words) to target the most likely matches. Cabbage and gelatin or Jell-O are a highly unique combination and appear to be the defining ingredients for this dish, so I decided to search for all instances where cabbage and gelatin (or the alternative spelling “gelatine” or Jell-O) appear within close proximity. The format of recipes in community cookbooks varies. Some have neat ingredient lists at the top, some have partial ingredient lists followed by new ingredients mentioned in the instructions, and some are entirely narrative instructions with ingredients mentioned throughout. This variability makes finding collocates a little tricky. For example, the two recipes below show widely different distances between the word "cabbage" and either "gelatin," "gelatine," or "jello." The first example has 16 words between gelatin and cabbage and the second example has 26 words between Jello and cabbage.  

{% include image.html objectid="/assets/post-images/make-ahead-slaw.JPG;/assets/post-images/first100-voyant-perfection-salad-30words.JPG" caption="tx715-m53-m5422x-1976;Recipe for Perfection Salad, excerpt from Voyant" %}

The distance on either side between your target word (cabbage) and your collocates (gelatin, gelatine, and jello) is called your "context window." In this case, the ability to adjust and search a large context window is important. Voyant Tools allows you to adjust your context window and can identify collocates across your corpus, but you cannot drill down to the individual document, and while the tools are intended to be interoperable, they often don’t behave has expected or intended when switching between them. Additionally, Voyant cannot search for specific collocates, it can only display a full list of collocates that you then have to scroll through to find the ones you're interested in. In this case, Voyant Tools is helpful for a first look at our collocates, but we need to look for a different tool to get more detailed and accurate results.  


### AntConc

AntConc is a free text analysis tool for concordancing or identifying all occurances of a particular word within it's context. The default context window within AntConc is 5 words on either side of the target word; however, as we've already seen with these recipes, we could be looking to identify 10 or 20 (or more) words on either side. This requires a lot more computing power. AntConc has significant trouble handling requests for context windows greater than 8 or 9 words on either side of the target word, so while I can gather partial results using AntConc, the context window limitations still make it hard to identify ALL desired recipes.

Nevertheless, AntConc results are easy to navigate and can be displayed in several ways that make it easy to confirm that the recipes identified are good matches for Perfection Salad, which makes it a worthwhile tool to explore. Searches for “cabbage” with collocates “gelatin,” “gelatine,” and “jello” within 5 words left or right return 13, 4, and 12 matches respectively. Below shows co-occurances of "cabbage" and "jello" in AntConc's KWIC (key words in context) window. 
{% include image.html objectid="/assets/post-images/jello-cabbage-colocates.JPG" %}

AntConc has many other helpful visualization tools including the Plot tool which shows where your target word appears across each file in your corpus. Below we can see in a search for "salad" where the salad chapter or section of each cookbook is by the high concentration of occurances, and we can also see that the word "salad" appears sporadically throughout most texts as well. Digging a little deeper into those occurances reveals that these are often mentions of either "salad dressing (Miracle Whip)" or "salad oil (vegetable or canola oil)" in other types of recipes. 
{% include image.html objectid="/assets/post-images/first100-antconc-salad-plot.JPG" %}

### Python and NLTK

The next step, which I have just begun exploring, is using Python and the Natural Language Toolkit (NLTK). Using Python sacrifices the convenience of Voyant and AntConc's GUIs for more power, speed, and flexibility. In the excerpt from my Jupyter Notebook below, it shows the first five matches of "cabbage" with either "gelatin," "gelatine," or "jello" with a context window of 15 words on either side and with a larger context of 50 words printed to make checking the recipe easier without having to view the full text. This is a very promising path that I will be exploring further, so stay tuned!
{% include image.html objectid="/assets/post-images/python-cabbage.JPG" %}

## Theme and Variations

Search results for each of the above methods reveal a related family of recipes which appears to be a spin-off or adaptation of the original molded Perfection Salad. With almost identical ingredients, but much less water, recipes for coleslaw with a gelatin-based dressing promise to keep the salad “crisp” for days in the fridge while looking more like traditional coleslaw. 

Other variations of the original recipe include adding or subtracting vegetable and fruit ingredients and adding mayonnaise or similar ingredients to make the salad creamy. 

{% include image.html objectid="/assets/post-images/first100-voyant-perfection-salad-dressing.JPG;/assets/post-images/tx715-2-m53-b6638x-1960i013-gelatin-coleslaw.JPG;/assets/post-images/fruited-perfection.jpg" caption="Recipe for Perfection Salad and Dressing, excerpt from Voyant;tx715-2-m53-b6638x-1960;Recipe for Fruited Perfection from *Joys of Jell-O,* 4th ed." %}

## Sources

Beard, James. *James Beard's American Cookery.* Boston: Little, Brown and Company, 1972.

Shapiro, Laura. *Perfection Salad : Women and Cooking at the Turn of the Century.* New York: Farrar,    
Straus, and Giroux, 1986.

Grey, Sarah. “A Social History of Jell-O Salad.” Serious Eats, February 7, 2023. https://www.seriouseats.com/history-of-jell-o-salad. 

Morgan, Bonnie. "Perfection Salad," *Topanga New Times* (Topanga, CA), Nov. 18, 2022.

“Published Collections: Jell-O, America’s Most Favorite Dessert.” Hagley Museum and Library, September 12, 2018. https://www.hagley.org/librarynews/published-collections-americas-most-favorite-dessert. 

Olver, Lynne. “Perfection Salad.” The food timeline FAQ: salads. Accessed May 1, 2025. https://www.foodtimeline.org/foodsalads.html#perfectionsalad. 
