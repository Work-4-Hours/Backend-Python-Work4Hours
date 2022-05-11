import base64
import string
from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref
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
        self.rol = 1
        self.estado = 1
        self.color = color


    #Function to decrypt passwords
    def decryptPassword(password : str, dbHashedPWD: str):
        encodedPassword = password.encode(encoding='UTF-8')
        encodedHash = dbHashedPWD.encode(encoding='UTF-8')
        return bcrypt.checkpw(encodedPassword,encodedHash)


    #Funtion to encrypt passwords
    def encryptPassword(password):
        encoded = bytes(password.encode(encoding='UTF-8'))
        return bcrypt.hashpw(encoded,salt)


    #Function to get the password from de db and decrypt it if it exist
    def getDecryptedUserPassword(password : str, email : str) -> bool :
        decryptedPassword = ""
        queryPassword =select(Users.contrasenna).where(Users.correo == email)
        passwordResult = db.session.execute(queryPassword)
        for dbpassword in passwordResult.scalars():
            if (dbpassword):
                decryptedPassword = Users.decryptPassword(password,dbpassword)
            else:
                decryptedPassword = False
        return decryptedPassword 


    #function to validate existance of an user in db: 
    def getExistantUser(email,password, type):
        userId = {}
        user = {}
        query = db.session.query(Users).filter(Users.correo == email)
        result = db.session.execute(query)
        if(result.scalars() and type == 1):
            if(Users.getDecryptedUserPassword(password,email)):
                user, userId = Users.getUserInfo(result.scalars())
        elif(result.scalars() and type == 0):
            user, userId = Users.getUserInfo(result.scalars())
        db.session.commit()
        return user, userId


    def getUserInfo(result):
        userId = {}
        user = {}
        for userInfo in result:
            user = {
                "name" : userInfo.nombres,
                "lastName" : userInfo.apellidos,
                "email" : userInfo.correo,
                "status" : userInfo.estado,
                "userPicture" : userInfo.fotop,
                "color": userInfo.color
            },
            userId = {
                "id" : userInfo.idusuario,
                "rol" : userInfo.rol
            }
        return user,userId


    #Function to decide if the user must be registered
    def validateRegistry(nombres,apellidos,celular,direccion,correo,contrasenna,fnac,fotop,ciudad,color):
        user, userId = Users.getExistantUser(correo,contrasenna,0)
        if(bool(user) == False):
            encryptedPassword = Users.encryptPassword(contrasenna)
            newUser = Users(nombres,apellidos,celular,direccion,correo,encryptedPassword,fnac,fotop,ciudad,color)
            db.session.add(newUser)
            db.session.commit()
            return {"exist": "new User created"}
        else:
            return {"exist": "User already exist"}


    #Function to look for a user in DB and take his info:
    def login(email,password):
        user, userId = Users.getExistantUser(email,password,1)
        if (user):
            token = str(write_token(userId)).split("'")[1]
            return {"token":token, "info":user, "exist": True}
        else:
            return {"exist":False}


    #Function to search all users in the app
    def searchUserInfo(encryptedId):
        users = []
        userId = validate_token(encryptedId,True)
        query = select(Users).filter(Users.idusuario == userId.id)
        result = db.session.execute(query)
        for usersInfo in result.scalars():
            {
                "name" : usersInfo.nombres,
                "lastName" : usersInfo.apellidos,
                "photo": usersInfo.fotop,
                "color": usersInfo.color,
            }
        db.session.commit()
        return users
