from fastapi import APIRouter ,Query
from fastapi.responses import JSONResponse
from model import *
from services import process_recipe , filter_recipe

recipe_router = APIRouter(prefix="/recipe",  tags=["users"])

@recipe_router.post("/")
async def create_recipe(recipe: Recipe):
    results = await process_recipe(recipe)
    return JSONResponse(status_code=201, content={"data": results, "message": "recipe created successfully"})



@recipe_router.get("/recipes")
async def get_recipes(title: str=Query(default=None, description="The title recipe" ) ,
ingredients: str = Query(default=None, description="the ingredient" ) ):
    
    title = title
    ingredients = ingredients
    
    message = filter_recipe (title , ingredients)