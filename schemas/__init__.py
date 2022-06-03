from pydantic import BaseModel as PydanticBaseModel

from .user_schema import UserLogin, UserSignup

class BaseModel(PydanticBaseModel):

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True