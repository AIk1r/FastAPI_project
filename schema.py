# build a schema using pydantic
import models
from pydantic import BaseModel
from typing import Optional


class Book(BaseModel):
    title: str
    rating: int
    author_id: int

    class Config:
        orm_mode = True


class BookUpdate(BaseModel):
    title: Optional[str] = None
    rating: Optional[int] = None
    author_id: Optional[int] = None

    class Config:
        orm_mode = True


class Author(BaseModel):
    name: str
    age: int

    class Config:
        orm_mode = True
