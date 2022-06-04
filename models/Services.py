from unittest import result
from utils.db import db
from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, select, insert, update, delete
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship, backref
from models.Categories import Categories
from models.Statuses import Statuses
from models.Users import Users
from models.Appeals import Appeals
from models.Departament import Departament
from models.City import City
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


    @classmethod
    def get_index_page_services(self) -> list :
        services = []
        query = db.session.query(Services).filter(self.calificacion >= 4.0).filter(self.estado == 1).limit(20)
        result = db.session.execute(query)
        for serviceInfo in result.scalars():
            services.append(
                self.extract_service_info(serviceInfo)
            )
        db.session.commit()
        return services

<<<<<<< HEAD
    def getServiceInfo(serviceId:int):
        service = ""
        query = db.session.query(Services).filter(Services.idservicio == serviceId)
        result = db.session.execute(query)
        for serviceInfo in result.scalars():
            service = Services.extractServiceInfo(serviceInfo)
        return service
=======
    
    @classmethod
    def get_service_info(self,serviceId):
        service = ""
        query = db.session.execute(db.session.query(Services).filter(self.idservicio == serviceId))
        for serviceInfo in query.scalars():
            service = self.extract_service_info(serviceInfo)
        user = Users.search_user_info(service['user'])
        db.session.commit()
        return {"serviceInfo":service,"serviceUser":user}
>>>>>>> ba60fe0b2d757d1adac4cfc82c4a0506d78dc251


    @classmethod
    def extract_service_info(self,serviceInfo):
        service = {}
        departmentId,cityId,cityName = City.get_city_info(serviceInfo.idservicio,serviceInfo.usuario)
        departmentName = Departament.get_department_info(departmentId)
        token = str(write_token({"userId" : serviceInfo.usuario})).split("'")[1]
        service = {
            "name": serviceInfo.nombre,
            "id" : serviceInfo.idservicio,
            "price": serviceInfo.precio,
            "photo": serviceInfo.foto,
            "city_code": cityId,
            "city_name": cityName,
            "department_code":departmentId,
            "department_name":departmentName,
            "user": token,
            "description":serviceInfo.descripcion,
            "category": serviceInfo.categorias.idcategoria
        }
        return service

    
    @classmethod
    def create_service(self,idcategoria,nombre,estado,tipo,precio,descripcion,foto,usuario):
        newService = Services(idcategoria,nombre,estado,tipo,precio,descripcion,foto,usuario)
        db.session.add(newService)
        db.session.commit()


    @classmethod
    def search_all_services_info(self,nombreServicio: str) -> list :
        services = []
        query = db.session.query(Services).filter(self.nombre.like('%{}%'.format(nombreServicio))).filter(self.estado == 1)
        result = db.session.execute(query)
        for serviceInfo in result.scalars():
            services.append(
                self.extract_service_info(serviceInfo)
            )
        db.session.commit()
        return services


    @classmethod
    def delete_service(self,serviceId:int):
        db.session.execute(delete(Services).filter(self.idservicio == serviceId))
        db.session.commit()
        return True
               

    @classmethod        
    def update_service_info(self,serviceId:int , categoryId:str , name:str , photo:str, type:str , price:int , description:str, status:int):
        db.session.execute(
            text("UPDATE servicios SET idcategoria = :categoryId, nombre = :name, foto = :photo, tipo= :type, precio = :price, descripcion= :description, estado = :status WHERE idservicio = :serviceId").bindparams(
                    categoryId = categoryId,
                    serviceId = serviceId,
                    name = name,
                    photo = photo,
                    type = type,
                    price = price,
                    description = description,
                    status = status,
                )
        )
        db.session.commit()
        return True

        
    @classmethod
    def get_services_from_user(self,userId:int):
        try:
            userInfo = Users.search_user_info(userId)
            services = []
            result = db.session.execute(db.session.query(Services).filter(self.usuario == userId))
            for serviceInfo in result.scalars():
                services.append(
                    self.extract_service_info(serviceInfo)
                )
            db.session.commit()
        except:
            raise Exception("Invalid Id")
        else:
            return services,userInfo


    
        