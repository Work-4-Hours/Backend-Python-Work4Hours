from utils.db import db


class User_services(db.model):
    __tablename__ = 'usuario_reportes'
    id = db.Column(db.Integer, primary_key=True)
    idusuario = db.Column(db.Integer, nullable=False)
    idreporte = db.Column(db.Integer, nullable=False)


    def __init__(self,idusuario,idreporte):
        self.idusuario=idusuario
        self.idreporte=idreporte