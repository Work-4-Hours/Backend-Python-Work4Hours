from utils.db import db, get_session
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
        with get_session() as session:
            prevQualification = session.execute(session.query(Qualification).filter(cls.idservicio == serviceId).filter(cls.idusuario == userId))
            isQualified = prevQualification.scalars().first()
            if (not isQualified):
                newQualification = Qualification(qualification,userId,serviceId)
                session.add(newQualification)
            else:
                session.execute(text("UPDATE calificacion SET calificacion = :qualification WHERE idusuario = :userId and idservicio = :serviceId").bindparams(
                    userId = userId,
                    qualification = qualification,
                    serviceId = serviceId
                ))
            session.commit()
        

    @classmethod
    def get_qualifications_average(self, serviceId : int) -> dict:
        with get_session() as session:
            averageQualification = {}
            query = session.query(func.avg(self.calificacion)).filter(self.idservicio == serviceId)
            result = session.execute(query)
            for average in result.scalars():
                averageQualification = {
                    "qualification" : average
                } 
            session.execute(text("UPDATE servicios SET calificacion = :average WHERE idservicio = :serviceId").bindparams(
            average = averageQualification['qualification'],
            serviceId = serviceId
            ))
            session.commit()
            return averageQualification

    @classmethod
    def get_user_qualification_avg(self,userId:int) -> dict:
        with get_session() as session:
            avgQualification = {}
            result = session.execute(text("SELECT AVG(s.calificacion) FROM servicios s RIGHT JOIN usuarios u ON u.idusuario = s.usuario WHERE u.idusuario = :userId").bindparams(
                userId = userId
            ))
            for average in result.scalars():
                avgQualification = {
                    "qualification" : average
                }
            session.commit()
            return avgQualification

    


        