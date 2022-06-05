from pydantic import Field
from .base_schema import BaseModel

class UserLogin(BaseModel):
    email: str = Field(...)
    password: str = Field(...)


class UserSignup(UserLogin):
    name: str = Field(...)
    lastName: str = Field(...)
    phoneNumber: int = Field(...)
    address: str = Field(...)
    birthDate: str = Field(...)
    picture: str = Field(...)
    city: int = Field(...)
    color: str = Field(...)


class UserModel(UserSignup):
    userId: int = Field(...)
    role: int = Field(...)
    status: int = Field(...)
    exist: bool = Field()
    
