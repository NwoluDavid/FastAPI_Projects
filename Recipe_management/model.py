from fastapi import HTTPException
import json
from pydantic import BaseModel, Field

class NutritionalInfo(BaseModel):
    calories: float= Field(gt=0 , lt=800, description="Amount of calories", examples=[12])
    fat: float=Field(gt=0 , lt=30, description="Amount of fat  in grams", examples=[12])
    protein: float =Field(gt=0 , lt=30, description="Amount of protien in grams", examples=[20])

class Ingredient(BaseModel):
    name: str=Field(min_length=3 , max_length =50 , description="Name of Ingridient" , examples=["Tomatos"], title="Ingredient")
    quantity: float =Field(gt=0 , lt=1000, description="Amount of in grams", examples=[20]) 

class Recipe(BaseModel):
    title: str =Field(min_length=3 , max_length =50 , description="Name of Recipe" , examples=["Shawarma"], title="Recipe")
    description: str = Field( description="descrieb the recipe") 
    instructions: str = Field( description="List the instructions for the recipe") 
    ingredients:list[Ingredient]= None
    nutritional_info: NutritionalInfo = None
    
# recipes_db = []    

# def get_recipes(title: str = None,
#                 ingredient: str = None,
#                 calories_less_than: float = None):
#     filtered_recipes = recipes_db

#     if title:
#         filtered_recipes = [r for r in filtered_recipes if title.lower() in r.title.lower()]
#     if ingredient:
#         filtered_recipes = [r for r in filtered_recipes if any(ingredient.lower() in i.name.lower() for i in r.ingredients)]
#     if calories_less_than:
#         filtered_recipes = [r for r in filtered_recipes if r.nutritional_info and r.nutritional_info.calories < calories_less_than]

#     return filtered_recipes


# def create_recipe(recipe: Recipe):
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