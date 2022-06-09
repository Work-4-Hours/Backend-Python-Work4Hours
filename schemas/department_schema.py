from pydantic import Field
from .base_schema import BaseModel

class Department(BaseModel):
    departmentid: int = Field(...)
    name: str = Field(...)

