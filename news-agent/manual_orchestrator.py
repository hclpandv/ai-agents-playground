from modules.news import fetch_news
from modules.llm import summarize
from modules.email_sender import send_email

"""
This is a manual orchestrator, not a true agentic AI system.

It mimics an agent by following a fixed pipeline:
fetch → filter → summarize → email

But it is hardcoded, linear, no state tracking, no branching logic engine

`agent.py` implements the same logic using an agent framework (LangGraph),
with explicit state, nodes, and flexible execution flow.
"""

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
# Entry point
# -----------------------------
if __name__ == "__main__":
    run_agent()
    