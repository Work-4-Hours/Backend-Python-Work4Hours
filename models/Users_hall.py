from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref
from models.Hall import Hall
from models.Users import Users


class Users_hall(db.Model):
    __tablename__ = 'user_hall'
    user_hallid = db.Column(db.Integer, primary_key=True)
    hallid = db.Column(db.Integer, ForeignKey('sala.idsala'),nullable=False)
    hall = relationship(Hall, backref=backref('sala_usuario', uselist=True))
    userid = db.Column(db.Integer, ForeignKey('usuarios.idusuario'),nullable=False)
    users = relationship(Users, backref=backref('sala_usuario', uselist=True))

    def __init__(self, hallId, userId):
        self.hallid = hallId
        self.userid = userId