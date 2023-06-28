import os

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, Session
from sqlalchemy.sql import func
from dotenv import load_dotenv

Base = declarative_base()

load_dotenv()

POSTGRES_URL = os.getenv('DATABASE_URL')

engine = create_engine(
    POSTGRES_URL, echo=True
)
DBSession = Session(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    rating = Column(Float)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    author_id = Column(Integer, ForeignKey('author.id'))

    author = relationship('Author')


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
