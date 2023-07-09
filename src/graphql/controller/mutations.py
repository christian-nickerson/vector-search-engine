from strawberry import asdict

from src.database.ingress import ImportClient
from src.database.models import Products
from src.embeddings.engine import EmbeddingEngine
from src.graphql.schema.products import ProductsInput


class CreateMutation:

    """GraphQL mutation resolvers"""

    def __init__(self) -> None:
        self.import_client = ImportClient()
        self.embedding_engine = EmbeddingEngine()

    def add_product(self, data: ProductsInput) -> Products:
        """Add a product to the database

        :param data: Data to be added to the database
        :return: Products
        """
        product_data = asdict(data)
        product_data["embedding"] = self.embedding_engine.embed(data.description)
        product = Products(**product_data)
        self.import_client.product(product)
        return product
