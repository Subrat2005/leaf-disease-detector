import os
from dotenv import load_dotenv

load_dotenv()
key = os.environ.get("GROQ_API_KEY")

if key:
    print("Key loaded! It starts with:", key[:4])
else:
    print("Key NOT found. Check your .env file.")