from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import schemas as _schemas
import services as _services
import models
from database import create_db



if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()

@app.on_event("startup")
def on_startup():
    create_db()  # Crear tablas al iniciar la app

@app.post("/api/books/", response_model=_schemas.Book)
async def create_book(
        book: _schemas.CreateBook,
        db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.create_book(book=book, db=db)

@app.get("/api/books/", response_model=List[_schemas.Book])
async def get_books(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_books(db=db)

@app.get("/api/books/{book_id}", response_model=_schemas.Book)
async def get_book(book_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    book = await _services.get_book(book_id=book_id, db=db)
    if book is None:
        raise _fastapi.HTTPException(status_code=404, detail="Book not found")
    return book

# obtener libro por autor
@app.get("/api/books/author/{author}", response_model=List[_schemas.Book])
async def get_book_by_author(author: str, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    books = await _services.get_book_by_author(author=author, db=db)
    if not books:
        raise _fastapi.HTTPException(status_code=404, detail="Books not found")
    return books

# obtener libro por titulo
@app.get("/api/books/title/{title}", response_model=List[_schemas.Book])
async def get_book_by_title(title: str, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    books = await _services.get_book_by_title(title=title, db=db)
    if not books:
        raise _fastapi.HTTPException(status_code=404, detail="Books not found")
    return books

@app.delete("/api/books/{book_id}")
async def delete_book(book_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    book = await _services.get_book(book_id=book_id, db=db)
    if book is None:
        raise _fastapi.HTTPException(status_code=404, detail="Book not found")

    await _services.delete_book(book=book, db=db)
    return "Book deleted successfully"

@app.put("/api/books/{book_id}", response_model=_schemas.Book)
async def update_book(
        book_id: int,
        book_data: _schemas.CreateBook,
        db: _orm.Session = _fastapi.Depends(_services.get_db)):
    book = await _services.get_book(book_id=book_id, db=db)
    if book is None:
        raise _fastapi.HTTPException(status_code=404, detail="Book not found")

    return await _services.update_book(book_data=book_data, book=book, db=db)