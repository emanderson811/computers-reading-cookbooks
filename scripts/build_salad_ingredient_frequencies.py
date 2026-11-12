"""Build category ingredient pools without modifying the cookbook transcriptions.

Run from the repository root: python scripts/build_salad_ingredient_frequencies.py
Uses only the Python standard library. See docs/salad-ingredient-frequencies.md.
"""

import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/data/salad-ingredients.json"
OUTPUT = ROOT / "assets/data/salad-ingredient-frequencies.json"
CATEGORIES = ("fruit", "jello", "vegetable")

# Exact exceptions take precedence over the ingredient-family rules below.
# None means the transcription needs a decision before it joins the spinner.
EXCEPTIONS = {
    "beets and red cabbage. both cooked and chopped.": ["beets", "red cabbage"],
    "broken lettuce and romaine": ["lettuce", "romaine lettuce"],
    "salt and pepper": ["salt", "black pepper"],
    "salt and celery seed to taste": ["salt", "celery seed"],
    "remaining brown sugar & flour": ["brown sugar", "flour"],
    "beet juice & pineapple combined": None,
    "celery and apples or pineapple and grapes": None,
    "royal anne cherries, pitted and stuffed with cream cheese and nuts":
        ["royal anne cherries", "cream cheese", "nuts (type unspecified)"],
    "cottage cheese (cream cheese can be substituted)": ["cottage cheese"],
    "large marshmallows - cut up - or 1 1/2 cups small marshmallows": ["marshmallows"],
    "green pepper stems": None,
    "green mangol diced": None,
    "red mangol diced (for color)": None,
    "fruit to taste": None,
    "seedless grapes or fresh": None,
    "wilderness lemon (or a little less)": None,
    "salad oil (or less)": ["salad oil"],
    "hot peach syrup (or peach syrup & water)": None,
    "mixed pineapple and apricot juice": None,
    "juice from bing cherries and enough cold water to make a cup.": None,
    "lemon gelatin, dissolved in 2 cups boiling water, and a little green coloring":
        ["lemon gelatin", "water", "green food coloring"],
    "plain gelatin combined with 2 tbsp. cold water": ["unflavored gelatin", "water"],
    "sweet pepper (red or green)": ["bell peppers (color unspecified)"],
    "eggs hard boiled and diced": ["hard-boiled eggs"],
    "kraft mint-flavored apple jelly": ["mint-flavored apple jelly"],
    "devonshire plain melba toast, broken": ["melba toast"],
}

# Order matters: juices, seasonings and processed ingredients precede produce.
# Preparation and fruit shape are combined; flavors and named varieties remain distinct.
FAMILIES = [
    (r"\bcelery seed\b", "celery seed"),
    (r"\balmond extract\b", "almond extract"),
    (r"\bonion flavoring\b", "onion flavoring"),
    (r"\bmustard seed\b", "mustard seed"),
    (r"\bdill seed\b", "dill seed"),
    (r"\bdry mustard\b", "dry mustard"),
    (r"\bhorseradish mustard\b", "horseradish mustard"),
    (r"\b(?:prepared mustard|mustard)\b", "mustard"),
    (r"\b(?:cayenne pepper)\b", "cayenne pepper"),
    (r"\b(?:apple cider|cider) vinegar\b", "cider vinegar"),
    (r"\bwhite vinegar\b", "white vinegar"),
    (r"\bsalad vinegar\b", "salad vinegar"),
    (r"\bsweet pickle vinegar\b", "sweet pickle vinegar"),
    (r"\bvinegar and oil dressing\b", "vinegar and oil dressing"),
    (r"\bvinegar\b", "vinegar"),
    (r"\b(?:worchester|worcestershire) sauce\b", "worcestershire sauce"),
    (r"\btabasco sauce\b", "tabasco sauce"),
    (r"\b(?:brown sugar)\b", "brown sugar"),
    (r"\b(?:powdered sugar|confectioner sugar)\b", "powdered sugar"),
    (r"\bsugar\b", "sugar"),
    (r"\b(?:corn starch|cornstarch)\b", "cornstarch"),
    (r"\bflour\b", "flour"),
    (r"\b(?:apple sauce|applesauce)\b", "applesauce"),
    (r"\b(?:whole cranberry sauce|jellied cranberry sauce|cranberry sauce)\b", "cranberry sauce"),
    (r"\borange cranberry relish\b", "orange cranberry relish"),
    (r"\bcherry pie filling\b", "cherry pie filling"),
    (r"\blemon pie filling\b", "lemon pie filling"),
    (r"\bpeach pie filling\b", "peach pie filling"),
    (r"\borange tapioca pudding mix\b", "orange tapioca pudding mix"),
    (r"\bvanilla tapioca pudding mix\b", "vanilla tapioca pudding mix"),
    (r"\borange sherb(?:er|e)t\b", "orange sherbet"),
    (r"\bvanilla ice cream\b", "vanilla ice cream"),
    (r"\bfrozen orange juice\b", "frozen orange juice concentrate"),
    (r"\borange juice\b", "orange juice"),
    (r"\b(?:pineapple juice|juice from pineapple|pineapple syrup|syrup from pineapple)\b", "pineapple juice"),
    (r"\b(?:liquid from cherries)\b", "cherry juice"),
    (r"\bstrawberry juice\b", "strawberry juice"),
    (r"\bpear juice\b", "pear juice"),
    (r"\bpeach syrup\b", "peach syrup"),
    (r"\b(?:juice from canned fruit|reserved fruit liquid)\b", "canned fruit juice"),
    (r"\bapricot nectar\b", "apricot nectar"),
    (r"\b(?:lemon juice|lemon, juiced|lemons, juiced)\b", "lemon juice"),
    (r"\borange rind\b", "orange rind"),
    (r"\blemon with rind\b", "lemon with rind"),
    (r"\bblack cherry (?:jello|gelatin)\b", "black cherry gelatin"),
    (r"\b(?:raspberry|rasberry) (?:jello|gelatin)\b", "raspberry gelatin"),
    (r"\blemon(?:-flavored)? (?:jello|gelatin)\b", "lemon gelatin"),
    (r"\blime (?:jello|gelatin)\b", "lime gelatin"),
    (r"\borange (?:jello|gelatine?)\b", "orange gelatin"),
    (r"\bcherry jello\b", "cherry gelatin"),
    (r"\bstrawberry (?:jello|gelatin)\b", "strawberry gelatin"),
    (r"\bpeach gelatin\b", "peach gelatin"),
    (r"\bred jello\b", "red gelatin (flavor unspecified)"),
    (r"\b(?:unflavored gelatin|knox gelatin|gelatine)\b", "unflavored gelatin"),
    (r"\bcream cheese\b", "cream cheese"),
    (r"\b(?:cottage cheese|cbttage cheese)\b", "cottage cheese"),
    (r"\bamerican cheese\b", "american cheese"),
    (r"\bcheddar cheese\b", "cheddar cheese"),
    (r"\bparmesan cheese\b", "parmesan cheese"),
    (r"\bswiss cheese\b", "swiss cheese"),
    (r"\bcheese whiz\b", "cheese whiz"),
    (r"\bcheese\b", "cheese (type unspecified)"),
    (r"\bsour cream\b", "sour cream"),
    (r"\b(?:sweetened cond\. milk)\b", "sweetened condensed milk"),
    (r"\bwhipped carnation instant\b", "whipped instant milk"),
    (r"\bmilk\b", "milk"),
    (r"\bcool whip\b", "cool whip"),
    (r"\bdream whip\b", "dream whip"),
    (r"\bcream\b", "cream"),
    (r"\bmayonnaise\b", "mayonnaise"),
    (r"\bmiracle whip\b", "miracle whip"),
    (r"\bfrench dressing\b", "french dressing"),
    (r"\bitalian dressing\b", "italian dressing"),
    (r"\bthousand island dressing\b", "thousand island dressing"),
    (r"\bdressing\b", "salad dressing (type unspecified)"),
    (r"\bbutter\b", "butter"),
    (r"\bsalad oil\b", "salad oil"),
    (r"\bcorn oil\b", "corn oil"),
    (r"\bcooking oil\b", "cooking oil"),
    (r"\bmarshmall?ows\b|\bmarshmellows\b", "marshmallows"),
    (r"\bblack walnuts\b", "black walnuts"),
    (r"\bwalnut(?:s| meats)?\b", "walnuts"),
    (r"\bpecan(?:s| meats)?\b", "pecans"),
    (r"\bpeanuts\b", "peanuts"),
    (r"\balmond(?:s| meats)?\b", "almonds"),
    (r"\b(?:nuts|nut ?meats)\b", "nuts (type unspecified)"),
    (r"\b(?:coconut|cocoanut)\b", "coconut"),
    (r"\b(?:red hots)\b", "red hots candy"),
    (r"\bbacon\b", "bacon"),
    (r"\bhard (?:boiled|cooked) eggs\b", "hard-boiled eggs"),
    (r"\begg yolks\b", "egg yolks"),
    (r"\beggs?\b", "eggs"),
    (r"\bcooked shrimp\b", "cooked shrimp"),
    (r"\btuna\b", "tuna"),
    (r"\bcorned beef\b", "corned beef"),
    (r"\banchovy fillets\b", "anchovy fillets"),
    (r"\b(?:sauerkraut|kraut)\b", "sauerkraut"),
    (r"\bred cabbage\b", "red cabbage"),
    (r"\bcabbage\b", "cabbage"),
    (r"\bcelery\b", "celery"),
    (r"\bcarrots?\b", "carrots"),
    (r"\bpickled beets\b", "pickled beets"),
    (r"\bbeets\b", "beets"),
    (r"\bcucumbers?\b", "cucumbers"),
    (r"\bgreen onions?\b", "green onions"),
    (r"\bfried onions\b", "fried onions"),
    (r"\bonions?\b", "onions"),
    (r"\bgreen peppers?\b", "green bell peppers"),
    (r"\bred peppers?\b", "red bell peppers"),
    (r"\bpeppers\b", "bell peppers (color unspecified)"),
    (r"\bpepper\b", "black pepper"),
    (r"\bpotatoes\b", "potatoes"),
    (r"\b(?:green beans)\b", "green beans"),
    (r"\b(?:wax beans|yellow beans)\b", "wax beans"),
    (r"\bkidney beans\b", "kidney beans"),
    (r"\bpeas\b", "peas"),
    (r"\bturnips\b", "turnips"),
    (r"\btomatoes\b|\btomato wedges\b", "tomatoes"),
    (r"\bspinach\b", "spinach"),
    (r"\blettuce\b", "lettuce"),
    (r"\bgarlic\b", "garlic"),
    (r"\bhorseradish\b", "horseradish"),
    (r"\b(?:pimento|pimentos|pimentoes|pimiento)\b", "pimentos"),
    (r"\bstuffed (?:olives|olvies)\b", "stuffed olives"),
    (r"\bgreen olives\b", "green olives"),
    (r"\bripe olives\b", "ripe olives"),
    (r"\bdill pickles\b", "dill pickles"),
    (r"\b(?:sweet pickle relish|sweet relish)\b", "sweet pickle relish"),
    (r"\bsweet pickles\b", "sweet pickles"),
    (r"\b(?:maraschino|marachino) cherries\b", "maraschino cherries"),
    (r"\bbing cherries\b", "bing cherries"),
    (r"\bwhite cherries\b", "white cherries"),
    (r"\bred cherries\b", "red cherries"),
    (r"\bcranberries\b", "cranberries"),
    (r"\bapples\b|\bapple\b", "apples"),
    (r"\bbananas?\b", "bananas"),
    (r"\bapricots?\b", "apricots"),
    (r"\bpineapple\b", "pineapple"),
    (r"\bmandarin orange(?:s| slices)?\b", "mandarin oranges"),
    (r"\boranges?\b", "oranges"),
    (r"\bgrapefruit\b", "grapefruit"),
    (r"\bgreen (?:seedless )?grapes\b", "green grapes"),
    (r"\bwhite (?:seedless )?grapes\b", "white grapes"),
    (r"\btokay grapes\b", "tokay grapes"),
    (r"\bred grapes\b", "red grapes"),
    (r"\bpeaches\b|\bpeach slices\b", "peaches"),
    (r"\bpears?\b", "pears"),
    (r"\bstrawberries\b", "strawberries"),
    (r"\braspberries\b", "raspberries"),
    (r"\bmelon balls\b", "melon"),
    (r"\bfruit cocktail\b|\bsalad fruit\b", "fruit cocktail"),
    (r"\bprunes\b", "prunes"),
    (r"\bmacaroni\b", "macaroni"),
    (r"\bwater\b", "water"),
    (r"\bsalt\b", "salt"),
]


def load_cookbooks():
    """Recover known formatting defects in memory, then decode all cookbook objects."""
    original = SOURCE.read_text(encoding="utf-8-sig")
    source = original
    repairs = []
    missing_comma = re.compile(r'("organization"\s*:\s*"[^"\n]*")\s*("recipes"\s*:)')
    source, count = missing_comma.subn(r"\1,\n\2", source)
    if count:
        repairs.append(f"Inserted {count} missing comma(s) after organization in memory.")
    count = source.count("{``")
    if count:
        source = source.replace("{``", "{")
        repairs.append(f"Removed stray backticks from {count} object(s) in memory.")
    # Match punctuation only outside JSON string literals.
    trailing = re.compile(r'("(?:\\.|[^"\\])*"\s*)|(,\s*(?=[}\]]))')
    count = 0

    def remove_trailing(match):
        nonlocal count
        if match.group(1) is not None:
            return match.group(1)
        count += 1
        return ""

    source = trailing.sub(remove_trailing, source)
    if count:
        repairs.append(f"Removed {count} trailing comma(s) in memory.")
    source, count = re.subn(r'\],\s*("cookbook_title"\s*:)', r']}\n{\1', source)
    if count:
        repairs.append(f"Separated {count} cookbook header(s) sharing a root object in memory.")

    def reject_duplicate_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result

    decoder = json.JSONDecoder(object_pairs_hook=reject_duplicate_keys)
    cookbooks = []
    offset = 0
    while offset < len(source):
        if source[offset].isspace():
            offset += 1
            continue
        cookbook, offset = decoder.raw_decode(source, offset)
        if not isinstance(cookbook, dict) or not isinstance(cookbook.get("recipes"), list):
            raise ValueError("Expected cookbook objects with recipe lists")
        cookbooks.append(cookbook)
    if len(cookbooks) > 1:
        repairs.append(f"Read {len(cookbooks)} consecutive cookbook objects separately.")
    expected = len(re.findall(r'"recipe_id"\s*:', original))
    actual = sum(len(cookbook["recipes"]) for cookbook in cookbooks)
    if actual != expected:
        raise ValueError(f"Recovered {actual} of {expected} recipe records")
    if SOURCE.read_text(encoding="utf-8-sig") != original:
        raise RuntimeError("Source changed during generation; please rerun")
    return cookbooks, repairs


def normalize(name):
    text = re.sub(r"\s+", " ", name.strip().lower())
    if text in EXCEPTIONS:
        result = EXCEPTIONS[text]
        return result, "Ambiguous or incomplete transcription" if result is None else None
    if re.search(r"\bor\b", text):
        return None, "Alternative ingredients; no single ingredient selected"
    for pattern, canonical in FAMILIES:
        if re.search(pattern, text):
            return [canonical], None
    return [text.rstrip("., ")], None


def build():
    cookbooks, repairs = load_cookbooks()
    counts = {category: Counter() for category in CATEGORIES}
    variants = {category: defaultdict(set) for category in CATEGORIES}
    recipe_counts = Counter()
    review = []
    ids = set()
    for cookbook in cookbooks:
        for recipe in cookbook["recipes"]:
            recipe_id = recipe["recipe_id"]
            if recipe_id in ids:
                raise ValueError(f"Duplicate recipe ID: {recipe_id}")
            ids.add(recipe_id)
            categories = recipe["category"]
            if isinstance(categories, str):
                categories = [categories]
            categories = [category for category in CATEGORIES if category in categories]
            if not categories:
                continue
            found = set()
            for ingredient in recipe["ingredients"]:
                name = ingredient["name"]
                normalized, reason = normalize(name)
                if normalized is None:
                    review.append({"recipe_id": recipe_id, "categories": categories,
                                   "source_name": name, "reason": reason})
                    continue
                found.update(normalized)
                for category in categories:
                    for canonical in normalized:
                        variants[category][canonical].add(name)
            for category in categories:
                recipe_counts[category] += 1
                counts[category].update(found)
    result = {
        "schema_version": 1,
        "source_file": "assets/data/salad-ingredients.json",
        "source_recipe_count": len(ids),
        "counting_method": "Number of source recipes containing each normalized ingredient, once per recipe per category. Counts use ingredient lists only, not instruction text.",
        "weighting_method": "sqrt(recipe_count), rounded to six decimals; sample without replacement and exclude locked ingredients from new draws.",
        "normalization_notes": [
            "Preparation, size, optional status, and fresh/frozen/canned forms are grouped where matched by explicit ingredient-family rules. Original names are retained in source_names.",
            "Juices, gelatin flavors, named nut varieties, and named cheeses remain distinct. Cream preparations and marshmallow sizes are grouped.",
            "Explicit compound entries are split where unambiguous. Unresolved alternatives and unclear transcriptions are excluded and listed in needs_review.",
            "Water and seasonings remain available; the spinner can filter them without rebuilding counts.",
        ],
        "source_read_notes": repairs,
        "cookbooks": [{"title": c["cookbook_title"], "organization": c["organization"],
                       "recipe_count": len(c["recipes"])} for c in cookbooks],
        "categories": {},
        "needs_review": review,
    }
    for category in CATEGORIES:
        ingredients = [
            {"name": name, "recipe_count": count, "weight": round(math.sqrt(count), 6),
             "source_names": sorted(variants[category][name], key=lambda value: (value.casefold(), value))}
            for name, count in sorted(counts[category].items(), key=lambda item: (-item[1], item[0]))
        ]
        result["categories"][category] = {
            "label": {"fruit": "Fruit", "jello": "Jello", "vegetable": "Vegetable"}[category],
            "recipe_count": recipe_counts[category],
            "ingredient_count": len(ingredients),
            "ingredients": ingredients,
        }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for category, data in result["categories"].items():
        print(f"{category}: {data['recipe_count']} recipes, {data['ingredient_count']} ingredients")
    print(f"{len(review)} source entries need review; source file unchanged.")


if __name__ == "__main__":
    build()
