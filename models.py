# Импортируем необходимые модули
import os
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, Session
from sqlalchemy.sql import func
from dotenv import load_dotenv

# Создаем базовый класс для объявления моделей
Base = declarative_base()

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем URL для подключения к базе данных PostgreSQL из переменной окружения
POSTGRES_URL = os.getenv('DATABASE_URL')

# Создаем движок SQLAlchemy для работы с базой данных
engine = create_engine(POSTGRES_URL, echo=True)

# Создаем сессию для работы с базой данных
DBSession = Session(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для получения экземпляра сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Определяем модель Book, которая соответствует таблице 'book' в базе данных
class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    rating = Column(Float)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    author_id = Column(Integer, ForeignKey('author.id'))

    author = relationship('Author')

# Определяем модель Author, которая соответствует таблице 'author' в базе данных
class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
