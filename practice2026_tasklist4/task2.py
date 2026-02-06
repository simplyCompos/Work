# task2_rest_server.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from pathlib import Path

USERS_FILE = Path("users.json")
USERS_FILE.write_text("[]", encoding="utf-8") if not USERS_FILE.exists() else None

app = FastAPI(title="Crypto Users API")

class User(BaseModel):
    id: int
    username: str
    email: str

@app.get("/users")
def get_users():
    users = json.loads(USERS_FILE.read_text())
    return {"status": "success", "data": users, "message": "All users"}

@app.post("/users")
def create_user(user: User):
    users = json.loads(USERS_FILE.read_text())
    users.append(user.dict())
    USERS_FILE.write_text(json.dumps(users), encoding="utf-8")
    return {"status": "success", "data": user.dict(), "message": "User created"}
