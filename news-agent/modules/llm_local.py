import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma4:e4b" 

def test_ollama():
    print("Testing local Ollama model...\n")

    print(
        summarize(
            "India launches new AI policy. Stock markets rise. ISRO announces mission."
        )
    )

def summarize(text: str):
    prompt = f"""
You are a news assistant.

Summarize the following news into:
- 5 bullet points
- simple English
- highlight important events

NEWS:
{text}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()
    data = response.json()

    return data["response"]

