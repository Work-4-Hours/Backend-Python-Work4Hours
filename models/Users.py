import base64
import string
from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref
from models.City import City
from models.Rol import Rol
from models.Statuses import Statuses
from jwt_Functions import write_token, validate_token
import bcrypt


class Users(db.Model):
    __tablename__ = 'user'
    userid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable= False)
    lastname = db.Column(db.String(60), nullable= False)
    phone = db.Column(db.String(30), nullable= False)
    address = db.Column(db.String(500), nullable= True)
    email = db.Column(db.String(500), nullable = False)
    password = db.Column(db.String(150), nullable= False)
    birthdate = db.Column(db.Date, nullable= False)
    picture = db.Column(db.String(500), nullable= True)
    color = db.Column(db.String(8), nullable= True)
    city = db.Column(db.Integer, ForeignKey('city.cityid'),nullable = False)
    cities = relationship(City, backref=backref('user', uselist=True))
    role = db.Column(db.Integer, ForeignKey('role.roleid'),nullable= False)
    roles = relationship(Rol, backref=backref('user', uselist=True))
    status = db.Column(db.Integer, ForeignKey('status.statusid'),nullable = False)
    statuses = relationship(Statuses, backref=backref('user', uselist=True))


    def __init__(self,name,lastName,phoneNumber,address,email,password,birthDate,picture,city,color):
        self.name= name
        self.lastname = lastName
        self.phone = phoneNumber
        self.address = address
        self.email = email
        self.password = password
        self.birthdate = birthDate
        self.picture = picture
        self.city = city
        self.role = 2
        self.estatus = 1
        self.color = color


    # #Function to decrypt passwords
    # def decrypt_password(password : str, dbHashedPWD: str):
    #     encodedPassword = password.encode(encoding='UTF-8')
    #     encodedHash = dbHashedPWD.encode(encoding='UTF-8')
    #     return bcrypt.checkpw(encodedPassword,encodedHash)


    # #Funtion to encrypt passwords
    # def encrypt_password(password):
    #     encoded = bytes(password.encode(encoding='UTF-8'))
    #     return bcrypt.hashpw(encoded,salt)


    # #Function to get the password from de db and decrypt it if it exist
    # def get_decrypted_user_password(self,password : str, email : str) :
    #     decryptedPassword = False
    #     queryPassword =select(self.contrasenna).where(self.correo == email)
    #     passwordResult = db.session.execute(queryPassword)
    #     for dbpassword in passwordResult.scalars():
    #         if (dbpassword):
    #             decryptedPassword = self.decrypt_password(password,dbpassword)
    #     return decryptedPassword 


    # #function to validate existance of an user in db: 
    # def get_existant_user(self,email:str , password:str , type:int) :
    #     userId = {}
    #     user = {}
    #     result = db.session.execute(db.session.query(Users).filter(self.correo == email))
    #     if(result.scalars() and type == 1):
    #         if(self.get_decrypted_user_password(password,email)):
    #             user, userId = self.get_user_info(result.scalars())
    #     elif(result.scalars() and type == 0):
    #         user, userId = self.get_user_info(result.scalars())
    #     db.session.commit()
    #     return user, userId


    # def get_user_info(result):
    #     userId = {}
    #     user = {}
    #     for userInfo in result:
    #         user = {
    #             "name" : userInfo.nombres,
    #             "lastName" : userInfo.apellidos,
    #             "email" : userInfo.correo,
    #             "status" : userInfo.estado,
    #             "userPicture" : userInfo.fotop,
    #             "phoneNumber": userInfo.celular,
    #             "birthDate": userInfo.fnac,
    #             "color": userInfo.color,
    #         },
    #         userId = {
    #             "userId" : userInfo.idusuario,
    #             "rol" : userInfo.rol
    #         }
    #     return user,userId


    # #Function to decide if the user must be registered
    # def validate_registry(self,nombres,apellidos,celular,direccion,correo,contrasenna,fnac,fotop,ciudad,color):
    #     user= self.get_existant_user(correo,contrasenna,0)
    #     if(bool(user) == False):
    #         encryptedPassword = self.encrypt_password(contrasenna)
    #         newUser = Users(nombres,apellidos,celular,direccion,correo,encryptedPassword,fnac,fotop,ciudad,color)
    #         db.session.add(newUser)
    #         db.session.commit()
    #         return {"exist": "new User created"}
    #     else:
    #         return {"exist": "User already exist"}


    # #Function to look for a user in DB and take his info:
    # def login(self,email:str , password:str):
    #     user, userId = self.get_existant_user(email,password,1)
    #     if (user):
    #         token = str(write_token(userId)).split("'")[1]
    #         return {"token":token, "info":user, "exist": True}
    #     else:
    #         return {"exist":False}


    # #Function to search all users in the app
    # def search_user_info(self,userId):
    #     user = {}
    #     try:           
    #         if (type(userId) != int):
    #             decryptedUserId = validate_token(userId,True)
    #             result = db.session.execute(select(Users).filter(self.idusuario == decryptedUserId.get('userId')))
    #         else:
    #             result = db.session.execute(select(Users).filter(self.idusuario == userId))
    #     except UnicodeDecodeError as err:
    #         raise(err)
    #     except ConnectionAbortedError as err:
    #         raise(err)
    #     else:
    #         for usersInfo in result.scalars():
    #             user = {
    #                 "name" : usersInfo.nombres,
    #                 "lastName" : usersInfo.apellidos,
    #                 "photo": usersInfo.fotop,
    #                 "phoneNumber": usersInfo.celular,
    #                 "email": usersInfo.correo,
    #                 "color": usersInfo.color,
    #             }
    #         db.session.commit()
    #         return user

