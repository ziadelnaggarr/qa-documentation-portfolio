# Simple rule-based chatbot + tiny keyword intent detector
from typing import Tuple
import random
import time

INTENT_KEYWORDS = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "bye": ["bye", "goodbye", "see you", "see ya"],
    "order_status": ["order", "status", "track", "tracking"],
    "complaint": ["not working", "error", "issue", "problem", "complaint"],
    "thank": ["thank", "thanks", "thx"]
}

DEFAULT_RESPONSES = {
    "greeting": ["Hello! How can I help you today?", "Hi there! What can I do for you?"],
    "bye": ["Goodbye! Have a great day.", "See you later!"],
    "order_status": ["Please provide your order ID and I will check the status.", "I can check that — what's the order number?"],
    "complaint": ["I’m sorry to hear that. Could you describe the issue in detail?", "I can escalate this to support — can you share more details?"],
    "thank": ["You’re welcome!", "Happy to help!"],
    "unknown": ["Sorry, I didn’t understand that. Can you rephrase?", "I’m not sure I got that — could you try again?"]
}

def detect_intent(text: str) -> Tuple[str, float]:
    """Simple keyword-based intent detection returning (intent, score)."""
    if not text:
        return "unknown", 0.0
    text_lower = text.lower()
    best_intent = "unknown"
    best_score = 0.0
    for intent, keywords in INTENT_KEYWORDS.items():
        hits = sum(1 for k in keywords if k in text_lower)
        if hits > 0:
            # naive scoring: hits / number_of_keywords
            score = hits / max(1, len(keywords))
            if score > best_score:
                best_score = score
                best_intent = intent
    return best_intent, best_score

class SimpleChatbot:
    def __init__(self, latency_ms: int = 0):
        self.latency_ms = latency_ms  # simulate latency if >0
        self.sessions = {}

    def respond(self, session_id: str, message: str):
        # simulate latency
        if self.latency_ms:
            time.sleep(self.latency_ms / 1000.0)

        intent, score = detect_intent(message)
        response_text = random.choice(DEFAULT_RESPONSES.get(intent, DEFAULT_RESPONSES["unknown"]))
        # keep simple dialogue memory (last message)
        self.sessions[session_id] = {"last_intent": intent, "last_message": message}
        return {"session_id": session_id, "message": response_text, "intent": intent, "score": round(score, 2)}