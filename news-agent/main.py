from modules.news import fetch_news
from modules.llm import summarize
from modules.email_sender import send_email


def is_important(article):
    text = (article.get("title") or "") + " " + (article.get("description") or "")

    keywords = ["AI", "India", "security", "economy", "policy", "ISRO"]

    return any(k.lower() in text.lower() for k in keywords)


def build_digest():
    print("📰 Fetching news...")

    articles = fetch_news("India OR AI OR technology")

    important = [a for a in articles if is_important(a)]

    if not important:
        return "No important news today."

    print(f"🔍 Found {len(important)} relevant articles")

    combined_text = "\n\n".join(
        f"{a.get('title')}\n{a.get('description')}"
        for a in important[:5]
    )

    print("🤖 Sending to LLM for summarization...")

    summary = summarize(combined_text)

    return summary


def run_agent():
    print("\n🚀 Starting AI News Agent...\n")

    result = build_digest()

    print("\n===== FINAL SUMMARY =====\n")
    print(result)

    print("\n📧 Sending email...")
    send_email(result)

    print("✅ Done!")


# -----------------------------
# 4. Entry point
# -----------------------------
if __name__ == "__main__":
    run_agent()
    