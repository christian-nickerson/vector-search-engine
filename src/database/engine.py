from sqlalchemy import Engine, create_engine


def connect(host: str, port: str, username: str, password: str, database: str) -> Engine:
    """connect to vector database"""
    _url = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
    return create_engine(_url)
