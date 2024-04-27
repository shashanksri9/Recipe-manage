class Recipe:
    def _init_(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def _str_(self):
        return f"{self.name}:\nIngredients: {', '.join(self.ingredients)}\nInstructions: {self.instructions}"

class RecipeManager:
    def _init_(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def display_recipes(self):
        for idx, recipe in enumerate(self.recipes, start=1):
            print(f"\nRecipe {idx}:")
            print(recipe)

# Example usage
recipe1 = Recipe("Spaghetti Carbonara", ["spaghetti", "bacon", "eggs", "parmesan cheese", "black pepper"], "1. Cook spaghetti. 2. Fry bacon. 3. Mix eggs and parmesan. 4. Combine all ingredients.")
recipe2 = Recipe("Chocolate Cake", ["flour", "sugar", "cocoa powder", "butter", "eggs", "vanilla extract"], "1. Mix dry ingredients. 2. Beat butter and sugar. 3. Add eggs and vanilla. 4. Combine wet and dry ingredients. 5. Bake.")

manager = RecipeManager()
manager.add_recipe(recipe1)
manager.add_recipe(recipe2)

manager.display_recipes()
