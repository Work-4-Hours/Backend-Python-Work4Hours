from schemas import Department as DepartmentSchema
from models.Departament import Departament
from utils.db import get_session
from sqlalchemy.sql import text

class Department:
    
    @classmethod
    def get_all_departments(cls) -> list[DepartmentSchema]:
        with get_session() as session:
            departments_query = session.execute(session.query(Departament))
            deparments : list[DepartmentSchema] = [DepartmentSchema(**department.__dict__).dict() for department in departments_query.scalars()]
            session.commit()
            if(not deparments):
                return None
            return deparments