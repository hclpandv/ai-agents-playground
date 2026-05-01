from modules.email_sender import send_email
from modules.llm import summarize, test_gemini
from modules.llm_local import query_local_llm
from modules.news import test_news, fetch_news


#--------Run-----------
if __name__ == "__main__":
    print("Performing some tests")
    #send_email("Hello from AI agent test")
    #test_gemini()
    test_news()
    