from fastapi import FastAPI, HTTPException
from app.schemas import ChatRequest, ChatResponse
from app.chatbot import SimpleChatbot

app = FastAPI(title="Simple Chatbot API for QA Demo")
bot = SimpleChatbot(latency_ms=0)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    if not req.message or not req.message.strip():
        raise HTTPException(status_code=400, detail="message cannot be empty")
    session_id = req.session_id or "default_session"
    out = bot.respond(session_id, req.message)
    return ChatResponse(**out)