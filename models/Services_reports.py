from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref



class Services_reports(db.Model):
    __tablename__ = 'servicio_reportes'
    id = db.Column(db.Integer, primary_key=True)
    idreporte = db.Column(db.Integer,ForeignKey('reportes.idreporte'), nullable=False)
    reportes = relationship(Report, backref=backref('servicio_reportes'), uselist=True)
    idservicio = db.Column(db.Integer, ForeignKey('servicios.idservicio'),nullable=False)
    servicios = relationship(Services, backref=backref('servicio_reportes'), uselist=True)


    def __init__(self, idreporte, idservicio):
        self.idreporte= idreporte
        self.idservicio= idservicio