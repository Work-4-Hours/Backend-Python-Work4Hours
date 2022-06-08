from datetime import date
from pydantic import Field
from .base_schema import BaseModel
from .service_schema import ServiceModel


class UserLogin(BaseModel):
    email: str = Field(...)
    password: str = Field(...)


class UserSignup(UserLogin):
    name: str = Field(...)
    lastName: str = Field(...)
    phoneNumber: int = Field(...)
    address: str = Field(...)
    birthDate: date = Field(...)
    picture: str = Field(...)
    city: int = Field(...)
    color: str = Field(...)


class UserModel(UserSignup):
    role: int = Field(...)
    status: int = Field(...)
    userId: int = Field(...)
    exist: bool = Field(None)
    services: ServiceModel = Field(None)


