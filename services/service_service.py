from sqlalchemy.sql import text
from schemas import IndexService, ServiceModel
from models.Services import Services
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
    def delete_service(cls, serviceid: int) -> bool or None:
        with get_session() as session:
            pass