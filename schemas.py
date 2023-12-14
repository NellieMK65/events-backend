# this allows us to create schemas of what our app accepts
from pydantic import BaseModel

class EventSchema(BaseModel):
    title: str
    description: str
    image: str
    location: str
    price: int
    start_date: str
    end_date: str
