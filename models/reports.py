from utils.db import db


class Report(db.model):
    __tablename__ = 'reportes'
    idreporte = db.Column(db.Integer, primary_key=True)
    nombrereporte = db.Column(db.String(14), nullable=False)

    def __init__(self,nombrereporte):
        self.nombrereporte=nombrereporte