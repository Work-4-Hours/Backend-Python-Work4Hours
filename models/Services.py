from unittest import result
from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref
from models.Categories import Categories
from models.Statuses import Statuses
from models.Users import Users


class Services(db.Model):
    __tablename__ = 'servicios'
    idservicio = db.Column(db.Integer, primary_key=True)
    idcategoria = db.Column(db.String(3), ForeignKey('categorias.idcategoria'),nullable=False)
    categorias = relationship(Categories, backref=backref('servicios', uselist=True))
    nombre = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.Integer, ForeignKey('estados.id'),nullable=False)
    estados = relationship(Statuses, backref=backref('servicios', uselist=True))
    tipo = db.Column(db.String(1), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String(2000), nullable=False)
    foto = db.Column(db.String(500), nullable=False)
    usuario = db.Column(db.Integer, ForeignKey('usuarios.idusuario'),nullable=False)
    usuarios = relationship(Users, backref=backref('servicios', uselist=True))


    def __init__(self, idcategoria, nombre, estado, tipo, precio, descripción, foto, usuario):
        self.idcategoria=idcategoria
        self.nombre=nombre
        self.estado=estado
        self.tipo=tipo
        self.precio=precio
        self.descripcion=descripción
        self.foto=foto
        self.usuario=usuario

    
    def searchAllServicesInfo(nombre):
        services = {}
        query = select(Services).where(Services.nombre.like(services)).all()
        result = db.session.execute(query)
        if (bool(services) == True):
            for serviceInfo in result.scalars():
                services.append(
                    {
                        "name": serviceInfo.nombre
                    }
                )
            db.session.commit()

            return services
        
        else:
            return {"Coincidence": "No results found"}