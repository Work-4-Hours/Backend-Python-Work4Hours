from utils.db import db, get_session
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
        with get_session() as session:
            categories: list[dict] = []
            query = session.execute(db.session.query(Categories))
            for category in query.scalars():
                categories.append({
                    "categoryName": category.nombrecateg,
                    "categId": category.idcategoria
                }
                )
            session.commit()
            return categories