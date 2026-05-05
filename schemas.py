from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    year: int | None = None
    isbn: str | None = None
    publisher: str | None = None
    pages: int | None = None
    genre: str | None = None
    description: str | None = None

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    year: int | None = None
    isbn: str | None = None
    publisher: str | None = None
    pages: int | None = None
    genre: str | None = None
    description: str | None = None

class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True
