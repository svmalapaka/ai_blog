import openai
import os
from dotenv import load_dotenv

# 🔄 Load environment variables from .env file
load_dotenv(dotenv_path="config/.env")  # Adjust path as needed

def validate_openai_key():
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.Model.list()
        return "✅ OpenAI key valid" if response and response.data else "❌ No models returned"
    except Exception as e:
        return f"❌ OpenAI key check failed: {str(e)}"