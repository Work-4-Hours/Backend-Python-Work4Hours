from utils.db import db
from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, select, insert, update
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func
from models.Services import Services


class Qualification(db.Model):
    __tablename__ = 'calificacion'
    idcalificacion = db.Column(db.Integer, primary_key=True)
    calificacion = db.Column(db.Integer, nullable=False)
    idusuario = db.Column(db.Integer, nullable=False)
    idservicio = db.Column(db.Integer, ForeignKey('servicios.idservicio'), nullable=False)
    servicio = relationship(Services, backref=backref('servicio', uselist=True))

    def __init__(self, calificacion, idusuario, idservicio):
        self.calificacion = calificacion
        self.idusuario = idusuario
        self.idservicio = idservicio

    def getQualificationsAverage(serviceId):
        average = {}
        query = db.session.query(func.avg(Qualification.calificacion)).filter(Qualification.idservicio == serviceId)
        result = db.session.execute(query)
        for average in result.scalars():
            average = {
                "average": average,
            }
        db.session.commit()
        return average

    def addQualification(self):
        query = update({'calificacion': Services.calificacion})
        db.session.execute(query)
        db.session.commit()

        