from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import get_books, get_book, create_book, update_book, delete_book
from schemas import BookCreate, BookUpdate, BookResponse
from database import get_db

router = APIRouter(prefix="/api/books", tags=["books"])

@router.get("/", response_model=list[BookResponse])
def read_books(db: Session = Depends(get_db)):
    return get_books(db)

@router.get("/{book_id}", response_model=BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=BookResponse, status_code=201)
def create_book_endpoint(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)

@router.put("/{book_id}", response_model=BookResponse)
def update_book_endpoint(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    updated = update_book(db, book_id, book)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

@router.delete("/{book_id}", status_code=204)
def delete_book_endpoint(book_id: int, db: Session = Depends(get_db)):
    deleted = delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return None
