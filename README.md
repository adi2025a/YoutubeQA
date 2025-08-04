# 🎥 YouTube Video Q&A Bot (Gemini + FAISS)

This project allows you to ask questions based on the content of any YouTube video. It transcribes the video, splits the transcript into chunks, embeds those using Google's Gemini embeddings, stores them in a FAISS vector index, and uses Gemini Pro to generate a context-aware answer.

---

## 🚀 Features

- ✅ Extracts transcript from YouTube videos  
- ✅ Splits long text into meaningful chunks  
- ✅ Embeds content using Gemini's embedding model  
- ✅ Stores and searches embeddings using FAISS  
- ✅ Answers user questions using Gemini Pro  
- ✅ Fast and scalable

---

## 🧠 Tech Stack

- **Python 3**
- **FAISS** - Facebook AI Similarity Search
- **Google Generative AI SDK (`google-generativeai`)**
- **YouTube Transcript API**
- **dotenv** for environment management
