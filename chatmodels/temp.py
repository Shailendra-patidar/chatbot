from dotenv import load_dotenv
from huggingface_hub import HfApi
import os

load_dotenv(r"C:\Generative_AI\.env", override=True)

token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

api = HfApi(token=token)

try:
    user = api.whoami()
    print("Authentication successful!")
    print("Username:", user["name"])

except Exception as e:
    print("Authentication failed:", e)