from pydantic import Field
from .base_schema import BaseModel

class Department(BaseModel):
    departamentid: int = Field(...)
    name: str = Field(...)

