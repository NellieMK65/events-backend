from fastapi import FastAPI, Depends, HTTPException, status, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db
from models import Event, User, Booking
from schemas import EventSchema, BookingSchema

# initialize it
app = FastAPI()

origins = ["*"]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"],
    )

# define a route
@app.get('/')
def index():
    return {"message": "Welcome to my first api"}

# get all events
@app.get('/events')
def events(db: Session = Depends(get_db)):
    events = db.query(Event).all()
    return events

# get a single event
@app.get('/events/{event_id}')
def event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()

    return event

# create an event
@app.post('/events')
def create_event(event: EventSchema, db: Session = Depends(get_db)):
    # unpacks a dict add passes it as key-value pairs
    # {"title": "Ngong"} -> title: "Ngong"
    new_event = Event(**event.model_dump())

    # adds the events to the transaction
    db.add(new_event)
    # commit the transaction
    db.commit()
    # get event from the db again
    db.refresh(new_event)
    return {"message": "Event created successfully", "event": new_event}

# update an event
@app.patch('/events/{event_id}')
def updated_event(event_id: int):
    return {"message":f"Event {event_id} created successfully"}

# delete an event
@app.delete('/events/{event_id}')
def delete_event(event_id: int, db: Session = Depends(get_db)):
    delete_event = db.query(Event).filter(Event.id == event_id).first()

    if delete_event == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event {event_id} does not exist")
    else:
        delete_event.delete()
        # running transaction
        db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

# creating a booking route
@app.post('/booking')
def book(booking: BookingSchema, db: Session = Depends(get_db)):
    # 1. Check if user exists using the phone number
    user = db.query(User).filter(User.phone == booking.phone).first()

    if user == None:
        # this means the user doesn`t exist so we create
        user = User(name=booking.name, phone=booking.phone)
        db.add(user)
        db.commit()

        # after creating user, now we can create a booking
        saved_booking = Booking(booking_date=booking.booking_date,
                          user_id= user.id,
                          event_id = booking.event_id)

        db.add(saved_booking)
        db.commit()

    else:
        # check if the user has already booked for an event
        saved_booking = db.query(Booking).filter(Booking.user_id == user.id,
                                           Booking.event_id == booking.event_id)

        if saved_booking == None:
            # this means the user has not booked the event
            saved_booking = Booking(booking_date=booking.booking_date,
                          user_id= user.id,
                          event_id = booking.event_id)

            db.add(saved_booking)
            db.commit()
        else:
            # if the user already has a booking we throw an error
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="Event already booked")


    return {"message": "Event booked successfully"}


