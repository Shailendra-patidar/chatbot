
import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Initialize Gemini model through LangChain
llm = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL"),
    api_key=api_key,
    temperature=0.7
)

# Conversation history
messages = [
    SystemMessage(
        content="You are a helpful AI assistant. "
                "Answer questions in simple language."
    )
]

print("LangChain AI Chatbot Started!")
print("Type 'exit' to end the chat.\n")

while True:

    user_input = input("User: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    try:
        # Add user message
        messages.append(
            HumanMessage(content=user_input)
        )

        print("Thinking...")

        # Get response from LLM
        response = llm.invoke(messages)

        # Display response
        print("\nChatbot:", response.content, "\n")

        # Save AI response
        messages.append(
            AIMessage(content=response.content)
        )

    except Exception as e:
        print("Error:", str(e))

        # Remove unanswered user message
        messages.pop()
