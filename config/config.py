import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="config/.env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("🛑 OPENAI_API_KEY not found!")