from youtube_transcript_api import YouTubeTranscriptApi
from langchain.text_splitter import RecursiveCharacterTextSplitter
from google import genai
import numpy as np
import faiss
import os
from dotenv import load_dotenv
import google.generativeai as genail

# Load API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genail.configure(api_key=api_key)


def input_user_question():
    question = input("Enter question:")
    question_embeddings = get_embeddings([question])
    return [question,question_embeddings]



def get_embeddings(content):
    client = genai.Client()
    result = client.models.embed_content(
            model="gemini-embedding-001",
            contents= content)

    suitable_format_embeddings = []
    for embedding in result.embeddings:
        suitable_format_embeddings.append(embedding.values)
    return suitable_format_embeddings

def text_splitter(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,      # max size of each chunk
        chunk_overlap=50    # how much to overlap between chunks
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_transcirpt(videoid):
    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(videoid)
    return " ".join([t.text for t in fetched_transcript])

def extract_videoid(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    elif "/embed/" in url:
        return url.split("/embed/")[1].split("?")[0]
    else:
        return None

def main():
    youtube_url = input("Enter Youtube URL:")
    videoid = extract_videoid(youtube_url)
    print(f"Video ID: {videoid}")
    fetched_transcript  = get_transcirpt(videoid)
    print(fetched_transcript)
    chunks = text_splitter(fetched_transcript)
    print(len(chunks))
    embeddings = get_embeddings(chunks)
    print(len(embeddings))
    index = store_embeddings(embeddings)
    print(index)
    [question,question_embeddings] = input_user_question()
    search_faiss_index(question,index,chunks,embedding_model,top_k=5)

if __name__ == "__main__":
    main()