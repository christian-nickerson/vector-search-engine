from typing import List

from src.database.models import Products
from src.database.query import Distance, SimilaritySearch
from src.embeddings.engine import EmbeddingEngine


class CreateQueries:

    """GrapQL query resolvers"""

    def __init__(self) -> None:
        self.similairty = SimilaritySearch()
        self.embedding_engine = EmbeddingEngine()

    def search(self, text: str, distance_metric: Distance = Distance.l2) -> List[Products]:
        """Search for similar products given a query string, e.g. 'lightweight soccer jackets'

        :param text: Query search text
        :param distance_metric: distance metric to use, defaults to Distance.l2
        :return: List of similar products
        """
        embedding = self.embedding_engine.embed(text)
        return self.similairty.query(embedding, distance_metric)
