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
            # loged_user : UserModel()
            db_data = session.execute(session.query(Users).filter(Users.email == user.email).first())
            # for db_user in db_data.scalars():
            print(db_data)
            loged_user = UserModel(**db_data.__dict__)
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
            print(db_user)
            if(not db_user):
                return None
            newUser = Users(**user)
            session.add(newUser)
            session.commit()
            return True


