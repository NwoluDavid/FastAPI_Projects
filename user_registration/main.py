from fastapi import FastAPI,  Body
from model import UserRegistration, Responses
from fastapi.responses import JSONResponse

app=FastAPI()

# Route for user registration
@app.post("/register" , response_model=Responses)
async def register_user(user: UserRegistration):
    # return JSONResponse(status_code=201, content= {"user": user.model_dump(), "message":"user registered successfully"})
    return JSONResponse(status_code=201, content= {  "data" :user.model_dump(), "message" : "user registered successfully"})