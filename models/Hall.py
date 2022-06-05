from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref
from models.Services import Services


class Hall(db.Model):
    __tablename__ = 'hall'
    hallid = db.Column(db.Integer, primary_key=True)
    startdate = db.Column(db.Date, nullable= False)
    enddate = db.Column(db.Date, nullable= False)
    starthour = db.Column(db.String(5), nullable= False)
    endhour = db.Column(db.String(5), nullable=False)
    serviceid = db.Column(db.Integer, ForeignKey('service.serviceid'), nullable=False)
    services = relationship(Services, backref = backref('hall', uselist = True))


    def __init__(self,startDate,endDate,startHour,endHour):
        self.startdate=startDate
        self.enddate=endDate
        self.starthour=startHour
        self.endhour=endHour