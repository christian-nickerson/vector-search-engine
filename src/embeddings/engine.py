import numpy as np
from sentence_transformers import SentenceTransformer

from config import settings


class EmbeddingEngine:

    """Sentence Embeddings engine for generating embeddings"""

    def __init__(self) -> None:
        self.model = SentenceTransformer(settings.embeddings.model)

    def get_embedding(self, text: str) -> np.ndarray:
        """Create embeddings from text"""
        return self.model.encode(text)
