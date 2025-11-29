from app.chatbot import SimpleChatbot

def test_flow_consistency():
    bot = SimpleChatbot()
    s = "sess123"
    r1 = bot.respond(s, "Hello")
    assert r1["intent"] == "greeting"
    # now send order message
    r2 = bot.respond(s, "I want to check my order status")
    assert r2["intent"] == "order_status"
    # ensure session stored last intent
    assert bot.sessions[s]["last_intent"] == "order_status"