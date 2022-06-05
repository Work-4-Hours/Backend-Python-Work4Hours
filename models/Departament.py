from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref

class Departament(db.Model):
    __tablename__ = 'departament'
    departamentid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable= False)

    def __init__(self,name):
        self.name= name

    
    # def get_department_info(self,departmentId:Integer):
    #     departmentName = ""
    #     departmentQuery = db.session.query(self.nombre).filter(self.iddepartamento == departmentId)
    #     departmentInfo = db.session.execute(departmentQuery)
    #     for department in departmentInfo.scalars():
    #         departmentName = department
    #     db.session.commit()
    #     return departmentName

    # def get_all_departments():
    #     departments = []
    #     departmentsQuery = db.session.query(Departament)
    #     departmentsInfo = db.session.execute(departmentsQuery)
    #     for department in departmentsInfo.scalars():
    #         departments.append(
    #             {
    #                 "id":department.iddepartamento,
    #                 "name":department.nombre
    #             }
    #         )
    #     db.session.commit()
    #     return departments
