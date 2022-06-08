from schemas import City
from models.City import City
from utils.db import get_session
from sqlalchemy.sql import text

class CityService:

    @classmethod
    def get_city_info(serviceId: int, userId: int ):
        with get_session() as session:
            city_info_query = session.execute(text("SELECT * FROM city c WHERE c.cityid = (SELECT u.city FROM user u WHERE u.userId = :userId)").bindparams(
                userId = userId
            ))