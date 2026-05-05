# chatbot.py

import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")

if not API_TOKEN or not ACCOUNT_ID:
    raise ValueError("Missing CLOUDFLARE_API_TOKEN or CLOUDFLARE_ACCOUNT_ID in .env file")

URL = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/meta/llama-3-8b-instruct"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

HISTORY_FILE = "chat_history.json"

# Load history
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)
else:
    history = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant with memory."
        }
    ]

def save_history():
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

# ✅ THIS is your main function (used by API)
def get_ai_response(prompt: str) -> str:
    try:
        # Add user message
        history.append({"role": "user", "content": prompt})
        save_history()

        # Trim history to send to AI (System prompt + last 10 messages)
        # This prevents "too many tokens" errors and empty responses
        system_message = [m for m in history if m.get("role") == "system"]
        recent_messages = [m for m in history if m.get("role") != "system"][-10:]
        
        payload = {
            "messages": system_message + recent_messages
        }

        response = requests.post(URL, headers=headers, json=payload)
        response.raise_for_status() # Check for HTTP errors
        data = response.json()

        if not data.get("success") or "result" not in data:
            return f"Error from API: {data.get('errors', 'Unknown error')}"

        reply = data["result"].get("response", "").strip()

        if not reply:
            return "The AI returned an empty response. This might be due to a temporary issue with the model."

        # Add bot reply to persistent history
        history.append({"role": "assistant", "content": reply})
        save_history()

        return reply

    except requests.exceptions.RequestException as e:
        return f"Network Error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"