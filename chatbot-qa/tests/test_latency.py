import time
from app.chatbot import SimpleChatbot

def test_latency_threshold():
    bot = SimpleChatbot(latency_ms=150)
    s = "sessT"
    start = time.perf_counter()
    bot.respond(s, "Hello")
    elapsed_ms = (time.perf_counter() - start) * 1000
    # allow slight tolerance
    assert elapsed_ms >= 140
    assert elapsed_ms < 500  # ensure not ridiculously large