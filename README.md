# 🔍 Semantic Similarity API

A FastAPI-based web service that computes semantic similarity between two text inputs using the `all-MiniLM-L6-v2` model from Sentence Transformers.

## 🚀 Features

* **FastAPI**: High-performance API framework.
* **Sentence Transformers**: Uses `all-MiniLM-L6-v2` for embeddings.
* **Cosine Similarity**: Measures sentence closeness.
* **Swagger UI**: Easily test API from browser.

---

## 📁 Project Structure

```
semantic_similarity_api/
├── main.py
├── requirements.txt
└── README.md
```

---

## 🧪 How to Run and Test Using Google Colab

We’ve created a full **Colab Notebook** where you can run and test this API live without installing anything locally.

### ✅ Colab Notebook Link:

👉 [Run Semantic Similarity API in Colab](https://colab.research.google.com/drive/1VnXC-53Mciichjh4-NQNRtoixXjJRmt4?usp=sharing)

### 🧾 What does this notebook do?

It performs these steps:

1. Installs necessary packages like `fastapi`, `uvicorn`, `pyngrok`, `sentence-transformers`, and `torch`.
2. Defines and runs a FastAPI server for semantic similarity.
3. Automatically generates a public **ngrok URL** to access the API from anywhere.
4. Guides you to test the API via a browser or with JSON POST requests.

### 🧪 Expected Output:

Once you run all cells:

* You’ll see output like:

  ```
  🚀 Public URL: https://xxxx-xxx.ngrok-free.app
  ```

* Go to:

  ```
  https://xxxx-xxx.ngrok-free.app/docs
  ```

  You'll find Swagger UI with a `POST /similarity` endpoint.

* Test with:

  ```json
  {
    "text1": "I love programming",
    "text2": "Coding is my passion"
  }
  ```

  Output:

  ```json
  {
    "similarity_score": 0.798
  }
  ```

---

## 🔧 Run Locally (Optional)

### 1. Clone the Repo:

```bash
git clone https://github.com/pushpendra255/semantic_similarity_api.git
cd semantic_similarity_api
```

### 2. Install Dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the App:

```bash
uvicorn main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test.

---

## 📄 License

MIT License. Free to use and modify.

---

For any issues or suggestions, feel free to raise an issue or contact the maintainer.
