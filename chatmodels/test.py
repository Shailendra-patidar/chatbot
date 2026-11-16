import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL"),
    google_api_key=os.getenv("GEMINI_API_KEY"),
    timeout=30,
    max_retries=1
)

print("Sending request to Gemini...")

try:
    response = llm.invoke("Explain Python in two sentences.")

    print("Response received!")
    print(response.text)

except Exception as e:
    print("API FAILED:")
    print(repr(e))