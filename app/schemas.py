from pydantic import BaseModel


class ChatRequest(BaseModel):
    """class ChatRequest"""
    message: str


class ChatResponse(BaseModel):
    """class ChatResponse"""
    reply: str
