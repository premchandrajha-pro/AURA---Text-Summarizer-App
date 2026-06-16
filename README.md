# 🧠 AI Text Summarizer

A modern AI-powered text summarization web application built using **FastAPI**, **Transformers**, and **PyTorch**. This project uses a fine-tuned **T5 model** to generate concise and meaningful summaries from long conversations or text passages.

Whether you're dealing with lengthy discussions, meeting notes, customer support chats, or articles, this application helps extract the key information in seconds.

---

## ✨ Features

✅ AI-powered text summarization using a fine-tuned T5 model

✅ Fast and lightweight FastAPI backend

✅ Beautiful and responsive user interface

✅ Real-time summary generation

✅ Clean and intuitive user experience

✅ REST API support for integration with other applications

---

## 🖼️ Project Preview

The application provides a clean interface where users can:

1. Paste a long conversation or text
2. Click the **Summarize** button
3. Receive an AI-generated summary instantly

---

## 🛠️ Tech Stack

### Backend

* ⚡ FastAPI
* 🤗 Hugging Face Transformers
* 🔥 PyTorch
* 🐍 Python

### Frontend

* HTML
* CSS
* JavaScript

### AI Model

* Fine-tuned T5 Transformer Model

---

## 📂 Project Structure

```text
text-summarizer/
│
├── app.py
├── index.html
├── requirements.txt
├── README.md
├── saved_summery_model/
│
└── .gitignore
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/text-summarizer.git
cd text-summarizer
```

---

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```bash
python -m uvicorn app:app --reload
```

Once the server starts successfully, open:

```text
http://127.0.0.1:8000
```

in your browser.

---

## 📡 API Endpoint

### Generate Summary

**POST** `/summarize/`

Request Body:

```json
{
    "Dialogue": "Your conversation or text here..."
}
```

Response:

```json
{
    "summary": "Generated summary text..."
}
```

---

## 🎯 Example

### Input

```text
John and Sarah discussed the upcoming project deadline.
John will handle the frontend implementation while Sarah
will work on the backend APIs. They agreed to finish
their tasks before Friday.
```

### Output

```text
John and Sarah planned their project work, assigning
frontend development to John and backend development
to Sarah, with a deadline set for Friday.
```

---

## 📚 What I Learned

This project helped me gain hands-on experience with:

* Building APIs using FastAPI
* Deploying Transformer models
* Working with Hugging Face libraries
* Frontend and backend integration
* Handling model inference in production-like environments
* Debugging real-world Python and FastAPI issues

---

## 🔮 Future Improvements

* Multiple summary length options
* File upload support (PDF, TXT, DOCX)
* Dark/Light mode toggle
* User authentication
* Deployment on Render or Railway
* Docker support
* Summarization history

---

## 🤝 Contributing

Contributions, suggestions, and feedback are always welcome.

Feel free to fork the repository and submit a pull request.

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐ on GitHub.

It motivates me to continue building and sharing more AI projects.

---

## 👨‍💻 Author

Developed with ❤️ using FastAPI, PyTorch, and Transformers.

**Happy Coding! 🚀**
