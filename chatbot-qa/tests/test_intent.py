from app.chatbot import detect_intent

def test_detect_greeting():
    intent, score = detect_intent("Hello there!")
    assert intent == "greeting"
    assert score > 0

def test_detect_unknown():
    intent, score = detect_intent("qwerty asdfg")
    assert intent == "unknown"
    assert score == 0.0