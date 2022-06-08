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
    __tablename__ = 'service'
    serviceid = db.Column(db.Integer, primary_key=True)
    categoryid = db.Column(db.String(3), ForeignKey('category.categoryid'),nullable=False)
    categories = relationship(Categories, backref=backref('service', uselist=True))
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Integer, ForeignKey('status.statusid'),nullable=False)
    statuses = relationship(Statuses, backref=backref('service', uselist=True))
    type = db.Column(db.String(1), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    picture = db.Column(db.String(500), nullable=False)
    user = db.Column(db.Integer, ForeignKey('user.userId'),nullable=False)
    users = relationship(Users, backref=backref('service', uselist=True))
    appeal = db.Column(db.Integer,ForeignKey('appeal.appealid'),nullable=True)
    appeals = relationship(Appeals, backref= backref('service'),uselist= True)
    qualification = db.Column(db.Float(), nullable=False)


    def __init__(self, categoryId, name, status, type, price, description, picture, userId):
        self.idcategoria=categoryId
        self.name= name
        self.status=status
        self.type=type
        self.price=price
        self.description=description
        self.picture=picture
        self.userId=userId


    # def get_index_page_services(self) -> list :
    #     services = []
    #     query = db.session.query(Services).filter(self.calificacion >= 4.0).filter(self.estado == 1).limit(20)
    #     result = db.session.execute(query)
    #     for serviceInfo in result.scalars():
    #         services.append(
    #             self.extract_service_info(serviceInfo)
    #         )
    #     db.session.commit()
    #     return services

    
    # def get_service_info(self,serviceId):
    #     service = ""
    #     query = db.session.execute(db.session.query(Services).filter(self.idservicio == serviceId))
    #     for serviceInfo in query.scalars():
    #         service = self.extract_service_info(serviceInfo)
    #     user = Users.search_user_info(service['user'])
    #     db.session.commit()
    #     return {"serviceInfo":service,"serviceUser":user}


    # def extract_service_info(serviceInfo):
    #     service = {}
    #     departmentId,cityId,cityName = City.get_city_info(serviceInfo.idservicio,serviceInfo.usuario)
    #     departmentName = Departament.get_department_info(departmentId)
    #     token = str(write_token({"userId" : serviceInfo.usuario})).split("'")[1]
    #     service = {
    #         "name": serviceInfo.nombre,
    #         "id" : serviceInfo.idservicio,
    #         "price": serviceInfo.precio,
    #         "photo": serviceInfo.foto,
    #         "city_code": cityId,
    #         "city_name": cityName,
    #         "department_code":departmentId,
    #         "department_name":departmentName,
    #         "user": token,
    #         "description":serviceInfo.descripcion,
    #         "category": serviceInfo.categorias.idcategoria
    #     }
    #     return service

    
    # def create_service(idcategoria,nombre,estado,tipo,precio,descripcion,foto,usuario):
    #     newService = Services(idcategoria,nombre,estado,tipo,precio,descripcion,foto,usuario)
    #     db.session.add(newService)
    #     db.session.commit()


    # def search_all_services_info(self,nombreServicio: str) -> list :
    #     services = []
    #     query = db.session.query(Services).filter(self.nombre.like('%{}%'.format(nombreServicio))).filter(self.estado == 1)
    #     result = db.session.execute(query)
    #     for serviceInfo in result.scalars():
    #         services.append(
    #             self.extract_service_info(serviceInfo)
    #         )
    #     db.session.commit()
    #     return services


    # def delete_service(self,serviceId:int):
    #     db.session.execute(delete(Services).filter(self.idservicio == serviceId))
    #     db.session.commit()
    #     return True
               
        
    # def update_service_info(serviceId:int , categoryId:str , name:str , photo:str, type:str , price:int , description:str, status:int):
    #     db.session.execute(
    #         text("UPDATE servicios SET idcategoria = :categoryId, nombre = :name, foto = :photo, tipo= :type, precio = :price, descripcion= :description, estado = :status WHERE idservicio = :serviceId").bindparams(
    #                 categoryId = categoryId,
    #                 serviceId = serviceId,
    #                 name = name,
    #                 photo = photo,
    #                 type = type,
    #                 price = price,
    #                 description = description,
    #                 status = status,
    #             )
    #     )
    #     db.session.commit()
    #     return True

        
    # def get_services_from_user(self,userId:int):
    #     try:
    #         userInfo = Users.search_user_info(userId)
    #         services = []
    #         result = db.session.execute(db.session.query(Services).filter(self.usuario == userId))
    #         for serviceInfo in result.scalars():
    #             services.append(
    #                 self.extract_service_info(serviceInfo)
    #             )
    #         db.session.commit()
    #     except:
    #         raise Exception("Invalid Id")
    #     else:
    #         return services,userInfo


    
        