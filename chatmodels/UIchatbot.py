
import os
import streamlit as st
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

# Streamlit page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI Chatbot")

# Conversation history
if "messages" not in st.session_state:
    st.session_state.messages = [
       SystemMessage(
    content=(
        "You are a helpful AI assistant. "
        "Answer questions in simple language. "
        "whenever someone asks you to what is your name, or who developed you name as shailendra. "
        "whenever someone asks you to who is the sister of shailendra name as Harshita and Arpita. "
        "whenever someone asks you to who is the brother of shailendra name as Deepak and Shubham. "
        "Whenever someone asks who is shailendra tell them He is a software engineer and He is a founder of a company named as Shailendra Technologies. "
    )
)   
    ]

# Display conversation history
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        role = "user"
    elif isinstance(message, AIMessage):
        role = "assistant"
    else:
        continue

    with st.chat_message(role):
        st.markdown(message.text)

# User input
user_input = st.chat_input("Ask me anything...")

if user_input:

    # Add user message
    st.session_state.messages.append(
        HumanMessage(content=user_input)
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):

                # Get response from LLM
                response = llm.invoke(
                    st.session_state.messages
                )

                # Display response
                st.markdown(response.text)

                # Save AI response
                st.session_state.messages.append(
                    AIMessage(content=response.content)
                )

    except Exception as e:
        st.error(f"Error: {str(e)}")

        # Remove unanswered user message
        st.session_state.messages.pop()
