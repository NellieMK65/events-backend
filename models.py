from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, VARCHAR, DateTime, Integer, TIMESTAMP

# Create a base model
Base = declarative_base()

# definining events model
class Event(Base):
    __tablename__ = "events"

    # define columns
    id = Column(Integer(), primary_key=True)
    title = Column(Text(), nullable=False)
    description = Column(VARCHAR, nullable=False)
    image = Column(VARCHAR, nullable=False)
    location = Column(Text(), nullable=False)
    price = Column(Integer(), nullable=False)
    start_date = Column(DateTime(), nullable=False)
    end_date = Column(DateTime(), nullable=False)
    created_at = Column(TIMESTAMP)

# the whole class represents a table, instances of the class represents a row
# and attributes represents columnss

class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(Text(), nullable=False)
    phone = Column(VARCHAR, nullable=False, unique=True)
