from utils.db import db


class Hall(db.model):
    __tablename__ = 'sala'
    idsala = db.Column(db.Integer, primary_key=True)
    fechainicio = db.Column(db.Date, nullable= False)
    fechafin = db.Column(db.Date, nullable= False)
    horainicio = db.Column(db.String(5), nullable= False)
    horafin = db.Column(db.String(5), nullable=False)


    def __init__(self,fechainicio,fechafin,horainicio,horafin):
        self.fechainicio=fechainicio
        self.fechafin=fechafin
        self.horainicio=horainicio
        self.horafin=horafin