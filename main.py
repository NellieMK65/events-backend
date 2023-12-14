from fastapi import FastAPI

# initialize it
app = FastAPI()

# define a route
@app.get('/')
def index():
    return {"message": "Welcome to my first api"}
