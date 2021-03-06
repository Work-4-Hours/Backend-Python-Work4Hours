from utils.db import get_session, db
from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, select, insert, true, update, delete
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.expression import func
from models.Categories import Categories
from models.Statuses import Statuses
from models.Users import Users
from models.Appeals import Appeals
from models.City import City
from models.Visibility import Visibilty
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
    calificacion = db.Column(db.Float(), nullable= False)
    visibilidad = db.Column(db.Integer, ForeignKey('visibilidad.id'), nullable = False)
    estado_visibilidad = relationship(Visibilty, backref = backref('servicios'), uselist= True)


    def __init__(self, idcategoria, nombre, estado, tipo, precio, descripcion, foto, usuario):
        self.idcategoria=idcategoria
        self.nombre=nombre
        self.estado= 1
        self.tipo=tipo
        self.precio=precio
        self.descripcion=descripcion
        self.foto=foto
        self.usuario=usuario
        self.visibilidad = estado


    @classmethod
    def get_index_page_services(cls) -> list :
        with get_session() as session:
            services = []
            query = session.query(Services).filter(Services.calificacion > 3.9).filter(Services.estado == 1).filter(Services.visibilidad == 1).limit(20)
            result = session.execute(query)
            for serviceInfo in result.scalars():
                services.append(
                    cls.extract_service_info(serviceInfo)
                )
            session.commit()
            return services
    
    @classmethod
    def get_service_info(cls, serviceId: int):
        with get_session() as session:
            service = ""
            query = session.execute(session.query(Services).filter(Services.idservicio == serviceId))
            for serviceInfo in query.scalars():
                service = cls.extract_service_info(serviceInfo)
            user = Users.search_user_info(service['user'])
            session.commit()
            if(type(user) != dict):
                return None
            return {"serviceInfo": service, "serviceUser": user}

    @classmethod
    def extract_service_info(cls,serviceInfo):
        with get_session() as session: 
            service = {}
            departmentId,cityId,cityName,departmentName = City.get_city_info(serviceInfo.idservicio,serviceInfo.usuario)
            db_reports = session.execute(text("SELECT COUNT(id) FROM servicio_reportes WHERE idservicio = :serviceId").bindparams(
                serviceId = serviceInfo.idservicio
            ))
            reports = db_reports.scalars().one()
            db_qualification = session.execute(text("SELECT avg(c.calificacion) FROM calificacion c WHERE idservicio = :serviceId").bindparams(
                serviceId = serviceInfo.idservicio
            ))
            qualification = db_qualification.scalars().one()
            session.commit()
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
                "category": serviceInfo.categorias.idcategoria,
                "status": serviceInfo.estado,
                "reports": reports,
                "qualification":qualification,
                "visibility": serviceInfo.visibilidad
            }
            return service

    
    @classmethod
    def create_service(cls,idcategoria,nombre,estado,tipo,precio,descripcion,foto,usuario):
        with get_session() as session:
            newService = Services(idcategoria,nombre,estado,tipo,precio,descripcion,foto,usuario)
            session.add(newService)
            session.commit()


    @classmethod
    def search_all_services_info(cls,nombreServicio: str) -> list[dict] :
        with get_session() as session:
            services: list[dict] = []
            query = session.query(Services).filter(cls.nombre.like('%{}%'.format(nombreServicio))).filter(cls.estado == 1).filter(cls.visibilidad == 1)
            result = session.execute(query)
            for serviceInfo in result.scalars():
                services.append(
                    cls.extract_service_info(serviceInfo)
                )
            session.commit()
            return services


    @classmethod
    def delete_service(cls,serviceId:int):
        with get_session() as session:
            session.execute(text("DELETE FROM calificacion WHERE idservicio = :serviceId").bindparams(
                serviceId= serviceId
            ))
            session.execute(delete(Services).filter(cls.idservicio == serviceId))
            session.commit()
            return True


    @classmethod        
    def update_service_info(cls,serviceId:int , categoryId:str , name:str , photo:str, type:str , price:int , description:str, status:int):
        with get_session() as session:
            session.execute(
                text("UPDATE servicios SET idcategoria = :categoryId, nombre = :name, foto = :photo, tipo= :type, precio = :price, descripcion= :description, visibilidad = :status WHERE idservicio = :serviceId").bindparams(
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
            session.commit()
            return True

        
    @classmethod
    def get_services_from_user(cls, userId: int, isOwn: bool):
        with get_session() as session:
            try:
                userInfo = Users.search_user_info(userId)
                services = []
                if(isOwn):
                    result = session.execute(session.query(Services).filter(cls.usuario == userId))
                else:
                    result = session.execute(session.query(Services).filter(cls.usuario == userId).filter(cls.estado == 1).filter(cls.visibilidad == 1))
                for serviceInfo in result.scalars():
                    services.append(
                        cls.extract_service_info(serviceInfo)
                    )
                session.commit()
            except:
                return None,None
            else:
                if(type(userInfo) != dict):
                    return None,None
                return services,userInfo

    @classmethod
    def use_filters(cls, filter_param: str, filter_type: int, service_name: str) -> list[dict]:
        with get_session() as session:
            result: list[dict] = []
            sql = ""
            if(filter_type == 1):
                sql = session.query(Services).filter(Services.idcategoria == filter_param).filter(Services.visibilidad == 1).filter(Services.estado == 1).filter(Services.nombre.like('%{}%'.format(service_name)))
            elif(filter_type == 2):
                sql = session.query(Services).filter(Services.tipo == filter_param).filter(Services.visibilidad == 1).filter(Services.estado == 1).filter(Services.nombre.like('%{}%'.format(service_name)))
        
            for service in session.execute(sql).scalars():
                result.append(
                    cls.extract_service_info(service)
                )
            session.commit()
            if(not result):
                return None
            return result
    
    @classmethod
    def get_categories_services(cls, categoryId: int) -> list[dict] or None:
        with get_session() as session:
            services: list[dict] = []
            query = session.execute(session.query(Services).filter(Services.idcategoria == categoryId).limit(20))
            for service_info in query.scalars():
                services.append(cls.extract_service_info(service_info))
            session.commit()
            if(not services):
                return None
            return services
        





