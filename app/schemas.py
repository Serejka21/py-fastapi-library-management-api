from datetime import date

from pydantic import BaseModel


class BookBase(BaseModel):
    tittle: str
    summary: str


class BookCreate(BookBase):
    publication_date: date
    author_id: int


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    name: str
    bio: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True
