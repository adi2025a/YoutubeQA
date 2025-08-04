import faiss
import numpy as np
from app.utility.ask_question import get_embeddings

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

    question_embedding = get_embeddings([question])
    question_embedding = np.array(question_embedding).astype('float32')
    faiss.normalize_L2(question_embedding)

    # Perform the search
    distances, indices = index.search(question_embedding, top_k)

    print("\nTop matching chunks:")
    for i in range(top_k):
        chunk_index = indices[0][i]
        print(f"\nScore: {distances[0][i]}")
        print(f"Chunk: {chunks[chunk_index]}")
