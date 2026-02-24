# Abhay Tiwari Portfolio - Backend

This is the Python-based backend for my personal portfolio, featuring an AI-driven chat assistant.

## Tech Stack
* **Framework:** FastAPI
* **Language:** Python 3.10+
* **Database:** MongoDB Atlas (Asynchronous via Motor)
* **AI Engine:** OpenRouter (google/gemini-2.0-flash-lite-preview-02-05:free)

## Key Features
* **Asynchronous API:** Built with FastAPI for high-performance, non-blocking requests.
* **Chat Persistence:** Automatically logs user queries and AI responses to MongoDB for session tracking.
* **AI Integration:** Context-aware responses based on my professional resume and NCC leadership experience.
* **Retry Logic:** Implemented a robust request wrapper to handle API rate-limiting gracefully.

## Setup
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Configure `.env` with `OPENROUTER_API_KEY` and `MONGO_DETAILS`.
5. Run the server: `uvicorn app.main:app --reload`
