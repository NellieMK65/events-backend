from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, VARCHAR, DateTime, Integer, TIMESTAMP

# Create a base model
Base = declarative_base()

# definining events model
class Event(Base):
    __tablename__ = "events"

    # define columns
    id = Column(Integer(), primary_key=True)
    title = Column(Text())
    description = Column(VARCHAR)
    image = Column(VARCHAR)
    location = Column(Text())
    price = Column(Integer())
    start_date = Column(DateTime())
    end_date = Column(DateTime())
    created_at = Column(TIMESTAMP)
