from cgitb import text
from utils.db import db
from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, select, insert, update
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func
from models.Services import Services


class Qualification(db.Model):
    __tablename__ = 'qualification'
    qualificationid = db.Column(db.Integer, primary_key=True)
    qualification = db.Column(db.Integer, nullable=False)
    userid = db.Column(db.Integer, nullable=False)
    serviceid = db.Column(db.Integer, ForeignKey('service.serviceid'), nullable=False)
    service = relationship(Services, backref=backref('service', uselist=True))


    def __init__(self, qualification, userid, serviceid):
        self.qualification = qualification
        self.userid = userid
        self.serviceid = serviceid


    # def add_qualification(qualification:float,userId:int,serviceId:int) -> None:
    #     newQualification = Qualification(qualification,userId,serviceId)
    #     db.session.add(newQualification)
    #     db.session.commit()


    # def get_qualifications_average(self,serviceId : int) -> dict:
    #     averageQualification = {}
    #     query = db.session.query(func.avg(self.calificacion)).filter(self.idservicio == serviceId)
    #     result = db.session.execute(query)
    #     for average in result.scalars():
    #         averageQualification = {
    #             "qualification" : average
    #         } 
    #     db.session.execute(text("UPDATE servicios SET calificacion = :average WHERE idservicio = :serviceId").bindparams(
    #     average = averageQualification['qualification'],
    #     serviceId = serviceId
    #     ))
    #     db.session.commit()
    #     return averageQualification


    # def get_user_qualification_avg(userId:int) -> dict:
    #     avgQualification = {}
    #     result = db.session.execute(text("SELECT AVG(s.calificacion) FROM servicios s RIGHT JOIN usuarios u ON u.idusuario = s.usuario WHERE u.idusuario = :userId").bindparams(
    #         userId = userId
    #     ))
    #     for average in result.scalars():
    #         avgQualification = {
    #             "qualification" : average
    #         }
    #     db.session.commit()
    #     return avgQualification

    


        