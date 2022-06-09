from schemas import City as CitySchema
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
        cities :list[CitySchema]
        with get_session() as session:
            cities_info_query = session.execute(text("SELECT * FROM city WHERE departmentid = :departmentId").bindparams(
                departmentId = departmentId
            ))
            for city in cities_info_query.scalars():
                cities.append(**city.__dict__)
            if(not cities):
                return None
            return cities


