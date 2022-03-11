from utils.db import db


class Services_reports(db.model):
    __tablename__ = 'servicio_reportes'
    id = db.Column(db.Integer, primary_key=True)
    idreporte = db.Column(db.Integer, nullable=False)
    idservicio = db.Column(db.Integer, nullable=False)

    def __init__(self, idreporte, idservicio):
        self.idreporte= idreporte
        self.idservicio= idservicio