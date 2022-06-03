from pydantic import Field
from .base_schema import BaseModel

class UserLogin(BaseModel):
    correo: str = Field(..., alias="email")
    contrasenna: str = Field(...,alias="password")


class UserSignup(UserLogin):
    nombre: str = Field(..., alias="name")
    apellido: str = Field(..., alias="lastName")
    celular: int = Field(..., alias="phoneNumber")
    direccion: str = Field(..., alias="address")
    fnac: str = Field(..., alias="birthDate")
    fotop: str = Field(..., alias="picture")
    ciudad: int = Field(..., alias="city")
    color: str = Field(..., alias="color")


class UserModel(UserSignup):
    idusuario: int = Field(..., alias="userId")
    rol: int = Field(..., alias="role")
    estado: int = Field(..., alias="status")
    exist: str = Field(...)
    
