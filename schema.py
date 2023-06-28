from pydantic import BaseModel
from typing import Optional


# Определение модели Book с полями title, rating и author_id
class Book(BaseModel):
    title: str  # Название книги
    rating: int  # Рейтинг книги
    author_id: int  # Идентификатор автора книги

    class Config:
        orm_mode = True


# Определение модели BookUpdate для обновления данных книги
class BookUpdate(BaseModel):
    title: Optional[str] = None  # Новое название книги (опциональное поле)
    rating: Optional[int] = None  # Новый рейтинг книги (опциональное поле)
    author_id: Optional[int] = None  # Новый идентификатор автора книги (опциональное поле)

    class Config:
        orm_mode = True


# Определение модели Author с полями name и age
class Author(BaseModel):
    name: str  # Имя автора
    age: int  # Возраст автора

    class Config:
        orm_mode = True
