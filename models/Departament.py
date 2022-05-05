from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref

class Departament(db.Model):
    __tablename__ = 'departamentos'
    iddepartamento = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable= False)

    def __init__(self,nombre):
        self.nombre= nombre

    
    def getDepartmentInfo(departmentId:Integer):
        departmentName = ""
        departmentQuery = db.session.query(Departament.nombre).filter(Departament.iddepartamento == departmentId)
        departmentInfo = db.session.execute(departmentQuery)
        for department in departmentInfo.scalars():
            departmentName = department
        return departmentName

    def getAllDepartments():
        departments = []
        departmentsQuery = db.session.query(Departament).all()
        departmentsInfo = db.session.execute(departmentsQuery)
        for department in departmentsInfo.scalars():
            departments.append(
                {
                    "departmentId":department.iddepartamento,
                    "departmentName":department.nombre
                }
            )
        return departments
