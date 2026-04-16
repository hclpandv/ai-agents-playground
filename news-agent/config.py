import os
from dotenv import load_dotenv

load_dotenv()

# Google account app cred
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Google ai studio api key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# news.
NEWS_API_KEY = os.getenv("NEWS_API_KEY")