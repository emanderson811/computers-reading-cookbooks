# Salad ingredient frequency data

`assets/data/salad-ingredient-frequencies.json` contains ingredient pools for
**Fruit**, **Jello**, and **Vegetable**, derived from the ingredient lists in
`assets/data/salad-ingredients.json`. It does not change the Salad Spinner page.

## Counts and weights

Each category contains a `recipe_count`, an `ingredient_count`, and an
`ingredients` array. Each ingredient has:

- `name`: the normalized ingredient name for display and matching.
- `recipe_count`: the number of recipes in that category containing it.
- `weight`: the square root of that count, rounded to six decimal places.
- `source_names`: the original ingredient wording grouped under this name,
  retained for auditing the normalization. These are not recipe credits.

An ingredient counts at most once per recipe, even when several entries in a
recipe normalize to it. A recipe assigned to multiple categories contributes to
each category. Jello is exclusive: recipes tagged jello have no other category.
The pools include 51 fruit recipes, 85 jello recipes, and 37 vegetable recipes.

The spinner can draw from `categories.fruit.ingredients` (or `jello` or
`vegetable`). For each slot, choose in proportion to `weight`, then remove that
ingredient from the available pool. Remove locked ingredients before drawing new
slots. Weights are relative values, not percentages. They must be summed again
over the available ingredients for each draw. This prevents repeating the same
normalized ingredient within a generated list.

Counts remain available if a future version uses equal chances or weights
directly by frequency instead. Water and seasonings are retained; the interface
can filter them out before drawing.

## Normalization and limitations

Explicit ingredient-family rules combine preparation and size variants, such as
chopped and diced celery, pineapple chunks and crushed pineapple, and miniature
and regular marshmallows. Fresh, frozen, and canned forms are generally grouped.
Cream and whipped cream are grouped as cream. These broad groupings support an
ingredient-only remix; they should not be used to substitute amounts or directions.

Juices remain separate from fruit. Celery seed remains separate from celery, and
flavored gelatins remain separate from one another. Named nut and cheese varieties
are retained; entries without a specified variety use an explicit unspecified label.
Some broad labels can overlap with more specific ones, such as cabbage and red
cabbage, or nuts and walnuts. Different normalized names are not a guarantee of
different food families.

Clear compounds are split: for example, "Salt and pepper" contributes salt and
black pepper. Optional ingredients count as present. An explicit primary ingredient
with a parenthetical substitution uses the primary ingredient. Alternatives such
as "bananas or oranges" and unclear transcriptions such as "green mangol diced"
are excluded from the ingredient pools and retained under `needs_review`, with
their recipe IDs, categories, original names, and reasons. These exclusions mean
the counts are conservative and may change after review. A category's recipe count
still includes recipes containing excluded entries.

Only the structured ingredient lists are counted; ingredients mentioned solely in
instructions are not extracted. Frequency describes these cookbook transcriptions,
not ingredient compatibility or a dietary classification.

## Rebuilding and reviewing

From the repository root, run:

```powershell
python scripts/build_salad_ingredient_frequencies.py
```

The script uses the Python standard library and writes the frequency JSON file.
Update its `EXCEPTIONS` or `FAMILIES` mappings to resolve entries or adjust grouping,
then rebuild. Edit the source recipes for transcription corrections.

The source currently includes three cookbooks and 185 recipes. It has formatting
defects: a missing comma, stray backticks, a trailing comma, consecutive root
objects, and two cookbooks sharing an object with repeated metadata keys. The
script repairs those known structural defects **in memory only**, preserving all
three cookbooks. It rejects remaining duplicate JSON keys and duplicate recipe IDs,
and checks that every source recipe record was recovered. Recovery details are
recorded in `source_read_notes`. The original source file remains unchanged and
still needs repair before it can be fetched directly as JSON in a browser.

Cookbook metadata is retained once at the top level for page-level attribution.

## Generator prototype

The Salad Spinner page includes `cookbook-viz/salad-ingredient-generator.html`
below the existing recipe picker. Its three buttons spin five ingredient columns,
using the stored weights without replacement. Each spin replaces all five
ingredients. Water and seasonings are currently included, and there are no locks.
Motion stops from left to right; reduced-motion preferences show results immediately.

The behavior checks use Node.js and no third-party packages:

```powershell
node scripts/test_salad_ingredient_generator.cjs
```

These checks exercise selection, animation lifecycle, data loading and recovery
with a simulated DOM. To review the actual layout and animation, serve the Jekyll
site and open the Salad Spinner page on desktop and mobile widths.
