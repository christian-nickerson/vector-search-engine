from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pgvector.sqlalchemy import Vector
from sqlalchemy import Engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Products(Base):

    """Nike Products table"""

    __tablename__: str = "products"

    uniq_id: Mapped[UUID] = mapped_column(primary_key=True)
    embedding: Mapped[Optional[Vector]] = mapped_column(Vector, index=True)
    url: Mapped[str]
    name: Mapped[str]
    sub_title: Mapped[str]
    brand: Mapped[str]
    model: Mapped[int]
    color: Mapped[str]
    price: Mapped[Decimal]
    currency: Mapped[str]
    availability: Mapped[str]
    description: Mapped[str]
    avg_rating: Mapped[Optional[float]]
    review_count: Mapped[Optional[float]]
    images: Mapped[str]
    available_sizes: Mapped[Optional[str]]
    scraped_at: Mapped[datetime]


def create_tables(engine: Engine) -> None:
    """create all database tables"""
    Base.metadata.create_all(engine)
