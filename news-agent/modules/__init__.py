import os

USE_LOCAL = os.getenv("USE_LOCAL_LLM", "false").lower() == "true"

if USE_LOCAL:
    from .llm_local import summarize
    print("Using LOCAL LLM (Ollama)")
else:
    from .llm import summarize
    print("Using GEMINI LLM")