from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref
from models.Users import Users
from models.Report import Report


class User_reports(db.Model):
    __tablename__ = 'usuario_reportes'
    id = db.Column(db.Integer, primary_key=True)
    idusuario = db.Column(db.Integer, ForeignKey('usuarios.idusuario'),nullable=False)
    usuarios = relationship(Users, backref=backref('usuario_reportes', uselist=True))
    idreporte = db.Column(db.Integer, ForeignKey('reportes.idreporte'),nullable=False)
    reportes = relationship(Report, backref=backref('usuario_reportes',uselist=True))


    def __init__(self,idusuario,idreporte):
        self.idusuario=idusuario
        self.idreporte=idreporte