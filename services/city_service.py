from schemas import City as CitySchema
from models.City import City as CityModel
from utils.db import get_session
from sqlalchemy.sql import text

class CityService:

    @classmethod
    def get_city_info(cls, userId: int ) -> CitySchema or None:
        with get_session() as session:
            city_info_query = session.execute(text("SELECT * FROM city c WHERE c.cityid = (SELECT u.city FROM user u WHERE u.userId = :userId)").bindparams(
                userId = userId
            ))
            city_info_result = city_info_query.scalars().one()
            if(not city_info_result):
                return None
            city = CitySchema(**city_info_result.__dict__)
            return city


    @classmethod
    def get_all_cities_from_department(cls, departmentId: int) ->  list[CitySchema] or None:
        with get_session() as session:
            cities_info_query = session.execute(session.query(CityModel).filter(CityModel.departmentid == departmentId))
            cities: list[CitySchema] = [CitySchema(**city.__dict__).dict() for city in cities_info_query.scalars()]
            if(not cities):
                return None
            return cities


