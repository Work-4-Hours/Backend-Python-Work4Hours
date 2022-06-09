from pydantic import Field
from .base_schema import BaseModel
from .city_schema import City


class IndexService(BaseModel):
    serviceid: int = Field(...)
    categoryid: int = Field(...)
    name: str = Field(...)
    price: int = Field(...)
    picture: str = Field(...)
    city: City = Field(...)
    user: str = Field(...)


class ServiceModel(IndexService):
    description: str = Field(...)
    status: int = Field(...)
    type: str = Field(...)
    appeals: int = Field(...)
    qualification: float = Field(...)

