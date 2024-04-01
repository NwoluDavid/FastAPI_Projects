from fastapi import FastAPI,  Body
from model import *

app=FastAPI()

# Route for user registration
@app.post("/register")
async def register_user(user: UserRegistration):
    return {"user": user.model_dump(), "message":"user registered successfully"}