from pydantic import Field

from .base_schema import BaseModel
from .user_schema import UserModel


class IndexService(BaseModel):
    serviceid: int = Field(...)
    categoryid: str = Field(...)
    name: str = Field(...)
    price: int = Field(...)
    picture: str = Field(...)
    city: int = Field(None)
    user: str = Field(...)
    qualification: float = Field(None)


class ServiceModel(IndexService):
    description: str = Field(...)
    status: int = Field(...)
    type: str = Field(...)
    appeals: int = Field(...)
    userInfo: UserModel = Field(None)


class ServiceUpdate(BaseModel):
    serviceid: int = Field(...)
    categoryid: str = Field(...)
    name: str = Field(...)
    price: int = Field(...)
    picture: str = Field(...)
    description: str = Field(...)
    type: str = Field(...)
    status: int = Field(...)