from models.Services import Services
from utils.db import db
from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, select, insert
from sqlalchemy.orm import relationship, backref


class Qualification(db.Model):
    __tablename__ = 'calificacion'
    idcalificacion = db.Column(db.Integer, primary_key=True)
    calificacion = db.Column(db.Integer, nullable=False)
    idusuario = db.Column(db.Integer, nullable=False)
    idservicio = db.Column(db.Integer, ForeignKey('servicios.idservicio'), nullable=False)
    servicio = relationship(Services, backref=backref('calificacion', uselist=True))

    def __init__(self, calificacion, idusuario, idservicio):
        self.calificacion = calificacion
        self.idusuario = idusuario
        self.idservicio = idservicio
        