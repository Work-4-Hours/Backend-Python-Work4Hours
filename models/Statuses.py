from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref


class Statuses(db.Model):
    __tablename__ = 'estados'
    id = db.Column(db.Integer, primary_key=True)
    nombre_estado = db.Column(db.String(50), nullable=False)

    def __init__(self,nombre_estado):
        self.nombre_estado=nombre_estado