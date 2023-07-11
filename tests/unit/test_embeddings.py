import numpy as np

from embeddings.engine import EmbeddingEngine


def test_embedding() -> None:
    """test embeddings return as expected"""
    engine = EmbeddingEngine()
    embedding = engine.embed("a soccer jacket")
    assert len(embedding) == 384
    assert isinstance(embedding, np.ndarray)
