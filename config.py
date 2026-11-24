import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env", override=True, encoding="utf-8-sig")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_MODEL = "gemini-3.5-flash-lite"

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing.")