from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref


class Categories(db.Model):
    __tablename__='category'
    categoryid = db.Column(db.String, primary_key=True)
    namecateg = db.Column(db.String(30), nullable=True)

    def __init__(self,nameCateg):
        self.namecateg=nameCateg