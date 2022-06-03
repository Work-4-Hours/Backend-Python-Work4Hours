from pydantic import Field

from . import BaseModel

class UserLogin(BaseModel):
    correo: str = Field(..., alias="email")
    contrasenna: str = Field(..., alias="password")

class UserSignup(UserLogin):
    nombres: str = Field(..., alias="name")
    apellidos: str = Field(..., alias="lastName")
    celular: str = Field(..., alias="phoneNumber")
    direccion: str = Field(..., alias="address")
    fnac: str = Field(..., alias="birthDate")
    fotop: str = Field(..., alias="picture")
    ciudad: str = Field(..., alias="city")
    color: str = Field(..., alias="color")
