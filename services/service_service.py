from schemas import IndexService, ServiceModel
from models.Services import Services
from utils.db import get_session

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
            services_query = session.execute(session.query(Services).filter(Services.qualification > 3.9).filter(Services.status == 1))
            services: list[IndexService] = [IndexService(**service_info.__dict__).dict() for service_info in services_query.scalars()]
            if(not services):
                return None
            return services