from sqlalchemy import select
from sqlalchemy.orm import Session

from config import settings
from data import NikeDataset
from database.engine import connect
from database.ingress import import_product
from database.tables import Products, create_tables
from embeddings.engine import EmbeddingEngine

index = 1

SEARCH_TEXT = "a soccer jacket"

if __name__ == "__main__":
    import numpy as np

    nd = NikeDataset()
    embed = EmbeddingEngine()

    conn = connect(
        host=settings.db.host,
        port=settings.db.port,
        username=settings.db.username,
        password=settings.db.password,
        database=settings.db.database,
    )
    # create_tables(conn)
    # import_product(nd, conn)

    query_embedding = embed.get_embedding(SEARCH_TEXT)
    session = Session(bind=conn)
    results = session.scalars(select(Products).order_by(Products.embedding.l2_distance(query_embedding)).limit(5))
    for item in results.all():
        print(f"TITLE: {item.name}")
        print(f"SUBTITLE: {item.sub_title}")
        print(f"DESCRIPTION: {item.description}")
        print("--------------------------------")
