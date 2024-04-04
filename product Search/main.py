import uvicorn
from fastapi import FastAPI 
from fastapi.responses import RedirectResponse
from routes import index

app =FastAPI()

PORT = 8001

@app.get("/")
async def read_root():
    return RedirectResponse(url ="/docs")
   
app.include_router(index.router)