from utils.db import db


class Services(db.model):
    __tablename__ = 'servicios'
    idservicio = db.Column(db.Integer, primary_key=True)
    idcategoria = db.Column(db.String(3), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(1), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String(2000), nullable=False)
    foto = db.Column(db.String(500), nullable=False)
    usuario = db.Column(db.Integer, nullable=False)


    def __init__(self, idcategoria, nombre, estado, tipo, precio, descripción, foto, usuario):
        self.idcategoria=idcategoria
        self.nombre=nombre
        self.estado=estado
        self.tipo=tipo
        self.precio=precio
        self.descripcion=descripción
        self.foto=foto
        self.usuario=usuario