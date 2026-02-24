import requests
import os
import json
import time
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()


def get_ai_response(user_message: str) -> str:
    """Fetches AI response with a retry loop and comprehensive resume context."""

    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        print("CRITICAL ERROR: OPENROUTER_API_KEY not found in .env file.")
        return "System Error: Missing API Key."

    resume_context = """
    You are the AI Assistant for Abhay Tiwari. [cite: 3]
    CONTACT: +91 8793195963, abhaytiwari3415@gmail.com. [cite: 2, 4]
    SUMMARY: Full-Stack Developer with 4 months of production experience in React, Next.js, and FastAPI. [cite: 5]
    EDUCATION: BCA student at RTMNU (2023-2026). [cite: 34, 35, 37]
    EXPERIENCE: Full-Stack Developer Intern at Label Lift (Oct 2025 – Feb 2026). [cite: 11, 12, 13] 
    Key work: Engineered features using Next.js and FastAPI, optimized RESTful APIs, and managed PostgreSQL databases. [cite: 14, 16]
    PROJECTS: 
    1. Therapist Maya: Mental health platform using Next.js, TypeScript, and Framer Motion. Live link: https://therapist-maya.vercel.app/ [cite: 20, 21, 22]
    2. NCC Cadet Attendance Tracker: Daily attendance system for college unit using JS and Local Storage. Live link: https://vmv-ncc-attendance-tracker.netlify.app/ [cite: 24, 25, 26]
    3. Ark Customizations: Live commercial site (arkcustomizations.in) built with React and TypeScript. [cite: 31, 32]
    4. Mahindra Lifespaces: Pixel-perfect Figma to Next.js conversion. Live link: https://mahindra-lifespaces.netlify.app/ [cite: 28, 29, 30]
    LEADERSHIP: NCC Senior Rank (CQMS). Managed large teams and high-pressure events. [cite: 40, 41]
    SKILLS: React.js, Next.js, TypeScript, Python, FastAPI, PostgreSQL, Tailwind CSS, and Git/GitHub. [cite: 8, 9]

    INSTRUCTION: Answer briefly and professionally as Abhay's assistant. If info is missing, suggest contacting him directly.
    """

    # Retry mechanism: Attempt the request up to 3 times
    for attempt in range(3):
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                data=json.dumps({
                    "model": "google/gemma-3-27b-it:free",
                    "messages": [
                        {"role": "user", "content": f"{resume_context}\n\nUSER QUESTION: {user_message}"}
                    ],
                }),
                timeout=15
            )

            result = response.json()

            if "choices" in result:
                content = result['choices'][0]['message'].get('content')
                if content:
                    return content

            # If the provider is busy (Rate Limit 429) or server error (500), wait and retry
            if response.status_code in [429, 500, 503]:
                print(
                    f"Attempt {attempt + 1} failed with status {response.status_code}. Retrying...")
                time.sleep(2)  # Wait 2 seconds before retrying
                continue

        except requests.exceptions.RequestException as e:
            print(f"Connection attempt {attempt + 1} failed: {e}")
            time.sleep(1)

    return "Abhay's AI is currently receiving many requests! Please try again in a few seconds or contact him at abhaytiwari3415@gmail.com."
