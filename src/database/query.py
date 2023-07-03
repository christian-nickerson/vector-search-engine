from enum import StrEnum
from typing import List, Tuple

import numpy as np
from sqlalchemy import Engine, Select, select
from sqlalchemy.orm import Session

from .tables import Products


class Distance(StrEnum):

    """distance metrics"""

    l2: str = "L2 Distance"
    inner_product: str = "Inner Product"
    cosine: str = "Cosine"


def _l2_distance_statement(query_embedding: np.ndarray) -> Select:
    """Create query statement with the L2 distance metric

    :param query_embedding: query embedding to search
    :return: Select query object
    """
    return (
        select(Products, Products.embedding.l2_distance(query_embedding).label("distance"))
        .order_by(Products.embedding.l2_distance(query_embedding))
        .limit(5)
    )


def _inner_product_distance_statement(query_embedding: np.ndarray) -> Select:
    """Create query statement with the inner product distance metric

    :param query_embedding: query embedding to search
    :return: Select query object
    """
    return (
        select(Products, Products.embedding.max_inner_product(query_embedding).label("distance"))
        .order_by(Products.embedding.max_inner_product(query_embedding))
        .limit(5)
    )


def _cosine_distance_statement(query_embedding: np.ndarray) -> Select:
    """Create query statement with the cosine distance metric

    :param query_embedding: query embedding to search
    :return: Select query object
    """
    return (
        select(Products, Products.embedding.cosine_distance(query_embedding).label("distance"))
        .order_by(Products.embedding.cosine_distance(query_embedding))
        .limit(5)
    )


QUERY_STATEMENT = {
    Distance.l2: _l2_distance_statement,
    Distance.inner_product: _inner_product_distance_statement,
    Distance.cosine: _cosine_distance_statement,
}


def similarity_search(
    engine: Engine, query_embedding: np.ndarray, distance_metric: Distance = Distance.l2
) -> List[Tuple[Products, float]]:
    """search database for similar products

    :param engine: SQLAlchemy engine
    :param query_embedding: Query embedding to search database with
    :return: Scalar result from database
    """
    statement = QUERY_STATEMENT[distance_metric](query_embedding)
    with Session(engine) as session:
        return session.execute(statement).all()
