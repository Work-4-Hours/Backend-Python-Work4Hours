from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
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