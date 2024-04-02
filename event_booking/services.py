async def process_booking(booking):
    result ={
        "event_name" : booking.name,
        "event_date":booking.date.isoformat(),
        "event_location": booking.location,
        "attendee_name": booking.attendee.name,
        "attendee_age": booking.attendee.age,
        "attendee_email": booking.attendee.email,
        "event_ticket_type":booking.ticket_types. ticket_type,
        
    }
    
    return result