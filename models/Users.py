from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select, true
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import text
from models.City import City
from models.Rol import Rol
from models.Statuses import Statuses
from jwt_Functions import write_token, validate_token
import os
from config import salt
import bcrypt


class Users(db.Model):
    __tablename__ = 'usuarios'
    idusuario = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(60), nullable= False)
    apellidos = db.Column(db.String(60), nullable= False)
    celular = db.Column(db.String(30), nullable= False)
    direccion = db.Column(db.String(500), nullable= True)
    correo = db.Column(db.String(500), nullable = False)
    contrasenna = db.Column(db.String(150), nullable= False)
    fnac = db.Column(db.Date, nullable= False)
    fotop = db.Column(db.String(500), nullable= True)
    color = db.Column(db.String(8), nullable= True)
    ciudad = db.Column(db.Integer, ForeignKey('ciudades.idciudad'),nullable = False)
    ciudades = relationship(City, backref=backref('usuarios', uselist=True))
    rol = db.Column(db.Integer, ForeignKey('roles.idrol'),nullable= False)
    roles = relationship(Rol, backref=backref('usuarios', uselist=True))
    estado = db.Column(db.Integer, ForeignKey('estados.id'),nullable = False)
    estados = relationship(Statuses, backref=backref('usuarios', uselist=True))



    def __init__(self,nombres,apellidos,celular,direccion,correo,contrasenna,fnac,fotop,ciudad,color):
        self.nombres= nombres
        self.apellidos = apellidos
        self.celular = celular
        self.direccion = direccion
        self.correo = correo
        self.contrasenna = contrasenna
        self.fnac = fnac
        self.fotop = fotop
        self.ciudad = ciudad
        self.rol = 2
        self.estado = 1
        self.color = color



    #Function to decrypt passwords
    @staticmethod
    def decrypt_password(password : str, dbHashedPWD: str):
        encodedPassword = password.encode(encoding='UTF-8')
        encodedHash = dbHashedPWD.encode(encoding='UTF-8')
        return bcrypt.checkpw(encodedPassword,encodedHash)



    #Funtion to encrypt passwords
    @staticmethod
    def encrypt_password(password):
        encoded = bytes(password.encode(encoding='UTF-8'))
        return bcrypt.hashpw(encoded,salt)

    #Function to get the password from de db and decrypt it if it exist
    @classmethod
    def get_decrypted_user_password(self,password : str, email : str) :
        decryptedPassword = False
        queryPassword =select(self.contrasenna).where(Users.correo == email)
        passwordResult = db.session.execute(queryPassword)
        for dbpassword in passwordResult.scalars():
            if (dbpassword):
                decryptedPassword = Users.decrypt_password(password,dbpassword)
        return decryptedPassword 



    #function to validate existance of an user in db: 
    # @classmethod
    # def get_existant_user(self,email:str , password:str , type:int) :
    #     userId = {}
    #     user = {}
    #     result = db.session.execute(db.session.query(Users).filter(Users.correo == email))
    #     if(result.scalars() and type == 1):
    #         if(self.get_decrypted_user_password(password,email)):
    #             user, userId = self.get_user_info(result.scalars())
    #     elif(result.scalars() and type == 0):
    #         user, userId = self.get_user_info(result.scalars())
    #     db.session.commit()
    #     return user, userId

    @classmethod
    def get_user(cls, email: str, password: str):
        userId: dict = {}
        user: dict = {}
        result = db.session.execute(db.session.query(Users).filter(Users.correo == email))
        scalar = result.scalars().first()
        if(not scalar):
            return None
        if(cls.decrypt_password(password, scalar.contrasenna)):
            user, userId = cls.get_user_info(scalar)
            return user, userId


    @classmethod
    def get_user_info(self,userInfo):
        user = {
            "name" : userInfo.nombres,
            "lastName" : userInfo.apellidos,
            "email" : userInfo.correo,
            "status" : userInfo.estado,
            "userPicture" : userInfo.fotop,
            "phoneNumber": userInfo.celular,
            "birthDate": userInfo.fnac,
            "color": userInfo.color,
        },
        userId = {
            "userId" : userInfo.idusuario,
            "rol" : userInfo.rol
        }
        return user,userId



    #Function to decide if the user must be registered
    @classmethod
    def validate_registry(self,nombres,apellidos,celular,direccion,correo,contrasenna,fnac,fotop,ciudad,color):
        user = self.get_user(correo,contrasenna)
        if(user):
            return {"exist": "User already exist"}
        else:
            encryptedPassword = Users.encrypt_password(contrasenna)
            newUser = Users(nombres,apellidos,celular,direccion,correo,encryptedPassword,fnac,fotop,ciudad,color)
            db.session.add(newUser)
            db.session.commit()
            return {"exist": "new User created"}



    #Function to look for a user in DB and take his info:
    @classmethod
    def login(self,email:str , password:str):
        user, userId = self.get_user(email,password)
        if (user):
            token = str(write_token(userId)).split("'")[1]
            return {"token":token, "info":user, "exist": True}
        else:
            return {"exist":False}



    #Function to search all users in the app
    @classmethod
    def search_user_info(self,userId):
        user = {}
        try:           
            if (type(userId) != int):
                decryptedUserId = validate_token(userId,True)
                result = db.session.execute(select(Users).filter(self.idusuario == decryptedUserId.get('userId')))
            else:
                result = db.session.execute(select(Users).filter(self.idusuario == userId))
        except UnicodeDecodeError as err:
            return(err)
        except ConnectionAbortedError as err:
            return(err)
        else:
            for usersInfo in result.scalars():
                user = {
                    "name" : usersInfo.nombres,
                    "lastName" : usersInfo.apellidos,
                    "photo": usersInfo.fotop,
                    "phoneNumber": usersInfo.celular,
                    "email": usersInfo.correo,
                    "color": usersInfo.color,
                }
            db.session.commit()
            return user


    @classmethod
    def update_user_info(cls, userId:str ,**args: any) -> None:
        db.session.execute(text(
            """UPDATE usuarios 
            SET nombres = :name,
            apellidos= :lastName, 
            direccion = :address,
            celular = :phoneNumber
            WHERE idusuario = :userId"""
        ).bindparams(
            name = args["name"],
            lastName = args["lastName"],
            address = args["address"],
            phoneNumber = args["phoneNumber"],
            userId = userId
        ))
        db.session.commit()



