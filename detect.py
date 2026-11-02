import base64
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq()

PROMPT = """You are a plant disease expert. Look at this image.

If it is NOT a plant leaf, reply with this JSON:
{"valid_leaf": false, "reason": "short explanation"}

If it IS a plant leaf, reply with this JSON:
{
  "valid_leaf": true,
  "disease_detected": true or false,
  "disease_name": "name, or null if healthy",
  "severity": "none, mild, moderate or severe",
  "symptoms": ["list of what you see"],
  "treatment": ["list of recommended actions"]
}

Reply with JSON only, no other text."""


def analyze_leaf(image_bytes, mime_type="image/jpeg"):
    """Send image bytes to the model and return the result as a dictionary."""
    base64_image = base64.b64encode(image_bytes).decode("utf-8")

    response = client.chat.completions.create(
        model="qwen/qwen3.8-27b",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": PROMPT},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:{mime_type};base64,{base64_image}"},
                    },
                ],
            }
        ],
        response_format={"type": "json_object"},
    )

    raw_text = response.choices[0].message.content

    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        return {"valid_leaf": False, "reason": "Model returned an unreadable reply"}

    

if __name__ == "__main__":
    for image in ["leaf.jpeg", "fruit.jpg", "green_leaf.jpg"]:
        print("=== Testing", image, "===")
        with open(image, "rb") as f:
              result = analyze_leaf(f.read())

        if not result.get("valid_leaf"):
            print("Not a valid leaf image:", result.get("reason"))
        elif result.get("disease_detected"):
            print("Disease:", result.get("disease_name"))
            print("Severity:", result.get("severity"))
        else:
            print("The leaf looks healthy.")
        print()