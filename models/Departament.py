from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref

class Departament(db.Model):
    __tablename__ = 'departamentos'
    iddepartamento = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable= False)

    def __init__(self,nombre):
        self.nombre= nombre