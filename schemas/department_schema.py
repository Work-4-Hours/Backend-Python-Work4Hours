from pydantic import Field
from .base_schema import BaseModel

class Department(BaseModel):
    departmenid: int = Field(...)
    name: str = Field(...)

