from cgitb import text
from csv import QUOTE_ALL
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

    @classmethod
    def add_qualification(cls, qualification: float, userId: int, serviceId: int) -> None:
        prevQualification = db.session.execute(db.session.query(Qualification).filter(cls.idservicio == serviceId).filter(cls.idusuario == userId))
        isQualified = prevQualification.scalars().first()
        if (not isQualified):
            newQualification = Qualification(qualification,userId,serviceId)
            db.session.add(newQualification)
        else:
            db.session.execute(text("UPDATE calificacion SET calificacion = :qualification WHERE idusuario = :userId and idservicio = :serviceId").bindparams(
                userId = userId,
                qualification = qualification,
                serviceId = serviceId
            ))
        db.session.commit()
        

    @classmethod
    def get_qualifications_average(self, serviceId : int) -> dict:
        averageQualification = {}
        query = db.session.query(func.avg(self.calificacion)).filter(self.idservicio == serviceId)
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

    @classmethod
    def get_user_qualification_avg(self,userId:int) -> dict:
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

    


        