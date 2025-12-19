import numpy as np
from sentence_transformers import SentenceTransformer

_model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve(query, index, chunks, top_k=5):
    """
    Retrieve top-k most relevant chunks for a query.
    """
    query_embedding = _model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    return [chunks[i] for i in indices[0]]
