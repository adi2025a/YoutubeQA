from fastapi import FastAPI
from pydantic import BaseModel
from app.utility.answer_question import answer_question
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Use specific origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QARequest(BaseModel):
    youtube_url: str
    question: str

@app.post("/ask")
def ask_question(data: QARequest):
    try:
        answer = answer_question(data.youtube_url, data.question)
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}
