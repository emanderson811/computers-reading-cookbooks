(() => {
    document.querySelectorAll('.salad-generator').forEach((container) => {
        if (container.dataset.initialized) return;
        container.dataset.initialized = 'true';

        const buttons = [...container.querySelectorAll('[data-category]')];
        const machine = container.querySelector('.salad-generator-machine');
        const label = container.querySelector('.salad-generator-label');
        const reels = [...container.querySelectorAll('.salad-generator-reel')];
        const status = container.querySelector('.salad-generator-status');
        const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
        let categories = null;
        let busy = false;

        function token(name) {
            const node = document.createElement('span');
            node.className = 'salad-generator-token';
            node.textContent = name;
            return node;
        }

        async function loadCategories() {
            if (categories) return categories;
            const response = await fetch(container.dataset.ingredientsUrl);
            if (!response.ok) throw new Error('Ingredient request failed');
            const data = await response.json();
            const loaded = {};
            buttons.forEach((button) => {
                const key = button.dataset.category;
                const category = data.categories?.[key];
                if (!Array.isArray(category?.ingredients)) throw new Error('Missing ingredient pool');
                const names = new Set();
                const ingredients = category.ingredients.filter((ingredient) => {
                    if (typeof ingredient?.name !== 'string' || !ingredient.name.trim() ||
                        !Number.isFinite(ingredient.weight) || ingredient.weight <= 0) return false;
                    const name = ingredient.name.trim().toLowerCase();
                    if (names.has(name)) return false;
                    names.add(name);
                    return true;
                });
                if (ingredients.length < reels.length) throw new Error('Not enough distinct ingredients');
                loaded[key] = { label: category.label || key, ingredients };
            });
            categories = loaded;
            return categories;
        }

        // Recalculate the total after every draw: five weighted picks without repeats.
        function chooseIngredients(ingredients) {
            const pool = [...ingredients];
            return reels.map(() => {
                const total = pool.reduce((sum, ingredient) => sum + ingredient.weight, 0);
                let remaining = Math.random() * total;
                let index = pool.length - 1;
                for (let i = 0; i < pool.length; i += 1) {
                    remaining -= pool[i].weight;
                    if (remaining < 0) {
                        index = i;
                        break;
                    }
                }
                return pool.splice(index, 1)[0];
            });
        }

        async function spinReel(reel, ingredient, pool, index) {
            const track = reel.querySelector('.salad-generator-track');
            const accessibleName = reel.querySelector('.salad-generator-ingredient');
            // Keep the final result out of the accessibility tree until this reel stops.
            if (!reducedMotion.matches && typeof track.animate === 'function') {
                const steps = 16 + index * 4;
                const tokens = Array.from({ length: steps }, () =>
                    token(pool[Math.floor(Math.random() * pool.length)].name));
                tokens.push(token(ingredient.name));
                track.replaceChildren(...tokens);
                reel.classList.add('is-spinning');
                const height = reel.querySelector('.salad-generator-window').clientHeight;
                const animation = track.animate([
                    { transform: 'translateY(0)' },
                    { transform: `translateY(-${height * steps}px)` }
                ], { duration: 1200 + index * 260, easing: 'cubic-bezier(.15,.55,.25,1)', fill: 'forwards' });
                const finishEarly = () => { if (reducedMotion.matches) animation.finish(); };
                reducedMotion.addEventListener('change', finishEarly);
                try {
                    await animation.finished;
                } finally {
                    reducedMotion.removeEventListener('change', finishEarly);
                    animation.cancel();
                    reel.classList.remove('is-spinning');
                }
            }
            track.replaceChildren(token(ingredient.name));
            accessibleName.textContent = ingredient.name;
        }

        async function spin(button) {
            if (busy) return;
            busy = true;
            buttons.forEach((control) => { control.disabled = true; });
            machine.setAttribute('aria-busy', 'true');
            status.textContent = categories ? 'Spinning the ingredients…' : 'Opening the ingredient cupboard…';
            try {
                const pools = await loadCategories();
                const category = pools[button.dataset.category];
                const selected = chooseIngredients(category.ingredients);
                buttons.forEach((control) => {
                    control.setAttribute('aria-pressed', String(control === button));
                });
                label.textContent = `Your ${category.label.toLowerCase()} salad remix`;
                status.textContent = 'Spinning the ingredients…';
                await Promise.all(reels.map((reel, index) =>
                    spinReel(reel, selected[index], category.ingredients, index)));
                status.textContent = `${category.label} salad: ${selected.map((ingredient) => ingredient.name).join(', ')}. Choose a category to spin again.`;
            } catch (error) {
                status.textContent = 'The ingredients could not be spun. Please choose a category to try again.';
            } finally {
                machine.setAttribute('aria-busy', 'false');
                buttons.forEach((control) => { control.disabled = false; });
                busy = false;
            }
        }

        buttons.forEach((button) => button.addEventListener('click', () => spin(button)));
    });
})();
