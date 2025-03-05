from typing import TYPE_CHECKING, List

import database as _database
import models as _models
import schemas as _schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def create_book(book: _schemas.CreateBook, db: "Session") -> _schemas.Book:
    book = _models.Book(**book.dict())
    db.add(book)
    db.commit()
    db.refresh(book)
    return _schemas.Book.from_orm(book)

async def get_all_books(db: "Session") -> List[_schemas.Book]:
    books = db.query(_models.Book).all()
    return list(map(_schemas.Book.from_orm, books))

async def get_book(book_id: int, db: "Session") -> _schemas.Book:
    book = db.query(_models.Book).filter(_models.Book.id == book_id).first()
    return book

# obtener libro por autor
async def get_book_by_author(author: str, db: "Session") -> List[_schemas.Book]:
    books = db.query(_models.Book).filter(_models.Book.author == author).all()
    return list(map(_schemas.Book.from_orm, books))

#obtener libro por titulo
async def get_book_by_title(title: str, db: "Session") -> List[_schemas.Book]:
    books = db.query(_models.Book).filter(_models.Book.title == title).all()
    return list(map(_schemas.Book.from_orm, books))

async def delete_book(book: _models.Book, db: "Session") -> None:
    db.delete(book)
    db.commit()
    return None

async def update_book(
        book_data: _schemas.CreateBook,
        book: _models.Book,
        db: "Session") -> _schemas.Book:
    book.title = book_data.title
    book.author = book_data.author
    book.year = book_data.year
    book.isbn = book_data.isbn

    db.commit()
    db.refresh(book)

    return _schemas.Book.from_orm(book)