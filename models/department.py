from utils.db import db


class Departament(db.model):
    __tablename__ = 'departamentos'
    iddepartamento = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable= False)


    def __init__(self,nombre):
        self.nombre= nombre