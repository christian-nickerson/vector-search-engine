from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from uuid import UUID

import strawberry


@strawberry.type
class ProductsType:

    """Products type schmea"""

    uniq_id: UUID
    embedding: List[float]
    url: str
    name: str
    sub_title: str
    brand: str
    model: int
    color: str
    price: Decimal
    currency: str
    availability: str
    description: str
    avg_rating: Optional[float] = None
    review_count: Optional[float] = None
    images: str
    available_sizes: Optional[str] = None
    scraped_at: datetime


@strawberry.input
class ProductsInput:

    """Products input schema"""

    uniq_id: UUID
    url: str
    name: str
    sub_title: str
    brand: str
    model: int
    color: str
    price: Decimal
    currency: str
    availability: str
    description: str
    avg_rating: Optional[float] = None
    review_count: Optional[float] = None
    images: str
    available_sizes: Optional[str] = None
    scraped_at: datetime
