from utils.db import db, get_session
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref

class Departament(db.Model):
    __tablename__ = 'departamentos'
    iddepartamento = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable= False)

    def __init__(self,nombre):
        self.nombre= nombre

    
    @classmethod
    def get_department_info(cls,departmentId:Integer):
        with get_session() as session:
            departmentName = ""
            departmentQuery = session.query(Departament.nombre).filter(Departament.iddepartamento == departmentId)
            departmentInfo = session.execute(departmentQuery)
            for department in departmentInfo.scalars():
                departmentName = department
            session.commit()
            return departmentName


    @classmethod
    def get_all_departments(cls):
        with get_session() as session:
            departments = []
            departmentsQuery = session.query(Departament)
            departmentsInfo = session.execute(departmentsQuery)
            for department in departmentsInfo.scalars():
                departments.append(
                    {
                        "id":department.iddepartamento,
                        "name":department.nombre
                    }
                )
            session.commit()
            return departments
