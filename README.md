# Chatbot QA Demo

A simple chatbot API plus QA tests demonstrating API testing, intent detection, flow testing, error handling, and latency tests.

## Run locally
1. Create venv and install:
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt

Start server:
  uvicorn app.main:app --reload --port 8000

3. Run tests:
  pytest -q

## What this demonstrates
- FastAPI REST endpoints
- Simple intent detection & chatbot logic
- Pytest tests for API, intents, flows, and latency
- Postman collection for manual QA
- GitHub Actions for CI