from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref
from models.Services import Services


class Hall(db.Model):
    __tablename__ = 'sala'
    idsala = db.Column(db.Integer, primary_key=True)
    fechainicio = db.Column(db.Date, nullable= False)
    fechafin = db.Column(db.Date, nullable= False)
    horainicio = db.Column(db.String(5), nullable= False)
    horafin = db.Column(db.String(5), nullable=False)
    idservicio = db.Column(db.Integer, ForeignKey('servicios.idservicios'), nullable=False)
    servicios = relationship(Services, backref = backref('sala', uselist = True))


    def __init__(self,fechainicio,fechafin,horainicio,horafin):
        self.fechainicio=fechainicio
        self.fechafin=fechafin
        self.horainicio=horainicio
        self.horafin=horafin