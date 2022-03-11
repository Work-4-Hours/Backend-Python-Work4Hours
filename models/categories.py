from utils.db import db


class Categories(db.model):
    __tablename__="categorias"
    idcategoria = db.Column(db.String, primary_key=True)
    nombrecateg = db.Column(db.String(30), nullable=True)


    def __init__(self,nombrecateg):
        self.nombrecateg=nombrecateg