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

---

## 📁 Directory Structure

project-root/
│
├── app/
│ ├── main.py # Entry point (optional)
│ └── utility/
│ ├── extractVidoeId.py # Extracts video ID from URL
│ ├── transcriptAPI.py # Fetches video transcript
│ ├── textSplitter.py # Splits transcript into chunks
│ ├── get_embeddings.py # Embeds content using Gemini
│ └── storeInFAISS.py # Stores/searches with FAISS
│
├── .env # Contains your Gemini API Key
├── requirements.txt # Python dependencies
└── README.md

yaml
Copy code

---

## ⚙️ Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/youtube-qna-gemini.git
cd youtube-qna-gemini
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:

Create a .env file in the root directory:

ini
Copy code
GEMINI_API_KEY=your_api_key_here
Run the application:

If you are running a script directly:

bash
Copy code
python app/main.py
If you are using FastAPI (optional):

bash
Copy code
uvicorn app.main:app --reload
🧪 Example Usage
python
Copy code
from app.answer import answer_question

url = "https://www.youtube.com/watch?v=your_video_id"
question = "What is the main topic of the video?"

answer = answer_question(url, question)
print("Answer:", answer)
📌 Notes
Gemini embedding model: models/embedding-001

Gemini text model: gemini-pro (ensure it's supported by the API version)

FAISS index is built in-memory

📜 License
MIT License

🙏 Acknowledgements
Google Generative AI

FAISS

YouTube Transcript API

vbnet
Copy code

Let me know if you want to include `FastAPI` routes, a frontend, Docker setup, or deployment instructions too.
