from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref
from models.Report import Report
from models.Services import Services



class Services_reports(db.Model):
    __tablename__ = 'report_services'
    id = db.Column(db.Integer, primary_key=True)
    reportid = db.Column(db.Integer,ForeignKey('report.reportid'), nullable=False)
    reports = relationship(Report, backref=backref('report_services'), uselist=True)
    serviceid = db.Column(db.Integer, ForeignKey('services.serviceId'),nullable=False)
    services = relationship(Services, backref=backref('reports_services'), uselist=True)


    def __init__(self, reportId, serviceId):
        self.reportid= reportId
        self.serviceid= serviceId