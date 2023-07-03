from typing import List

from sqlalchemy import Engine
from sqlalchemy.orm import Session

from data import NikeDataset

from .tables import Products


def _build_records(dataset: NikeDataset) -> List[Products]:
    """Build list of records to insert into database"""
    records = []
    for _, row in dataset.df.iterrows():
        records.append(Products(**row))
    return records


def import_product(dataset: NikeDataset, engine: Engine) -> None:
    """Batch import product data"""
    records = _build_records(dataset)
    session = Session(bind=engine)
    session.add_all(records)
    session.flush()
    session.commit()
