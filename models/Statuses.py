from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref


class Statuses(db.Model):
    __tablename__ = 'status'
    statusid = db.Column(db.Integer, primary_key=True)
    statusname = db.Column(db.String(50), nullable=False)

    def __init__(self,statusName):
        self.statusName= statusName