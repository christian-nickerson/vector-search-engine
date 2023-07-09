import strawberry

from src.graphql.controller.mutations import CreateMutation
from src.graphql.schema.products import ProductsType

mutations = CreateMutation()


@strawberry.type
class Mutation:

    """GraphQL mutations"""

    add_product: ProductsType = strawberry.mutation(resolver=mutations.add_product)
