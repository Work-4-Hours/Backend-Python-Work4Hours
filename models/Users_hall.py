from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref


class Users_hall(db.Model):
    __tablename__ = 'sala_usuario'
    idsalausuario = db.Column(db.Integer, primary_key=True)
    idsala = db.Column(db.Integer, ForeignKey('sala.idsala'),nullable=False)
    sala = relationship(Hall, backref=backref('sala_usuario', uselist=True))
    idusuario = db.Column(db.Integer, ForeignKey('usuarios.idusuario'),nullable=False)
    usuarios = relationship(Users, backref=backref('sala_usuario', uselist=True))

    def __init__(self, idsala, idusuario):
        self.idsala=idsala
        self.idusuario=idusuario