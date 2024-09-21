#add users

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory storage for users (you can replace this with a database later)
users_db = {}

# Pydantic model for user data
class User(BaseModel):
    username: str
    email: str

# Endpoint to add a new user
@app.post("/users/", response_model=User)
async def create_user(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists.")
    
    users_db[user.username] = user
    return user

# Endpoint to retrieve all users
@app.get("/users/", response_model=List[User])
async def get_users():
    return list(users_db.values())

# Run the app with: uvicorn script_name:app --reload