import os
from dotenv import load_dotenv
load_dotenv()

from dotenv import load_dotenv
import os

# Forcefully load the .env file from current directory
load_dotenv(dotenv_path=".env")

groq_api_key = os.getenv("groq_api_key")
print("groq_api_key")
print("Loaded key:", groq_api_key)  # Should not print None


# Check if the key was loaded
print("API key loaded:", groq_api_key is not None)



from langchain_groq import ChatGroq
model=ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)
print(model)

from langchain_core.messages import HumanMessage , SystemMessage

messages=[
    SystemMessage(content="Translate the following from English to French"),
    HumanMessage(content="hello how are you")
]

model.invoke(messages)