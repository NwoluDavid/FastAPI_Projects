from fastapi import APIRouter
from fastapi.responses import JSONResponse
from model import Event
from services import process_booking

event_booking_router =APIRouter(prefix="/booking", tags=["client"])
 
@event_booking_router.post("/" , response_model=Event)
async def event_booking(booking: Event):
    results = await process_booking(booking)
    return JSONResponse(status_code=201, content={"data": results, "message": "Booking successful"})



