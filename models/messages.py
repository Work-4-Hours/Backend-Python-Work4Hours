from utils.db import db

class Messages(db.model):
    __tablename__ = 'mensajes'
    idmensaje = db.Column(db.Integer, primary_key=True)
    mensaje = db.Column(db.String(1000), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    idsala = db.Column(db.Integer, nullable= False)
    idusuario = db.Column(db.Integer, nullable=False)

    def __init__(self, mensaje, fecha, idsala, idusuario):
        self.mensaje = mensaje
        self.fecha = fecha
        self.idsala = idsala
        self.idusuario = idusuario