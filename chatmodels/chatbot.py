from langchain.messages import SystemMessage, AIMessage,HumanMessage
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
    ),
)
messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
]

chat_model = ChatHuggingFace(llm=llm)

while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    messages.append(HumanMessage(content=user_input))
    result = chat_model.invoke(messages)
    messages.append(AIMessage(content=result.content))  
    print("Bot:", result.content)