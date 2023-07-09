from sqlalchemy.orm import Session

from src.config import settings
from src.database.engine import connect
from src.database.models import Products


class ImportClient:

    """Client for importing data to vector db"""

    def __init__(self) -> None:
        self.engine = connect(
            host=settings.db.host,
            port=settings.db.port,
            username=settings.db.username,
            password=settings.db.password,
            database=settings.db.database,
        )

    def product(self, product: Products) -> None:
        """Import a product record"""
        with Session(bind=self.engine, expire_on_commit=False) as session, session.begin():
            session.merge(product)
