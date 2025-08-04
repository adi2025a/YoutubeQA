from app.utility.extractVidoeId import extract_videoid
from app.utility.transcriptAPI import get_transcript
from app.utility.textSplitter import text_splitter
from app.utility.get_embeddings import get_embeddings
from app.utility.storeInFAISS import store_embeddings, search_faiss_index
import google.generativeai as genail
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
genail.configure(api_key=os.getenv("GEMINI_API_KEY"))


def answer_question(url, question):
    # Step 1: Extract video ID and get transcript
    video_id = extract_videoid(url)
    print("Video ID:", video_id)

    transcript = get_transcript(video_id)
    print("Transcript:", transcript)

    # Step 2: Split transcript into chunks
    chunks = text_splitter(transcript)
    print("Chunks:", len(chunks))

    # Step 3: Get embeddings for each chunk
    chunk_embeddings = get_embeddings(chunks)
    print("Embeddings:", len(chunk_embeddings))

    # Step 4: Store in FAISS
    index = store_embeddings(chunk_embeddings)
    print("FAISS index created.")

    # Step 5: Search for relevant chunks
    results = search_faiss_index(question, index, chunks, get_embeddings, top_k=2)
    print("Top relevant chunks:", results)

    # Step 6: Build prompt and generate answer
    prompt = f"""
    You are an intelligent assistant. Answer the following question based only on the transcript of a YouTube video.
    If the answer is not in the transcript, respond with "I couldn't find that in the video."
    
    Transcript:
    \"\"\"
    {''.join(results)}
    \"\"\"
    
    Question:
    \"\"\"
    {question}
    \"\"\"
    """
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    print(response.text)
    return response.text