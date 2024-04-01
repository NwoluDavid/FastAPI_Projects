from model import Recipe
import json


async def process_recipe(recipe):
    ingredients = [{"name": ingredient.name, "quantity": ingredient.quantity} for ingredient in recipe.ingredients]

    result = {
        "recipe_title": recipe.title,
        "recipe_description": recipe.description,
        "recipe_instructions": recipe.instructions,
        "recipe_ingredients": ingredients,
        "nutritional_info": {
            "calories": recipe.nutritional_info.calories,
            "fat": recipe.nutritional_info.fat,
            "protein": recipe.nutritional_info.protein
        }
    }
    
    with open("recipes.json", "a") as file:
        json.dump(result, file)
        file.write('\n')
        
    return result



def read_recipes_from_file() -> list[Recipe]:
    with open("recipes.json", "r") as file:
        recipes_data = json.load(file)
        return [Recipe(**recipe) for recipe in recipes_data]

def filter_recipe(title,ingredients: str) -> list[Recipe]:
    recipes = read_recipes_from_file()

    if title:
        title = title.lower().strip()  # Convert provided title to lowercase
        recipes = [recipe for recipe in recipes if title in recipe.title.lower().strip()]
    if ingredients:
        recipes = [recipe for recipe in recipes if any(ingredient.lower() in [ing.name.lower() for ing in recipe.ingredients] for ingredient in ingredients.split(','))]

    return recipes

# from fastapi import HTTPException
# import json


# recipes_db = []

# async def create_recipe(recipe: Recipe):
#     recipes_db.append(recipe)
#     return recipe


# def get_recipe(recipe_id: int):
#     for recipe in recipes_db:
#         if recipe_id == id(recipe):
#             return recipe
#     raise HTTPException(status_code=404, detail="Recipe not found")

# def update_recipe(recipe_id: int, recipe: Recipe):
#     for i, existing_recipe in enumerate(recipes_db):
#         if recipe_id == id(existing_recipe):
#             recipes_db[i] = recipe
#             return recipe
#     raise HTTPException(status_code=404, detail="Recipe not found")

# def delete_recipe(recipe_id: int):
#     for i, recipe in enumerate(recipes_db):
#         if recipe_id == id(recipe):
#             del recipes_db[i]
#             return {"message": "Recipe deleted successfully"}
#     raise HTTPException(status_code=404, detail="Recipe not found")