from utils.db import db

class Users_hall(db.model):
    idsalausuario = db.Column(db.Integer, primary_key=True)
    idsala = db.Column(db.Integer, nullable=False)
    idusuario = db.Column(db.Integer, nullable=False)

    def __init__(self, idsala, idusuario):
        self.idsala=idsala
        self.idusuario=idusuario