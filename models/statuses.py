from utils.db import db

class Statuses(db.model):
    __tablename__ = 'estados'
    id = db.Column(db.Integer, primary_key=True)
    nombre_reporte = db.Column(db.String(50), nullable=False)

    def __init__(self,nombre_reporte):
        self.nombre_reporte=nombre_reporte
        