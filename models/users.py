import email
from this import d
from utils.db import db

class Users(db.model):
    __tablename__ = 'usuarios'
    idusuario = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(60), nullable= False)
    apellidos = db.Column(db.String(60), nullable= False)
    celular = db.Columnn(db.String(30), nullable= False)
    direccion = db.Column(db.String(500), nullable= False)
    correo = db.Column(db.String(500), nullable = False)
    contrasenna = db.Column(db.String(45), nullable= False)
    fnac = db.Column(db.Date, nullable= False)
    fotop = db.Column(db.String(500), nullable= True)
    ciudad = db.Column(db.Integer, nullable = False)
    rol = db.Column(db.Integer, nullable= False)
    estado = db.Column(db.Integer, nullable = False)

    def __init__(self,nombres,apellidos,celular,direccion,correo,contrasenna,fnac,fotop,ciudad,rol,estado):
        self.nombres= nombres
        self.apellidos = apellidos
        self.celular = celular
        self.direccion = direccion
        self.correo = correo
        self.contrasenna = contrasenna
        self.fnac = fnac
        self.fotop = fotop
        self.ciudad = ciudad
        self.rol = rol
        self.estado = estado