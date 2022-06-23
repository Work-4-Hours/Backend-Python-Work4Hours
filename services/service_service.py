from sqlalchemy.sql import text
from schemas import IndexService, ServiceModel, UserModel
from models.Services import Services
from schemas.user_schema import UserProfile
from utils.db import get_session
from jwt_Functions import write_token


class ServicesService:

    @classmethod
    def create_service(cls, serviceInfo: ServiceModel) -> ServiceModel:
        with get_session() as session:
            new_service = Services(**serviceInfo)
            session.add(new_service)
            session.commit()
        return new_service


    @classmethod
    def get_index_services(cls) -> list[IndexService] or None:
        with get_session() as session:
            services: list[IndexService] = []
            services_query = session.execute(session.query(Services).filter(Services.qualification > 3.9).filter(Services.status == 1))
            for service_info in services_query.scalars():
                service_info.__dict__["user"] = write_token({"userId": service_info.__dict__["user"]})
                services.append(IndexService(**service_info.__dict__).dict())
            if(not services):
                return None
            session.commit()
            return services


    @classmethod
    def search_services(cls, serviceName: str) -> list[IndexService] or None:
        with get_session() as session:
            services: list[IndexService] = []
            services_query = session.execute(session.query(Services).filter(Services.name.like('{}%'.format(serviceName))).filter(Services.status == 1))
            for service_info in services_query.scalars():
                service_info.__dict__["user"] = write_token({"userId": service_info.__dict__["user"]})
                services.append(IndexService(**service_info.__dict__).dict())
            if(not services):
                return None
            session.commit()
            return services


    @classmethod
    def update_service(cls, service_info: ServiceModel) -> ServiceModel or None: 
        with get_session() as session:
            try:
                session.execute(text("UPDATE servicios SET idcategoria = :categoryId, nombre = :name, foto = :photo, tipo= :type, precio = :price, descripcion= :description, estado = :status WHERE idservicio = :serviceId").bindparams(
                    categoryId = service_info.categoryid,
                    serviceId = service_info.serviceid,
                    name = service_info.name,
                    photo = service_info.picture,
                    type = service_info.type,
                    price = service_info.price,
                    description = service_info.description,
                    status = service_info.status,
                    )
                )
                session.commit()
            except:
                return None
            else:
                return service_info

    
    @classmethod
    def get_service_info(cls, service_id: int) -> ServiceModel or None:
        with get_session() as session:
            service_query = session.execute(session.query(Services).filter(Services.serviceid == service_id))
            service_data = service_query.scalars().one()
            user_query = session.execute(text("SELECT u.userId, u.name, u.lastName, u.phoneNumber, u.email, u.picture, u.color, u.status from user u where userId = :userId").bindparams(
                userId = service_data.user
            ))
            user_data = user_query.one()
            service_info = ServiceModel(**service_data.__dict__,userInfo= UserProfile())
            if (not service_info):
                return None
            else:
                return service_info
            


    


