from enum import StrEnum

from pydantic import BaseModel


class DataTypes(StrEnum):
    object: str = "object"
    int64: str = "int64"
    float64: str = "float64"


class ColumnSchema(BaseModel):
    column_name: str
    column_type: DataTypes
