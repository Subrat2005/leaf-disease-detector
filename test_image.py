import base64
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq()

# 1. Read the image file and turn it into base64 text
with open("leaf.jpeg", "rb") as f:
    image_bytes = f.read()
base64_image = base64.b64encode(image_bytes).decode("utf-8")

# 2. Send the text question and the image together
response = client.chat.completions.create(
    model="qwen/qwen3.8-27b",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this leaf in two sentences."},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ],
)

print(response.choices[0].message.content)