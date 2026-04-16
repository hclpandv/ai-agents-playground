from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def test_gemini():
    print("Testing Gemini 2.5 Flash...\n")

    print(
        summarize(
            "India launches new AI policy. Stock markets rise. ISRO announces mission."
        )
    )

def summarize(text: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
You are a news assistant.

Summarize the following news into:
- 5 bullet points
- simple English
- highlight important events

NEWS:
{text}
"""
    )
    return response.text


