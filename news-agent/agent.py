from typing import TypedDict
from langgraph.graph import StateGraph, END

from modules.news import fetch_news
from modules.email_sender import send_email
from modules import summarize


# -----------------------------
# Define State
# -----------------------------
class AgentState(TypedDict):
    articles: list
    summary: str


# -----------------------------
# Nodes
# -----------------------------
def fetch_node(state):
    print("\n📰 [FETCH] Starting news fetch...")
    articles = fetch_news("India OR AI OR technology")
    return {"articles": articles}


def summarize_node(state):
    print("\n🧠 [SUMMARIZE] Preparing summary...")
    articles = state["articles"]

    combined_text = "\n\n".join(
        f"{a.get('title')}\n{a.get('description')}"
        for a in articles[:5]
    )

    summary = summarize(combined_text)
    return {"summary": summary}


def email_node(state):
    print("\n📧 [EMAIL] Sending email...")
    send_email(state["summary"])
    return {}


# -----------------------------
# Build Graph
# -----------------------------
builder = StateGraph(AgentState)

builder.add_node("fetch", fetch_node)
builder.add_node("summarize", summarize_node)
builder.add_node("email", email_node)

builder.set_entry_point("fetch")

builder.add_edge("fetch", "summarize")
builder.add_edge("summarize", "email")
builder.add_edge("email", END)

graph = builder.compile()


# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    print("🚀 Running LangGraph Agent...\n")
    graph.invoke({})