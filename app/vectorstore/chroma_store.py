import os
import chromadb
from typing import List, Dict, Any
from langchain_core.documents import Document
import numpy as np
from app.config.settings import settings

class ChromaVectorStore:
    """Manages persistent document storage and similarity search using ChromaDB."""

    def __init__(self, collection_name: str = "pdf_rag_collection", persist_dir: str = settings.VECTOR_DB_DIR):
        os.makedirs(persist_dir, exist_ok=True)
        self.client = chromadb.PersistentClient(path=persist_dir)
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def add_documents(self, chunks: List[Document], embeddings: np.ndarray) -> None:
        ids = [f"chunk_{i}" for i in range(len(chunks))]
        texts = [chunk.page_content for chunk in chunks]
        metadatas = [
            {
                "source": chunk.metadata.get("source", "unknown"),
                "page": chunk.metadata.get("page", 0)
            }
            for chunk in chunks
        ]

        self.collection.add(
            ids=ids,
            documents=texts,
            embeddings=embeddings.tolist(),
            metadatas=metadatas
        )
        print(f"✓ Saved {len(chunks)} chunks to ChromaDB.")

    def search(self, query_embedding: np.ndarray, top_k: int = settings.TOP_K) -> List[Dict[str, Any]]:
        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=top_k
        )

        formatted_results = []
        if results and results['documents']:
            docs = results['documents'][0]
            metas = results['metadatas'][0]
            distances = results['distances'][0] if 'distances' in results else [0.0] * len(docs)

            for doc, meta, dist in zip(docs, metas, distances):
                score = 1.0 / (1.0 + float(dist))
                formatted_results.append({
                    "content": doc,
                    "source": meta.get("source", "unknown"),
                    "page": meta.get("page", 0),
                    "score": score
                })

        return formatted_results