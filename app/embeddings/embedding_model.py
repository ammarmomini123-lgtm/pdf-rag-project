from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer
from app.config.settings import settings

class EmbeddingModel:
    """Handles vector embedding generation using SentenceTransformers."""

    def __init__(self, model_name: str = settings.EMBEDDING_MODEL_NAME):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts: List[str]) -> np.ndarray:
        return self.model.encode(texts, show_progress_bar=True)

    def embed_query(self, text: str) -> np.ndarray:
        return self.model.encode([text])[0]