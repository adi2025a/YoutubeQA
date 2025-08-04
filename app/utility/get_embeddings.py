import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def get_embeddings(content):
    try:
        response = genai.embed_content(
            model="models/embedding-001",
            content=content,
            task_type="retrieval_document"
        )
        return response['embedding']  # This is a 768-dim float vector
    except Exception as e:
        print("Error while embedding content:", e)
        return None
