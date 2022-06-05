from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import as_declarative, declared_attr, Session, sessionmaker
from flask_sqlalchemy import SQLAlchemy

from config import settings

db = SQLAlchemy()
metadata = MetaData()
engine = create_engine(url=settings.DB_URI, echo=True, encoding="utf-8")
sync_session = sessionmaker(
    bind=engine,
    class_=Session
)

@as_declarative(metadata=metadata)
class Base:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lowercase()
    pass

def get_session():
    with sync_session() as session:
        try:    
            return session
        except:
            pass