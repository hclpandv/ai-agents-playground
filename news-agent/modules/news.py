import requests
from config import NEWS_API_KEY

def fetch_news(query="AI", from_date=None):
    url = "https://newsapi.org/v2/everything"

    params = {
        "q": query,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY
    }

    if from_date:
        params["from"] = from_date

    response = requests.get(url, params=params)
    data = response.json()

    return data.get("articles", [])


def test_news():
    articles = fetch_news("India AI")

    for i, a in enumerate(articles[:5], 1):
        print(f"\n{i}. {a.get('title')}")
        print(a.get("description"))