from app.utility.extractVidoeId import extract_videoid
from app.utility.transcriptAPI import get_transcript
from app.utility.textSplitter import text_splitter
from app.utility.get_embeddings import get_embeddings
from app.utility.storeInFAISS import store_embeddings, search_faiss_index
import google.generativeai as genai

def answer_question(url,question):
    client = genai.Client()
    videoId = extract_videoid(url)
    print(videoId)
    transcript = get_transcript(videoId)
    print(transcript)
    chunks = text_splitter(transcript)
    print(len(chunks))
    chunk_embeddings = get_embeddings(chunks)
    index = store_embeddings(chunk_embeddings)
    results = search_faiss_index(question, index, chunks, top_k=5)

    response = client.models.generate_content(
        model="gemini-pro",
        prompt = f"""
                You are an intelligent assistant. Answer the following question based only on the transcript of a YouTube video.
                If the answer is not in the transcript, respond with "I couldn't find that in the video."
                
                Transcript:
                \"\"\"
                {results}
                \"\"\"
                
                Question:
                \"\"\"
                {question}
                \"\"\"
                """,
        max_output_tokens=1024,
        temperature=0.5,
    )

    return response.text