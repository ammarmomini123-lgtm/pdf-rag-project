from typing import List, Dict, Any
from app.vectorstore.chroma_store import ChromaVectorStore
from app.embeddings.embedding_model import EmbeddingModel

class DocumentRetriever:
    """Retrieves relevant chunks from ChromaDB for a query."""

    def __init__(self, vector_store: ChromaVectorStore, embedding_model: EmbeddingModel):
        self.vector_store = vector_store
        self.embedding_model = embedding_model

    def get_relevant_chunks(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        query_embedding = self.embedding_model.embed_query(query)
        return self.vector_store.search(query_embedding, top_k=top_k)