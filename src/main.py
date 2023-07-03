from data import NikeDataset
from database.tables import Table

if __name__ == "__main__":
    nd = NikeDataset()
    table = Table("products", nd.column_types)
    Products = table.get_table("Products")
    print(Products)
