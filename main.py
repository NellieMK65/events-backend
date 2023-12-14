from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Event
from schemas import EventSchema

# initialize it
app = FastAPI()

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
def event():
    return {}

# create an event
@app.post('/events')
def create_event(event: EventSchema):
    print(event)
    return {"message": "Event created successfully"}

# update an event
@app.patch('/events/{event_id}')
def updated_event(event_id: int):
    return {"message":f"Event {event_id} created successfully"}

# delete an event
@app.delete('/events/{event_id}')
def delete_event(event_id: int):
    return {"message":f"Event {event_id} deleted successfully"}


