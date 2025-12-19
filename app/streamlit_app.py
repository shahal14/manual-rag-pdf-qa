import streamlit as st

st.set_page_config(page_title="Multi-Modal RAG", layout="centered")

st.title("📄 Multi-Modal Document QA (Manual RAG)")

st.write("Upload a PDF and ask questions grounded in the document.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file is None:
    st.info("Please upload a PDF to continue.")
    st.stop()

st.success("PDF uploaded successfully!")

# Save uploaded file
with open("temp.pdf", "wb") as f:
    f.write(uploaded_file.read())

st.write("🔍 Running document ingestion...")

try:
    from ingestion.run_ingestion import ingest
    docs = ingest("temp.pdf")

    st.write(f"✅ Extracted {len(docs)} document elements")

    # Show preview
    if docs:
        st.write("📄 Preview of first extracted item:")
        st.json(docs[0])
    else:
        st.warning("⚠️ No content extracted from document")

except Exception as e:
    st.error(f"❌ Ingestion failed: {e}")
    st.stop()

st.write("✂️ Chunking document content...")

from processing.chunking import chunk_documents
chunks = chunk_documents(docs)

st.success(f"Created {len(chunks)} chunks")

st.write("🧩 Sample chunk:")
st.json(chunks[0])

st.write("🧠 Generating embeddings...")

from processing.embeddings import embed_chunks
embeddings = embed_chunks(chunks)

st.success(f"Generated {len(embeddings)} embeddings")

st.write("📦 Building FAISS vector index...")

from retrieval.vector_store import build_faiss_index
index = build_faiss_index(embeddings)

st.success("Vector index is ready!")

st.divider()
st.subheader("💬 Ask a question")

query = st.text_input("Enter your question", key="user_query")

if query:
    st.write("🔎 Retrieving relevant context...")

    from retrieval.retriever import retrieve
    results = retrieve(query, index, chunks)

    from qa.qa_chain import generate_answer
    answer = generate_answer(query, results)

    st.subheader("📌 Answer")
    st.write(answer)

# import streamlit as st
# from ingestion.run_ingestion import ingest
# from processing.chunking import chunk_documents
# from processing.embeddings import embed_chunks
# from retrieval.vector_store import build_faiss_index
# from retrieval.retriever import retrieve
# from qa.qa_chain import generate_answer
# from qa.llm_qa_chain import generate_llm_answer

# st.title("📄 LLaMA-3 Powered Manual RAG")

# uploaded = st.file_uploader("Upload PDF", type=["pdf"])

# if uploaded:
#     with open("temp.pdf", "wb") as f:
#         f.write(uploaded.read())

#     docs = ingest("temp.pdf")
#     chunks = chunk_documents(docs)
#     embeddings = embed_chunks(chunks)
#     index = build_faiss_index(embeddings)

#     mode = st.radio(
#         "Answer Mode",
#         ["Manual (Extractive)", "LLM (LLaMA-3)"]
#     )

#     query = st.text_input("Ask a question", key="query")

#     if query:
#         results = retrieve(query, index, chunks)

#         if mode == "Manual (Extractive)":
#             answer = generate_answer(query, results)
#         else:
#             answer = generate_llm_answer(query, results)

#         st.subheader("📌 Answer")
#         st.write(answer)
