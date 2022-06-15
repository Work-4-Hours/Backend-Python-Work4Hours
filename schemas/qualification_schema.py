from pydantic import Field
from .base_schema import BaseModel

class Qualification(BaseModel):
    qualification: int = Field(...)
    userId: int = Field(None)
    serviceid: int = Field(None)