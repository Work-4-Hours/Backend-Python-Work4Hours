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
            loged_user : UserModel()
            db_data = session.execute(session.query(Users).filter(Users.email == user.email))
            for db_user in db_data.scalars():
                loged_user = UserModel(**db_user.__dict__)
            session.commit()
            if(cls.decrypt_password(user.password,loged_user.password)):
                return loged_user
            else:
                return None

    @classmethod
    def signup(cls, user: UserSignup) -> dict:
        with get_session() as session:
            db_data = session.execute(session.query(Users).filter(Users.email == user.email))    
            if(db_data.scalars()):
                return None
            else:
                newUser = Users(**user.__exclude_fields__("exist"))
                session.add(newUser)
                session.commit()
                return True


