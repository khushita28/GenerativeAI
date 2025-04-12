import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}",
    "Accept": "application/json"
}

def summarize_with_hf_api(code: str) -> str:
    payload = {
        "inputs": code,
        "parameters": {
            "max_length": 128,
            "min_length": 20,
            "do_sample": False
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        result = response.json()
        if isinstance(result, list):
            if "summary_text" in result[0]:
                return result[0]["summary_text"]
            elif "generated_text" in result[0]:
                return result[0]["generated_text"]
        elif "error" in result:
            return f"❌ API Error: {result['error']}"
        else:
            return f"⚠️ Unexpected response: {result}"
    except Exception:
        return f"❌ API Error: {response.text}"
