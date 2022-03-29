from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref

class Users(db.Model):
    __tablename__ = 'usuarios'
    idusuario = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(60), nullable= False)
    apellidos = db.Column(db.String(60), nullable= False)
    celular = db.Column(db.String(30), nullable= False)
    direccion = db.Column(db.String(500), nullable= False)
    correo = db.Column(db.String(500), nullable = False)
    contrasenna = db.Column(db.String(45), nullable= False)
    fnac = db.Column(db.Date, nullable= False)
    fotop = db.Column(db.String(500), nullable= True)
    ciudad = db.Column(db.Integer, ForeignKey('ciudades.idciudad'),nullable = False)
    ciudades = relationship(City, backref=backref('usuarios', uselist=True))
    rol = db.Column(db.Integer, ForeignKey('roles.idrol'),nullable= False)
    roles = relationship(Rol, backref=backref('usuarios', uselist=True))
    estado = db.Column(db.Integer, ForeignKey('estados.id'),nullable = False)
    estados = relationship(Statuses, backref=backref('usuarios', uselist=True))

    def __init__(self,nombres,apellidos,celular,direccion,correo,contrasenna,fnac,fotop,ciudad):
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

    #function to validate existance of an user in db: 
    def validateExistantUser(email,password):
        user = {}
        query = select(Users).where((Users.correo == email and Users.contrasenna == password))
        result = db.session.execute(query)
        for userInfo in result.scalars():
            user = {
                "id" : userInfo.idusuario,
                "name" : userInfo.nombres,
                "lastName" : userInfo.apellidos,
                "email" : userInfo.correo,
                "status" : userInfo.estado,
                "rol" : userInfo.rol,
                "userPicture" : userInfo.fotop
            }
        db.session.commit()
        return user

    def validateRegistry(nombres,apellidos,celular,direccion,correo,contrasenna,fnac,fotop,ciudad):
        user = Users.validateExistantUser(correo,contrasenna)
        if(bool(user) == False):
            newUser = Users(nombres,apellidos,celular,direccion,correo,contrasenna,fnac,fotop,ciudad)
            db.session.add(newUser)
            db.session.commit()
            return {"exist": "new User created"}
        else:
            return {"exist": "User already exist"}

    #Function to look for a user in DB and take his info:
    def searchUserInfo(email,password):
        user = Users.validateExistantUser(email,password)
        if (user):
            token = str(write_token(user)).split("'")[1]
            return {"token":token}
        else:
            return {"exist":False}

    #Function to search all users in the app
    def searchAllUsersInfo():
        users = []
        query = select(Users)
        result = db.session.execute(query)
        for usersInfo in result.scalars():
            users.append(
                {
                    "name" : usersInfo.nombres,
                    "lastName" : usersInfo.apellidos,
                    "email" : usersInfo.correo
                }
            )

        db.session.commit()

        return users
