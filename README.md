# 📘 Free LLM-Based OCR Using OpenRouter (No Cost, Image → Text Extraction)

This project performs **OCR (Optical Character Recognition)** using **free vision-enabled LLMs** available on **OpenRouter**.
No paid API keys, no subscriptions — just fully free OCR using models like:

* **amazon/nova-2-lite-v1:free**
* Any OpenRouter vision-capable free model

This allows you to extract text from images using modern LLMs at **zero cost**.

---

## 🚀 Features

* **100% free OCR using OpenRouter’s free-tier models**
* Works with:

  * 🌐 Image URLs
  * 🖼️ Local images (converted to Base64)
* Model-agnostic (works with any vision LLM on OpenRouter)
* Preserves reading order and all visible text
* Saves extracted text to a `.txt` file
* No OpenAI API key needed — only OpenRouter free API

---

## 🛠 Requirements

* Python 3.7+
* `requests`
* `python-dotenv` (optional, for managing API key)

Install:

```bash
pip install requests python-dotenv
```

Add your OpenRouter API key to a `.env` file:

```
OPENROUTER_API_KEY=your_key_here
```

(You can use the free key available on your OpenRouter dashboard.)

---

## 📘 How It Works

OpenRouter allows sending **image URLs or base64 images** to free LLMs.
This script sends:

* The instruction prompt
* The image as a URL or base64 data URL

And returns **clean text extracted by the model**.

---

## 📂 Functions

### ✔️ `encode_image_to_base64(image_path)`

Loads a local image and converts it to Base64.

### ✔️ `image_to_text_from_url(image_url)`

Downloads the image → sends to LLM → extracts text.

### ✔️ `image_to_text_from_base64(image_base64)`

Sends Base64 directly in a `data:image/jpeg;base64,...` format.

Both functions call a free OpenRouter LLM.

---

## 🧪 Example Usage

### **Extract text from a local image**

```python
image_path = "image.jpg"
image_base64 = encode_image_to_base64(image_path)
text = image_to_text_from_base64(image_base64)
print(text)
```

### **Extract text from an online URL**

```python
image_url = "https://example.com/sample.jpg"
text = image_to_text_from_url(image_url)
print(text)
```

### **Save the OCR output**

```python
with open("extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(text)
```

---

## 🔄 Change the Model Easily

Modify:

```python
"model": "amazon/nova-2-lite-v1:free"
```

To any OpenRouter free vision model (if available):

```python
"model": "qwen2.5-vision:free"
"model": "llama-vision-free"
"model": "openai/gpt-4o-mini:free"
```

No other changes required.

---

## 🧠 Why LLM-Based OCR?

Compared to traditional OCR tools, LLM OCR:

* Reads small & faint text
* Preserves formatting
* Handles mixed fonts
* Works on stylized documents
* Understands layout and context

And with OpenRouter free models — you pay nothing.

---

## 🎯 Use Cases

* OCR for receipts, invoices, IDs
* Text extraction from PDFs (after converting to images)
* Digitizing notes
* Document preprocessing for ML pipelines
* Free OCR for students & hobbyists

---

## 🤝 Contributing

Feel free to submit pull requests for improvements:

* Model selector menu
* Export to JSON/Markdown
* Batch processing
* CLI tool

---

## 📄 License

MIT License.
