from typing import List, Dict, Any
from app.vectorstore.chroma_store import ChromaVectorStore
from app.embeddings.embedding_model import EmbeddingModel
from app.retriever.retriever import DocumentRetriever
from app.config.settings import settings

class RetrievalPipeline:
    """Retrieves context chunks for a given query."""

    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.vector_store = ChromaVectorStore()
        self.retriever = DocumentRetriever(self.vector_store, self.embedding_model)

    def run(self, query: str, top_k: int = settings.TOP_K) -> List[Dict[str, Any]]:
        return self.retriever.get_relevant_chunks(query, top_k=top_k)