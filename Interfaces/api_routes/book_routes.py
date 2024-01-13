from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from use_cases.book_management import CreateBook, UpdateBook, DeleteBook, ListBooks
from core.entities.Book import Book
from core.use_cases.interfaces.IBookRepository import IBookRepository

# Assuming dependency injection for the book repository is already set up
router = APIRouter()

@router.post("/books/", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_data: Book, book_repository: IBookRepository = Depends()):
    create_book_use_case = CreateBook(book_repository)
    return create_book_use_case.execute(book_data)

@router.get("/books/", response_model=List[Book])
def list_books(book_repository: IBookRepository = Depends()):
    list_books_use_case = ListBooks(book_repository)
    return list_books_use_case.execute()

@router.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_data: Book, book_repository: IBookRepository = Depends()):
    update_book_use_case = UpdateBook(book_repository)
    return update_book_use_case.execute(book_id, book_data)

@router.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, book_repository: IBookRepository = Depends()):
    delete_book_use_case = DeleteBook(book_repository)
    delete_book_use_case.execute(book_id)
    return {"message": "Book deleted successfully"}