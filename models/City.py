from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship, backref
from models.Departament import Departament

class City(db.Model):
    __tablename__ = 'ciudades'
    idciudad = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable= False)
    iddepartamento = db.Column(db.Integer, ForeignKey('departamentos.iddepartamento'),nullable=False)
    departamentos = relationship(Departament, backref=backref('departamentos', uselist=True))


    def __init__(self,nombre,iddepartamento):
        self.nombre=nombre
        self.iddepartamento=iddepartamento


    @classmethod
    def get_city_info(self,serviceId:Integer,userId:Integer):
        departmentId = ""
        cityId = ""
        cityName = ""
        cityInfoQuery = text("""SELECT d.nombre, c.iddepartamento, c.idciudad, c.nombre FROM ciudades c INNER JOIN departamentos d on d.iddepartamento = c.iddepartamento WHERE c.idciudad = (SELECT u.ciudad FROM usuarios u where u.idusuario = :userId)""").bindparams(
            userId = userId
        )
        cityInfo = db.session.execute(cityInfoQuery)
        for city in cityInfo:
            departmentName = city[0]
            departmentId = city[1]
            cityId = city[2]
            cityName = city[3]
        db.session.commit()
        return departmentId,cityId,cityName,departmentName


    @classmethod
    def get_all_cities_from_department(self,departmentId:Integer):
        cities = []
        citiesQuery = db.session.query(City).filter(self.iddepartamento == departmentId)
        citiesResult = db.session.execute(citiesQuery)
        for city in citiesResult.scalars():
            cities.append(
                {
                    "name":city.nombre,
                    "id":city.idciudad
                }
            )
        db.session.commit()
        return cities