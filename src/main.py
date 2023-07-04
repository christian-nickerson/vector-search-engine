from config import settings
from data import NikeDataset
from database.engine import connect
from database.ingress import import_product
from database.query import Distance, similarity_search
from database.tables import Products, create_tables
from embeddings.engine import EmbeddingEngine

index = 1

SEARCH_TEXT = "a soccer jacket"

if __name__ == "__main__":
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
    results = similarity_search(conn, query_embedding)

    for item, distance in results:
        print(f"TITLE: {item.name}")
        print(f"SUBTITLE: {item.sub_title}")
        print(f"DESCRIPTION: {item.description}")
        print(f"DISTANCE: {distance}")
        print("--------------------------------")
