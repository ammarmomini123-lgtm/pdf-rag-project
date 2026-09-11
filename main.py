import os
import shutil
from typing import Optional, List, Dict, Any
from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from app.pipelines.ingestion_pipeline import IngestionPipeline
from app.pipelines.rag_pipeline import RAGPipeline
from app.vectorstore.chroma_store import ChromaVectorStore
from app.config.settings import settings

# Initialize FastAPI App
app = FastAPI(
    title="AI-Powered Document RAG Chatbot Dashboard API",
    description="Backend API for document management, vector indexing, and grounded RAG question-answering.",
    version="1.0.0"
)

# Enable CORS for frontend connectivity (Streamlit / React / Vue)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Pipelines
vector_store = ChromaVectorStore()
ingestion_pipeline = IngestionPipeline()
rag_pipeline = RAGPipeline()


# --- Pydantic Data Models ---
class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str
    context: List[Dict[str, Any]]


# --- FastAPI Endpoints ---

@app.get("/api/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "RAG Backend API"}


@app.get("/api/dashboard/stats")
def get_dashboard_stats():
    """Returns real-time dashboard metrics sourced directly from ChromaDB vector store."""
    stats = vector_store.get_stats()
    raw_files = []
    if os.path.exists(settings.RAW_DATA_DIR):
        raw_files = [f for f in os.listdir(settings.RAW_DATA_DIR) if not f.startswith(".")]

    return {
        "total_documents": stats["total_documents"],
        "total_indexed_chunks": stats["total_indexed_chunks"],
        "raw_files_count": len(raw_files),
        "indexed_files": stats["indexed_files"],
        "status": "operational"
    }


@app.get("/api/documents")
def list_documents():
    """Lists all indexed files in the vector database."""
    stats = vector_store.get_stats()
    return {"documents": stats["indexed_files"]}


@app.post("/api/documents/upload")
async def upload_documents(file: UploadFile = File(...)):
    """Uploads a PDF, DOCX, or TXT document, saves it to raw storage, and triggers ingestion."""
    filename = file.filename
    ext = os.path.splitext(filename)[1].lower()
    
    if ext not in [".pdf", ".docx", ".txt", ".md"]:
        raise HTTPException(
            status_code=400, 
            detail=f"Unsupported file format '{ext}'. Upload PDF, DOCX, or TXT."
        )

    os.makedirs(settings.RAW_DATA_DIR, exist_ok=True)
    file_path = os.path.join(settings.RAW_DATA_DIR, filename)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Trigger Ingestion Pipeline for newly uploaded file
        success = ingestion_pipeline.run(file_path)
        if not success:
            raise HTTPException(status_code=500, detail="Failed to extract text or index document.")

        return {
            "message": f"Successfully uploaded and indexed '{filename}'.",
            "file_name": filename,
            "status": "processed"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/api/documents/{file_name}")
def delete_document(file_name: str):
    """Deletes a document from raw storage and removes its vector chunks from ChromaDB."""
    try:
        vector_store.delete_by_file_name(file_name)
        
        file_path = os.path.join(settings.RAW_DATA_DIR, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)

        return {"message": f"Successfully deleted document '{file_name}' from backend and vector store."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    """Executes RAG Pipeline to return grounded answers with document source citations."""
    if not request.question or not request.question.strip():
        raise HTTPException(status_code=400, detail="Question string cannot be empty.")

    result = rag_pipeline.run(request.question)
    return ChatResponse(
        answer=result["answer"],
        context=result.get("context", [])
    )


# --- CLI Execution Mode ---
def run_cli_test():
    """Runs a direct terminal test if main.py is executed as a standalone script."""
    raw_dir = settings.RAW_DATA_DIR
    print("🚀 Initializing Ingestion Pipeline...")
    ingestion_success = ingestion_pipeline.run(raw_dir)

    if not ingestion_success:
        print("⚠️ Ingestion completed with no new documents processed.")

    print("\n🤖 Initializing RAG Pipeline...")
    query = "What is the seller commission fee and escrow deposit policy at AeroEstate Realty?"
    
    print(f"\n❓ Question: {query}")
    result = rag_pipeline.run(query)

    print("\n💡 Answer:")
    print(result["answer"])

    print("\n📚 Retrieved Sources:")
    context_chunks = result.get("context", [])
    
    if not context_chunks:
        print("  (No relevant sources retrieved)")
    else:
        for idx, chunk in enumerate(context_chunks, 1):
            file_name = chunk.get("file_name", "Unknown Source")
            page_num = chunk.get("page", 1)
            score = chunk.get("score", 0.0)
            print(f"[{idx}] Source: 📄 {file_name} — Page {page_num} (Score: {score:.4f})")


if __name__ == "__main__":
    # Runs FastAPI server on localhost:8000
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)