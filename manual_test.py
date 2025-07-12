from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="./.env")

print("Key:", os.getenv("GROQ_API_KEY"))
