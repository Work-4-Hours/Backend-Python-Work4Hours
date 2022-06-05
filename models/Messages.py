from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref
from models.Hall import Hall
from models.Users import Users


class Messages(db.Model):
    __tablename__ = 'messages'
    messageid = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.Date, nullable=False)
    hallid = db.Column(db.Integer, ForeignKey('hall.hallid'),nullable= False)
    hall = relationship(Hall, backref=backref('messages', uselist=True))
    userid = db.Column(db.Integer, ForeignKey('user.userid'), nullable=False)
    users = relationship(Users, backref=backref('messages', uselist=True))

    def __init__(self,message,userId,date,hallId):
        self.message = message
        self.date = date
        self.hallid = hallId
        self.userid = userId