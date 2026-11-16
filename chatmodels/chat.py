
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    "google_genai:gemini-3.8-flash"
)

response = model.invoke("What is cricket give me in bullet points?")

print(response.content)
