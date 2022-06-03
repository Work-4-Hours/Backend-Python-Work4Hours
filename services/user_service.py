from passlib.context import CryptContext

from schemas import UserLogin, UserSignup
from models.Users import Users

class UserService:

    __password_context__ = CryptContext(
        schemes=["bcrypt"]
    )

    @classmethod
    def login(
        cls,
        email: str,
        password: str
    ) -> Users:
        try:
            usr = Users.filter(correo=email)
            if not validate_pasword:
                return None
            return usr 
        except:
            pass
        else:
            pass

    @classmethod
    def verify_password(cls, password: str, plain: str) -> bool:
        return cls.__password_context__.verify(password, plain)
    
    @classmethod
    def encrypt_password(cls, plain_password: str) -> str:
        return cls.__password_context__.encrypt(plain_password)