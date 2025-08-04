# 🎥 YouTube Video Q&A Chatbot

This project is an intelligent chatbot that answers questions based on the transcript of a YouTube video using Gemini AI. It features a React frontend and a FastAPI backend, with support for transcript processing, embedding storage with FAISS, and efficient caching.

---

## 🚀 Features

- 🔗 Accepts YouTube video links
- 🧠 Answers user questions based on video transcript using Gemini API
- 📄 Automatically extracts and chunks transcripts
- ⚡ Uses FAISS for fast semantic search
- 🧠 Uses Gemini API for answer generation
- 🧠 Caches embeddings to avoid reprocessing
- 💬 Responsive chatbot UI built with Tailwind CSS

---

## 🧩 Tech Stack

### 💻 Frontend
- React
- Vite
- Tailwind CSS

### 🧠 Backend
- FastAPI
- FAISS
- Pydantic
- Google Generative AI (Gemini)
- Custom utility modules

---

## ⚙️ How It Works

1. User submits a YouTube video link and a question.
2. Backend extracts transcript using the YouTube Transcript API.
3. Transcript is split into chunks.
4. Embeddings are generated and stored in FAISS index.
5. Index is cached using video ID to avoid recomputation.
6. Relevant chunks are retrieved from FAISS.
7. Gemini API answers based on retrieved transcript content.
8. Answer is returned and displayed in chat UI.
