from pydantic import BaseModel, Field, EmailStr
from datetime import date
from typing import List, ClassVar

available_ticket_types = ['standard', 'premium', 'vip']

class Ticket(BaseModel):
    ticket_type: str= Field(description="choose the ticket type" , examples=['standard', 'premium', 'vip'])
    
class Attendee(BaseModel):
    name:str= Field(min_length=3 , max_length =50 , description="Name of the attendee" , examples=["Jonh Mac"], title="Name", pattern="^[a-zA-Z]")
    email: EmailStr
    age : int= Field(gt=0 , lt=110, description="Age of attendee", examples=[25], title="Age")

class Event ( BaseModel):
    name: str =Field(min_length=3 , max_length =50 , description="Name of the Event" , examples=["TechSpark Summit"], title="Name", pattern="^[a-zA-Z]")
    date: date 
    location: str =Field(min_length=3 , max_length =50 , description="address of the location" , examples=["Royal Albert Hall London, UK"], pattern="^[a-zA-Z]")
    ticket_types:Ticket
    attendee: Attendee
    
    class Config:
        orm_mode = True
    
    