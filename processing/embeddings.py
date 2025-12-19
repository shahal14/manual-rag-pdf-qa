from sentence_transformers import SentenceTransformer

_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks):
    texts = [c["content"] for c in chunks]
    embeddings = _model.encode(texts, show_progress_bar=False)
    return embeddings
