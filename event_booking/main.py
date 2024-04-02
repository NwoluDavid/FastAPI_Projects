from fastapi import FastAPI
from routes import event_booking_router

app =FastAPI()
app.include_router(event_booking_router)