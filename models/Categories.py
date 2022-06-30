from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, select
from sqlalchemy.orm import relationship, backref


class Categories(db.Model):
    __tablename__='categorias'
    idcategoria = db.Column(db.String, primary_key=True)
    nombrecateg = db.Column(db.String(30), nullable=True)

    def __init__(self,nombrecateg):
        self.nombrecateg=nombrecateg

    @classmethod
    def get_categories(cls) -> list[dict]:
        categories: list[dict] = []
        query = db.session.execute(db.session.query(Categories))
        for category in query.scalars():
            categories.append({
                "categoryName": category.nombrecateg,
                "categId": category.idcategoria
            }
            )
        return categories