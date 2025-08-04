import faiss
import numpy as np
from app.utility.get_embeddings import get_embeddings

def store_embeddings(embeddings):
    # Convert embeddings to numpy array if not already
    embeddings_array = np.array(embeddings).astype('float32')

    # Get the dimension of embeddings from the actual data
    embedding_dim = embeddings_array.shape[1]

    # Normalize the embeddings (L2 normalization)
    faiss.normalize_L2(embeddings_array)

    # Create a FAISS index for L2 (Euclidean) distance
    index = faiss.IndexFlatL2(embedding_dim)

    # Add the embeddings to the index
    index.add(embeddings_array)

    return index

def search_faiss_index(question, index, chunks, embedding_model, top_k=5):
    # Step 1: Get embedding of the user question using the passed embedding model
    question_embedding = embedding_model([question])  # Make sure it returns a list of vectors
    query_vector = np.array(question_embedding).astype('float32')

    # Step 2: Normalize query vector (if your FAISS index is L2-normalized)
    faiss.normalize_L2(query_vector)

    # Step 3: Search FAISS index
    distances, indices = index.search(query_vector, top_k)

    # Step 4: Retrieve top matching text chunks
    results = []
    for idx in indices[0]:
        results.append(chunks[idx])

    return results

