---
layout: page
title: Developing My Corpus
tags: corpus data
date: 2024-06-07
author: Erin
excerpt: Criteria for selecting the cookbooks for this project
image: tx715-2-m53-d38x-1974i001-crop.jpg
---

## About the Iowa Cookbook Collection
{% include blockquote.html quote="Over the past century, many towns, organizations, and churches in Iowa have gathered recipes from members and published them, essentially preserving and documenting the culinary heritage of this state.  These cookbooks often contain family recipes, ethnic dishes, and history about the organization or area.  The Iowa State University Library is working to preserve these valuable wells of social history for use by future generations in understanding Iowa culture and history...These cookbooks contain not just recipes, but the history of the ethnic flavor of Iowa's people. Their contents can be used to illuminate the past and document the changes occurring in our population. We currently have about 3000 cookbooks dating back to the 1800's for Iowa in addition to about 100 historical America cookbooks dating back to the early 1700's. This project began in the early 1990's spurred on by two rather substantial gifts of cookbooks from Robert Smith or What Cheer and the family of Ruth Ellen Church, an ISU graduate and food editor for the Chicago Tribune." speaker="Iowa Cookbook Collection Exhibit" source="Iowa State University Special Collections and University Archives" %}

## My Selection Criteria for this Project: Iowa Community Cookbooks
Cookbooks selected for this project should fit the following criteria:

- Published 2009 or earlier - a somewhat arbitrary date before which we can reasonably assume no longer in print

- Produced by a community organization, cooperative, or special interest group - formal or informal

    - No single-author publications or family collections
    - No state-wide compilations
    - No ingredient-specific corporate publications

Dataset was pulled from Alma using the “Iowa Cookbook Collection” designator in the catalog record

An original list of 1405 was cleaned for duplicates, and any records not fitting the above criteria were removed creating a subset of “Iowa Community Cookbooks” numbering = 982

## Choosing the First 200
For Phase 1, a random selection of 200 books was selected from the Iowa Community Cookbooks list using the following steps:

The total number of books was divided by the number of decades in the collection to determine how many books from each decade should be randomly selected in order to get a date-balanced subset (as much as possible)

Dates: 1896-2009 = 11 decades (only 2 books dated 1896 were wrapped into the 1900 decade) 

200/11 = ~18 books/decade

Earlier decades from 1896-1950 did not include at least 18 books in each decade so all books from this time period were included.

Starting in 1950, the list was randomized by decade using Excel’s “RAND()” function, and the first 18 books in the list for each decade were selected, the same method was used for books with no publication date

This process resulted in 166 books selected with an additional 8 books that had been scanned as part of the project proposal/testing phase. The remaining books were selected randomly by the method above choosing 4 from each decade 1950-2000 and 2 books from the no-date category.
