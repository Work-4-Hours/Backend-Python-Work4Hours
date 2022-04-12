from typing_extensions import Self
from unittest import result
from utils.db import db
from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, select, insert, update
from sqlalchemy.orm import relationship, backref
from models.Categories import Categories
from models.Statuses import Statuses
from models.Users import Users
from models.Appeals import Appeals
from jwt_Functions import write_token




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
    apelacion = db.Column(db.Integer,ForeignKey('apelaciones.idapelacion'),nullable=True)
    apelaciones = relationship(Appeals, backref= backref('servicios'),uselist= True)
    calificacion = db.Column(db.Float(), nullable=False)
         


    def __init__(self, idcategoria, nombre, estado, tipo, precio, descripcion, foto, usuario):
        self.idcategoria=idcategoria
        self.nombre=nombre
        self.estado=estado
        self.tipo=tipo
        self.precio=precio
        self.descripcion=descripcion
        self.foto=foto
        self.usuario=usuario
        

    def getIndexPageServices():
        services = []
        query = db.session.query(Services).filter(Services.calificacion >= 4.0).limit(20)
        result = db.session.execute(query)
        for serviceInfo in result.scalars():
            token = str(write_token(serviceInfo.usuario)).split("'")[1]
            services.append(
                {
                    "name": serviceInfo.nombre,
                    "id" : serviceInfo.idservicio,
                    "price": serviceInfo.precio,
                    "photo": serviceInfo.foto,
                    "user": token
                }
            )
            db.session.commit()
        return services

    
    def validateService(idcategoria,nombre,estado,tipo,precio,descripcion,foto,usuario):
        newService = Services(idcategoria,nombre,estado,tipo,precio,descripcion,foto,usuario)
        db.session.add(newService)
        db.session.commit()



    def searchAllServicesInfo(nombreServicio):
        services = []
        query = db.session.query(Services).filter(Services.nombre.like('%{}%'.format(nombreServicio)))
        result = db.session.execute(query)
        for serviceInfo in result.scalars():
            token = str(write_token(serviceInfo.usuario)).split("'")[1]
            services.append(
                {
                    "name": serviceInfo.nombre,
                    "id" : serviceInfo.idservicio,
                    "price": serviceInfo.precio,
                    "photo": serviceInfo.foto,
                    "user": token
                }
                
            )
            db.session.commit()
        return services


    def addQualification(self):
        query = update({'calificacion': Services.calificacion})
        db.session.execute(query)
        db.session.commit()

        


    
        
        