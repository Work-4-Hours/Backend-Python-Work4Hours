import this
from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref
from models.City import City

class Appeals(db.Model):
    __tablename__ = 'apelaciones'
    idapelacion = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(500), nullable= False)
    idservicio = db.Column(db.Integer, nullable= False)

    def __init__(self,description,serviceid):
        self.descripcion = description
        self.idservicio = serviceid