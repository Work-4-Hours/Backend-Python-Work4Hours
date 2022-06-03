from passlib.context import CryptContext
from schemas import UserLogin,UserSignup,UserModel
from models.Users import Users
from utils.db import get_session

class UserService:

    __password_context__ = CryptContext(
        schemes= ["bcrypt"]
    )

    @classmethod
    def encrypt_password(cls, plain: str) -> str:
        return cls.__password_context__.encrypt(plain)

    def decrypt_password(cls, plain: str, hashedPassword: str) -> bool:
        return cls.__password_context__.verify(plain,hashedPassword)

    @classmethod
    def login(cls, user: UserLogin) -> dict:
        with get_session() as session:
            db_data = session.execute(session.query(Users).filter(Users.correo == user.correo))
            for db_user in db_data.scalars():
                loged_user = UserModel(db_user,exist=True)
            session.commit()
            if(cls.decrypt_password(user.contrasenna,loged_user.contrasenna)):
                return loged_user
            else:
                return None


    @classmethod
    def signup(cls, user: UserSignup) -> dict:
        with get_session as session:
            db_data = session.execute(session.query(Users).filter(Users.correo == user.correo))    
            if(db_data.scalars()):
                return {"exist":"User already exist"}
            else:
                newUser = Users(**user)
                session.add(newUser)
                session.commit()
                return {"exist":"New user created"}


