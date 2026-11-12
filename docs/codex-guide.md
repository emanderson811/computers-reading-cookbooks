# Codex guidelines - Computers Reading Cookbooks: Exploring the Iowa Community Cookbook Corpus with NLP Tools

This site is built using the [bootstrap5-template](https://github.com/thecdil/bootstrap5-template), a Jekyll template for using Bootstrap 5 with GitHub Pages. See 'create-website.md' for template documentation.

## GitHub Pages and Sass Compatibility

Keep SCSS compatible with the older Ruby Sass compiler used by the GitHub Pages build. A successful local build with a newer Sass compiler does not guarantee compatibility with the hosted build.

Use comma-separated color functions such as `rgb(37, 38, 44)` or `rgba(37, 38, 44, 0.12)`. Avoid modern space-separated/slash syntax such as `rgb(37 38 44 / 12%)` in SCSS: it caused the GitHub Pages build to fail with `wrong number of arguments (1 for 3)` for `rgb` in `_sass/_custom.scss`.

Check compiler compatibility when introducing newer CSS/Sass syntax. Keep project styles in `_sass/_custom.scss`. Leave Jekyll builds to the user unless they explicitly request one; focused syntax compatibility checks are acceptable.

## Project Website Design Context

This website shares the scholarly outcomes and interactive/exploratory data visualizations of a collections-as-data and computational text analysis project called Computers Reading Cookbooks which analyses over 200 digitized and ocr'd cookbooks published by community organizations across Iowa. The researcher is interested both in the historical context of the cookbooks, their place within larger historical American culinary trends, and their ability to reveal unique ethnic and cultural identities of their respective communities. 

### Audience

- General public, local to Iowa: Desktop and mobile users casually interested in the history of Iowa food culture and their communities
- Scholars: Desktop and mobile users food historians, Iowa/Midwest historians, digital humanists

### Personality and Design Aesthetic

**References** A playful blend of scholarly/archival and digital humanities/data analyis, merging hyper-local historical often kitchy print media with experimental computational text analysis from an humanist perspective. Aesthetic draws directly from the cookbook source material (vintage paper, typewritten text, spiral bound cookbooks, hand-drawn line illustrations) combined with data analysis/data visualization elements. Retro coding environment. Voyant Tools color palette. The Pudding data journalism stories.


**Anti-references** corporate, trendy, social media-esque. Standard template elements like horizontal bar header image and nav bar, visible grid structure.

Do not use eyebrow text (small labels above headings) in page designs. Use headings directly without introductory category labels or numbered section labels.


### Accessibility

Full WCAG 2.1 AA standards compliance. Reduced motion preferences respected throughout.
