from utils.db import db


class Rol(db.model):
    __tablename__ = 'roles'
    idrol = db.Column(db.Integer, primary_key=True)
    nombrerol = db.Column(db.String(15), nullable=False)


    def __init__(self,nombrerol):
        self.nombrerol=nombrerol