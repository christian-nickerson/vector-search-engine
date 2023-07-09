from enum import StrEnum
from typing import List

import numpy as np
import strawberry
from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from src.config import settings

from .engine import connect
from .models import Products


@strawberry.enum
class Distance(StrEnum):

    """distance metrics"""

    l2: str = "L2 Distance"
    inner_product: str = "Inner Product"
    cosine: str = "Cosine"


class SimilaritySearch:

    """Similarity search engine"""

    def __init__(self) -> None:
        self._register_statements()
        self.engine = connect(
            host=settings.db.host,
            port=settings.db.port,
            username=settings.db.username,
            password=settings.db.password,
            database=settings.db.database,
        )

    @staticmethod
    def _l2_distance_statement(query_embedding: np.ndarray) -> Select:
        """Create query statement with the L2 distance metric

        :param query_embedding: query embedding to search
        :return: Select query object
        """
        return select(Products).order_by(Products.embedding.l2_distance(query_embedding)).limit(5)

    @staticmethod
    def _inner_product_distance_statement(query_embedding: np.ndarray) -> Select:
        """Create query statement with the inner product distance metric

        :param query_embedding: query embedding to search
        :return: Select query object
        """
        return select(Products).order_by(Products.embedding.max_inner_product(query_embedding)).limit(5)

    @staticmethod
    def _cosine_distance_statement(query_embedding: np.ndarray) -> Select:
        """Create query statement with the cosine distance metric

        :param query_embedding: query embedding to search
        :return: Select query object
        """
        return select(Products).order_by(Products.embedding.cosine_distance(query_embedding)).limit(5)

    def _register_statements(self) -> None:
        """register different distance search statements"""
        self.query_statements = {
            Distance.l2: self._l2_distance_statement,
            Distance.inner_product: self._inner_product_distance_statement,
            Distance.cosine: self._cosine_distance_statement,
        }

    def query(self, query_embedding: np.ndarray, distance_metric: Distance) -> List[Products]:
        """search database for similar products

        :param query_embedding: Query embedding to search database with
        :return: Scalar result from database
        """
        statement = self.query_statements[distance_metric](query_embedding)
        with Session(self.engine) as session:
            results = session.execute(statement).all()
            return [row[0] for row in results]
