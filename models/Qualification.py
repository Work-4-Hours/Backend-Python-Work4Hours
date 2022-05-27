from cgitb import text
from utils.db import db
from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, select, insert, update
from sqlalchemy.sql import text
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


    def getQualificationsAverage(serviceId : int) -> dict:
        averageQualification = {}
        query = db.session.query(func.avg(Qualification.calificacion)).filter(Qualification.idservicio == serviceId)
        result = db.session.execute(query)
        for average in result.scalars():
            averageQualification = {
                "qualification" : average
            } 
        db.session.execute(text("UPDATE servicios SET calificacion = :average WHERE idservicio = :serviceId").bindparams(
        average = averageQualification['qualification'],
        serviceId = serviceId
        ))
        db.session.commit()
        return averageQualification


    def addQualification(qualification:float,userId:int,serviceId:int) -> None:
        newQualification = Qualification(qualification,userId,serviceId)
        db.session.add(newQualification)
        db.session.commit()


    def getUserQualificationAvg(userId:int) -> dict:
        avgQualification = {}
        result = db.session.execute(text("SELECT AVG(s.calificacion) FROM servicios s RIGHT JOIN usuarios u ON u.idusuario = s.usuario WHERE u.idusuario = :userId").bindparams(
            userId = userId
        ))
        for average in result.scalars():
            avgQualification = {
                "qualification" : average
            }
        db.session.commit()
        return avgQualification


        