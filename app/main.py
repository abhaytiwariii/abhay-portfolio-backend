import motor.motor_asyncio
import os
from datetime import datetime
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import ChatRequest, ChatResponse
from app.services.ai_service import get_ai_response

load_dotenv()

app = FastAPI(title="Abhay Portfolio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database Connection
MONGO_DETAILS = os.getenv("MONGO_DETAILS")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.abhay_portfolio
chat_collection = database.get_collection("chat_history")


@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    # 1. Fetch AI Response
    ai_reply = get_ai_response(request.message)

    # 2. Asynchronous Logging 
    try:
        await chat_collection.insert_one({
            "user_query": request.message,
            "ai_response": ai_reply,
            "timestamp": datetime.utcnow()
        })
    except Exception as e:
        print(f"DB Error: {e}")

    return {"reply": ai_reply}
