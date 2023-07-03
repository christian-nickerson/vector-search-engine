from config import settings
from data import NikeDataset
from database.engine import connect
from database.ingress import import_product
from database.tables import create_tables

if __name__ == "__main__":
    nd = NikeDataset()
    # print(nd.df.dtypes)
    conn = connect(
        host=settings.db.host,
        port=settings.db.port,
        username=settings.db.username,
        password=settings.db.password,
        database=settings.db.database,
    )
    create_tables(conn)
    import_product(nd, conn)
