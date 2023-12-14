from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# connect to our pg db
engine = create_engine("postgresql://admin:578xpmqofLZXq7pzsvs7yq3l6iTYi4U0@dpg-cltb9dq1hbls73ecgc8g-a.frankfurt-postgres.render.com/events_yrwj",
                       echo=True)

# Create connection with sessionmaker
SessionLocal = sessionmaker(bind=engine)

# def method to get db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
