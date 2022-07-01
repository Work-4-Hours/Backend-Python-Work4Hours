from utils.db import db, get_session
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.functions import func
from models.Report import Report
from models.Services import Services



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

    @classmethod
    def get_service_reports(cls, serviceId: int) -> int:
        with get_session() as session:
            db_reports = session.execute(session.query(func.count(cls.id)).filter(cls.idservicio == serviceId))
            reports = db_reports.scalars().one()
            session.commit()
            return reports