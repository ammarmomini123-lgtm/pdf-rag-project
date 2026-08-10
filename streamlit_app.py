import os
import streamlit as st
from app.pipelines.ingestion_pipeline import IngestionPipeline
from app.pipelines.rag_pipeline import RAGPipeline
from app.config.settings import settings

# Page Configuration
st.set_page_config(
    page_title="PDF RAG Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 PDF Document Q&A Assistant")

# Sidebar - Document Ingestion
with st.sidebar:
    st.header("1. Document Management")
    uploaded_files = st.file_uploader("Upload PDF Documents", type=["pdf"], accept_multiple_files=True)
    
    if st.button("Process & Ingest Documents"):
        if uploaded_files:
            os.makedirs(settings.RAW_DATA_DIR, exist_ok=True)
            for uploaded_file in uploaded_files:
                save_path = os.path.join(settings.RAW_DATA_DIR, uploaded_file.name)
                with open(save_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
            
            with st.spinner("Ingesting documents and updating vector database..."):
                ingestion = IngestionPipeline()
                ingestion.run(settings.RAW_DATA_DIR)
            st.success("✓ Documents ingested successfully!")
        else:
            st.warning("Please upload at least one PDF file first.")

# Main Interface - Querying
st.header("2. Ask Questions")
query = st.text_input("Enter your question based on the uploaded documents:")

if st.button("Submit Question") and query:
    with st.spinner("Searching document context and generating answer..."):
        rag = RAGPipeline()
        result = rag.run(query)

    st.subheader("💡 Answer")
    st.write(result["answer"])

    if result["context"]:
        with st.expander("📚 View Retrieved Sources"):
            for idx, chunk in enumerate(result["context"], 1):
                st.markdown(f"**Source {idx}:** `{chunk['source']}` (Page {chunk['page'] + 1}) | *Score: {chunk['score']:.4f}*")
                st.write(chunk["content"])
                st.divider()