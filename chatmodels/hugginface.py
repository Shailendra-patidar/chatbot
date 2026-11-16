
import os

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation",
    max_new_tokens=256,
    do_sample=False,
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is cricket give me in bullet points?")

print(response.content)



