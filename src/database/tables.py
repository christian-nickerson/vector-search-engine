from typing import Any, Dict, List, Union

from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import declarative_base

from .schema import ColumnSchema, DataTypes

Base = declarative_base()


class Table:

    """dynamically create a SQLAlchemy table class"""

    def __init__(self, table_name: str, table_spec: List[Dict[str, str]]) -> None:
        self.table_spec = self._table_attr(table_name, table_spec)

    def _table_attr(self, table_name: str, table_spec: List[Dict[str, str]]) -> Dict[str, Union[str, Column]]:
        """build table spec"""
        spec = {"__tablename__": table_name}
        for item in table_spec:
            schema = ColumnSchema.parse_obj(item)
            data_type = self._type_conversion(schema.column_type)
            spec[schema.column_name] = Column(data_type)
        return spec

    @staticmethod
    def _type_conversion(numpy_type: str) -> Union[Integer, String]:
        """Convert a numpy type (name) to a SQL Alchemy type"""
        match numpy_type:
            case DataTypes.object:
                return String
            case DataTypes.int64:
                return Integer
            case DataTypes.float64:
                return Float
            case _:
                raise ValueError(f"Unmapped numpy type: {numpy_type}")

    def get_table(self, class_name: str) -> Any:
        """get table class"""
        print(self.table_spec)
        return type(class_name, (Base,), self.table_spec)
