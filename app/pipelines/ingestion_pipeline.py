from app.loaders.pdf_loader import PDFLoader
from app.chunking.chunker import DocumentChunker
from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.chroma_store import ChromaVectorStore
from app.config.settings import settings

class IngestionPipeline:
    """Handles automatic discovery, loading, chunking, embedding, and vector storage."""

    def __init__(self):
        self.loader = PDFLoader()
        self.chunker = DocumentChunker()
        self.embedding_model = EmbeddingModel()
        self.vector_store = ChromaVectorStore()

    def run(self, folder_path: str = settings.RAW_DATA_DIR) -> None:
        print(f"\n--- Scanning Directory for PDFs: '{folder_path}' ---")
        
        # Automatically fetch all documents from the directory
        documents = self.loader.load_directory(folder_path)
        
        if not documents:
            print("--- Ingestion Skipped (No documents to process) ---")
            return

        chunks = self.chunker.split(documents)
        
        texts = [chunk.page_content for chunk in chunks]
        embeddings = self.embedding_model.embed_documents(texts)
        
        self.vector_store.add_documents(chunks, embeddings)
        print("--- Ingestion Pipeline Finished Successfully ---")