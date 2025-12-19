from textwrap import wrap

def chunk_documents(docs, chunk_size=600):
    chunks = []

    for doc in docs:
        if doc["type"] == "text":
            parts = wrap(doc["content"], chunk_size)
            for part in parts:
                chunks.append({
                    "type": "text",
                    "content": part,
                    "page": doc["page"]
                })
        else:
            # tables or others stay as-is
            chunks.append(doc)

    return chunks
