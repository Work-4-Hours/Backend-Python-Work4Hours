from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref


class Report(db.Model):
    __tablename__ = 'report'
    reportid = db.Column(db.Integer, primary_key=True)
    reportName = db.Column(db.String(14), nullable=False)

    def __init__(self,reportName):
        self.reportName=reportName