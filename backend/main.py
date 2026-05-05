# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import get_ai_response
from fastapi.middleware.cors import CORSMiddleware

import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# CORS configuration
allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "AI Chatbot API is running 🚀"}

@app.post("/chat")
def chat(req: ChatRequest):
    if not req.message.strip():
        return {"response": "Please enter a message"}

    reply = get_ai_response(req.message)
    return {"response": reply}