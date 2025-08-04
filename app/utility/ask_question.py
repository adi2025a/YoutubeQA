from google import genai
import google.generativeai as genail
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genail.configure(api_key=api_key)

def get_embeddings(content):
    client = genai.Client()

    result = client.models.embed_content(
            model="gemini-embedding-001",
            contents= [
                content
            ])

    for embedding in result.embeddings:
        print(embedding)


def answer_question(question):
    client = genai.Client(api_key)

    response = client.models.generate_content(
        model="gemini-pro",
        prompt=question,
        max_output_tokens=1024,
        temperature=0.5,
    )

    return response.text