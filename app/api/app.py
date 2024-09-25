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

from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel
from typing import List , Dict
app = FastAPI()

# In-memory storage for users and messages
users = {}
messages = {}

#User model for registration 
class User(BaseModel):
    username:str 

     #messages model
    class Message(BaseModel):
        sender : str
        recipient : str
        content : str

        @app.post("/register", response_model=User)
        async def register_user(user :User):
            if user.username in users:
             raise HTTPException(status_code=400,detail="Username already exists")
            users[user.username] = user.username 
            return user
        
        @app.post("/send_message", response_model=Message)
        async def send_message(message: Message):
    if message.sender not in users:
        raise HTTPException(status_code=404, detail="Sender not registered")
    if message.recipient not in users:
        raise HTTPException(status_code=404, detail="Recipient not registered")
    
    messages.append(message)
 return message


@app.get("/messages/{recipient}", response_model=List[Message])
async def get_messages(recipient: str):
    if recipient not in users:
        raise HTTPException(status_code=404, detail="Recipient not registered")
    
    # Filter messages for the recipient
    received_messages = [msg for msg in messages if msg.recipient == recipient]
    return received_messages



