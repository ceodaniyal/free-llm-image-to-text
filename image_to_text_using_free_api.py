import base64
import requests
import os
import requests
import json
import base64
from dotenv import load_dotenv
load_dotenv()


url = "https://openrouter.ai/api/v1/chat/completions"
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
                    "text": "Extract all text from this image thoroughly. "
                            "Do NOT miss any words, headings, lists, faint text, "
                            "or text near edges. Maintain the original reading order."
                            "Don't need to give any explanation, just provide the extracted text."
                },
                {
                    "type": "image_url",
                    "image_url": {"url": image_url}
                }
            ]
        }
    ]

    payload = {
        "model": "amazon/nova-2-lite-v1:free",
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
                    "text": "Extract all text from this image thoroughly. "
                            "Do NOT miss any words, headings, lists, faint text, "
                            "or text near edges. Maintain the original reading order."
                            "Don't need to give any explanation, just provide the extracted text."
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
        "model": "amazon/nova-2-lite-v1:free",
        "messages": messages
    }

    response = requests.post(url, headers=headers, json=payload)
    print(response.json())

    return response.json().get("choices", [])[0].get("message", {}).get("content", "")



if __name__ == "__main__":
    
    # ---- Example 1: From Image URL ----
    # image_url = "https://media.gettyimages.com/id/1813512682/vector/certificate-diploma-template.jpg?s=612x612&w=gi&k=20&c=sqk_pABwv9CYB4UwaAu3fQdRoILYurBzGok05Fj1JRk=" # Replace with your image URL
    # text_from_image = image_to_text_from_url(image_url)
    # print("Text from Image URL:\n", text_from_image)

    # ---- Example 2: From Image Path ----
    image_path = "image.jpg" # Replace with your local image path
    image_base64 = encode_image_to_base64(image_path)
    text_from_image = image_to_text_from_base64(image_base64)
    print("Text from Image Path:\n", text_from_image)

    # Save the extracted text to a file
    output_file_path = "extracted_text.txt"
    with open("extracted_text.txt", "w", encoding="utf-8") as output_file:
        output_file.write(text_from_image)
    print(f"Extracted text saved to {output_file_path}")