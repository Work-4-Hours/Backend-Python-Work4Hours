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
                user = write_token({"userId": service_info.__dict__["user"]})
                del service_info.__dict__["user"]
                services.append(IndexService(**service_info.__dict__,user=user).dict())
            if(not services):
                return None
            return services

    # @classmethod
    # def without_keys(cls, d: dict, keys: dict):
    #     return {x: dict[x] for x in d if x not in keys}