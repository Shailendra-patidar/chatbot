
from langchain.chat_models import init_chat_model

# Initialize local Ollama model
model = init_chat_model(
    "ollama:llama3.2"
)

# Send prompt
response = model.invoke(
    "What is cricket? Explain in bullet points."
)

# Print response
print(response.content)
