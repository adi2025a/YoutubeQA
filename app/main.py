from fastapi import FastAPI, Query
from pydantic import BaseModel
from app.utility.ask_question import answer_question

app = FastAPI()

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
