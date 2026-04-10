import base64
import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()

url = "https://openrouter.ai/api/v1/chat/completions"
base_model = "nvidia/nemotron-nano-12b-v2-vl:free"
headers = {
    "Authorization": f"Bearer {os.getenv("OPENROUTER_API_KEY")}",
    "Content-Type": "application/json"
}

# from image path to base64 converter
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# ---------------------------------------------------------
# Extract text from image via URL (download → LLM)
# ---------------------------------------------------------
def image_to_text_from_url(image_url):

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Describe this photo in detail. Be accurate and helpful. "
                    		"Don't need to give any explanation, just provide the image description."
                },
                {
                    "type": "image_url",
                    "image_url": {"url": image_url}
                }
            ]
        }
    ]

    payload = {
        "model": base_model,
        "messages": messages
    }

    response = requests.post(url, headers=headers, json=payload)
    print(response.json())

    return response.json().get("choices", [])[0].get("message", {}).get("content", "")



# ---------------------------------------------------------
# Extract text from image using Base64
# ---------------------------------------------------------
def image_to_text_from_base64(image_base64):

    data_url = f"data:image/jpeg;base64,{image_base64}"

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Describe this photo in detail. Be accurate and helpful. "
                    		"Don't need to give any explanation, just provide the image description."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": data_url
                    }
                }
            ]
        }
    ]

    payload = {
        "model": base_model,
        "messages": messages
    }

    response = requests.post(url, headers=headers, json=payload)
    print(response.json())

    return response.json().get("choices", [])[0].get("message", {}).get("content", "")

if __name__ == "__main__":
    image_path = "image.jpg" # Replace with your local image path
    image_base64 = encode_image_to_base64(image_path)
    text_from_image = image_to_text_from_base64(image_base64)
    print("Text from Image Path:\n", text_from_image)
