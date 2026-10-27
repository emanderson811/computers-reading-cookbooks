(() => {
    // The include can appear more than once on a page.
    document.querySelectorAll('.salad-recipe-randomizer').forEach((container) => {
        if (container.dataset.initialized) return;
        container.dataset.initialized = 'true';

        const button = container.querySelector('.salad-recipe-button');
        const status = container.querySelector('.salad-recipe-status');
        const card = container.querySelector('.salad-recipe-card');
        let recipes = [];
        let currentIndex = -1;

        function element(tag, text, className) {
            const node = document.createElement(tag);
            node.textContent = text;
            if (className) node.className = className;
            return node;
        }

        function renderText(text) {
            const body = document.createElement('div');
            body.className = 'salad-recipe-body';
            const lines = text.split(/\r?\n/).map((line) => line.trim()).filter(Boolean);
            // Keep ingredients and instructions in their original order.
            const direction = /^(?:\d+[.)]\s*)?(?:add|arrange|bake|beat|blend|boil|bring|chill|combine|cook|cover|cut|dissolve|drain|fold|heat|let|mix|peel|place|pour|refrigerate|serve|shred|soak|soften|sprinkle|stir|toss|turn|whip)\b/i;
            const quantity = /^(?:\d|[¼½¾⅓⅔⅛⅜⅝⅞]|one\b|two\b|three\b|four\b|five\b|six\b|a\s+(?:cup|can|package|pinch|dash)\b|pinch\b|dash\b)/i;
            let list = null;

            lines.forEach((line, index) => {
                const ingredient = !direction.test(line) && !/^\d+[.)]\s/.test(line) && (
                    (quantity.test(line) && line.length < 130 && !/[.!?]\s+[A-Z]/.test(line)) ||
                    (line.length < 65 && index < lines.length - 1 &&
                        /^(?:sliced|chopped|grated|miniature|maraschino|salt\b|pepper\b|lettuce\b|salad dressing\b|remaining\b)/i.test(line))
                );
                if (ingredient) {
                    if (!list) {
                        list = document.createElement('ul');
                        body.append(list);
                    }
                    list.append(element('li', line));
                } else {
                    list = null;
                    body.append(element('p', line));
                }
            });
            return body;
        }

        function showRecipe() {
            // Choose uniformly from the other recipes to avoid immediate repeats.
            let index = Math.floor(Math.random() * (recipes.length - (currentIndex >= 0 ? 1 : 0)));
            if (currentIndex >= 0 && index >= currentIndex) index += 1;
            if (recipes.length === 1) index = 0;
            currentIndex = index;
            const recipe = recipes[index];
            const heading = element('h2', recipe.title, 'salad-recipe-title');
            const credit = document.createElement('footer');
            credit.className = 'salad-recipe-credit';
            credit.append('From ', element('cite', recipe.cookbook_title), ' — ', recipe.organization);
            card.replaceChildren(heading, renderText(recipe.full_text), credit);
            card.hidden = false;
            status.textContent = '';
            button.textContent = 'Show Me Another Salad Recipe';
        }

        async function loadRecipes() {
            button.disabled = true;
            status.textContent = 'Opening the recipe box…';
            try {
                const response = await fetch(container.dataset.recipesUrl);
                if (!response.ok) throw new Error('Recipe request failed');
                const data = await response.json();
                if (!Array.isArray(data)) throw new Error('Expected a recipe list');
                recipes = data.filter((recipe) => recipe &&
                    ['title', 'full_text', 'cookbook_title', 'organization'].every(
                        (key) => typeof recipe[key] === 'string' && recipe[key].trim()
                    ));
                if (!recipes.length) throw new Error('No recipes found');
                showRecipe();
            } catch (error) {
                status.textContent = 'The recipe box could not be opened. Please try again.';
                button.textContent = 'Try Again';
            } finally {
                button.disabled = false;
            }
        }

        button.addEventListener('click', () => recipes.length ? showRecipe() : loadRecipes());
    });
})();
