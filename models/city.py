from utils.db import db


class City(db.model):
    __tablename__ = 'ciudades'
    idciudad = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable= False)
    iddepartamento = db.Column(db.Integer, nullable=False)

    def __init__(self,nombre,iddepartamento):
        self.nombre=nombre
        self.iddepartamento=iddepartamento