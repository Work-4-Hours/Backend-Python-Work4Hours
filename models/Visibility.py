from utils.db import db
from sqlalchemy import ForeignKey, Integer, String, Column

class Visibilty(db.Model):
    __tablename__ = 'visibilidad'
    id = db.Column(db.Integer, primary_key = True)
    nombre_estado = db.Column(db.String(30), nullable = False)

    def __init__(self, nombre_estado: str) -> None:
        self.nombre_estado = nombre_estado