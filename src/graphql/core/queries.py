from typing import List

import strawberry

from src.graphql.controller.queries import CreateQueries
from src.graphql.schema.products import ProductsType

queries = CreateQueries()


@strawberry.type
class Query:

    """GraphQL queries"""

    search: List[ProductsType] = strawberry.field(resolver=queries.search)
