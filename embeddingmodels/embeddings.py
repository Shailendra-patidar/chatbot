from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=34,
)

vecor = embeddings.embed_query("What is Data Science?")
print(vecor)


# This will not work because the api credit is over, but the code is correct. You can use your own api key to test it.