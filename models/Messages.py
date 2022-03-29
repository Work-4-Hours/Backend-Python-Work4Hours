from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref


class Messages(db.Model):
    __tablename__ = 'mensajes'
    idmensaje = db.Column(db.Integer, primary_key=True)
    mensaje = db.Column(db.String(1000), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    idsala = db.Column(db.Integer, ForeignKey('sala.idsala'),nullable= False)
    sala = relationship(Hall, backref=backref('mensajes', uselist=True))
    idusuario = db.Column(db.Integer, ForeignKey('usuarios.idusuario'), nullable=False)
    usuarios = relationship(Users, backref=backref('mensajes', uselist=True))

    def __init__(self, mensaje, fecha, idsala, idusuario):
        self.mensaje = mensaje
        self.fecha = fecha
        self.idsala = idsala
        self.idusuario = idusuario