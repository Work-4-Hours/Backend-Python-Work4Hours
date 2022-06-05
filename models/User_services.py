from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref
from models.Users import Users
from models.Report import Report


class User_services(db.Model):
    __tablename__ = 'report_users'
    report_usersid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, ForeignKey('usuarios.idusuario'),nullable=False)
    users = relationship(Users, backref=backref('usuario_reportes', uselist=True))
    reportid = db.Column(db.Integer, ForeignKey('reportes.idreporte'),nullable=False)
    reports = relationship(Report, backref=backref('usuario_reportes',uselist=True))


    def __init__(self,userId,reportId):
        self.userid=userId
        self.reportid=reportId