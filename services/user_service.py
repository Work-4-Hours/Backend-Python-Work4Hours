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
        return cls.__password_context__.hash(plain)


    @classmethod
    def decrypt_password(cls, plain: str, hashedPassword: str) -> bool:
        return cls.__password_context__.verify(plain,hashedPassword)


    @classmethod
    def login(cls, user: UserLogin) -> UserModel:
        with get_session() as session:
            db_data = session.execute(session.query(Users).filter(Users.email == user.email))
            user_data = db_data.scalars().one()
            loged_user = UserModel(**user_data.__dict__,exist= True)
            session.commit()
            if(cls.decrypt_password(user.password,loged_user.password)):
                return loged_user
            else:
                return None


    @classmethod
    def signup(cls, user: UserSignup) -> dict:
        with get_session() as session:
            db_data = session.execute(session.query(Users).filter(Users.email == user.email))    
            db_user = db_data.scalars().first()
            if(db_user):
                return None
            hashed_password = cls.encrypt_password(user.password)
            user.password = hashed_password
            newUser = Users(
                **user.dict()
            )
            print(newUser)
            session.add(newUser)
            session.commit()
            return True


