from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref


class Rol(db.Model):
    __tablename__ = 'role'
    roleid = db.Column(db.Integer, primary_key=True)
    roleName = db.Column(db.String(15), nullable=False)

    def __init__(self,roleName):
        self.roleName= roleName