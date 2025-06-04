# 🧠 Semantic Similarity API (Lite Version) – Google Colab Deployment

This project provides an API to compute **semantic similarity** between two pieces of text using **FastAPI**, `sentence-transformers`, and **ngrok**, deployed directly from **Google Colab**.

---

## 🚀 Features
- Text similarity scoring API using cosine similarity
- Hosted via FastAPI inside Colab
- Public link via Ngrok tunnel
- Minimal dependency and RAM usage
- Auto API documentation at `/docs`

---

## 📂 Project Structure
```
semantic_similarity_api/
├── main.py                # FastAPI app with endpoint
├── requirements.txt       # Dependencies
├── colab_ngrok_run.py     # Script to run API via Colab + ngrok
├── README.md              # This file
```

---

## ▶️ How to Deploy via Google Colab

### 🔗 1. Open Colab Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pushpendra255/semantic_similarity_api/blob/main/colab_ngrok_run.ipynb)

OR manually run the commands below in a new Colab notebook:

```python
# 1. Clone the GitHub repo
!git clone https://github.com/pushpendra255/semantic_similarity_api.git
%cd semantic_similarity_api

# 2. Install required packages
!pip install -r requirements.txt
!pip install fastapi nest_asyncio pyngrok uvicorn

# 3. Start the FastAPI app using ngrok
import nest_asyncio
from pyngrok import ngrok
import uvicorn

nest_asyncio.apply()
public_url = ngrok.connect(8000)
print("🚀 Public URL:", public_url)

!uvicorn main:app --host 0.0.0.0 --port=8000
```

---

## 📮 API Endpoint

### `POST /similarity`

#### 🔹 Request JSON
```json
{
  "text1": "Data science is an amazing field.",
  "text2": "Machine learning is a part of data science."
}
```

#### 🔹 Response
```json
{
  "similarity score": 0.725
}
```

### ✅ Live Swagger UI

Once deployed in Colab, open:

```
https://<your-ngrok-id>.ngrok-free.app/docs
```

There, you can test your API using Swagger UI without any code!

---

## 📌 Notes

- Ngrok sessions are temporary – they expire after a few hours.
- For permanent deployment, consider Render, HuggingFace, or Deta Space.

---

## 👨‍💻 Author
Built by [Pushpendra Bhadauriya](https://github.com/pushpendra255)  
🧪 For educational and demo purposes