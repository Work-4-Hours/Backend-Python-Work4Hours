from distutils.debug import DEBUG
from pydantic import Field
from .base_schema import BaseModel
from .department_schema import Department

class City(BaseModel):
    cityid: int = Field(...)
    name: str = Field(...)
    departmentid: Department = Field(...)