import this
from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref
from models.City import City

class Appeals(db.Model):
    __tablename__ = 'appeal'
    appealid = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable= False)
    serviceid = db.Column(db.Integer, nullable= False)

    def __init__(self,description,serviceId):
        self.description = description
        self.serviceid = serviceId


    # def createAppeal(email:str, description:str, serviceId:int) --> bool :
        