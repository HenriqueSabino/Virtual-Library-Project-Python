from typing import Type
from Core.entities.Book import Book
from Core.use_cases.interfaces.IBookRepository import IBookRepository

class CreateBook:

    def __init__(self, book_repository: Type[IBookRepository]):
        self.book_repository = book_repository

    def execute(self, title: str, author: str, isbn: str, status: str) -> Book:
        new_book = Book(title=title, author=author, isbn=isbn, status=status)
        return self.book_repository.add(new_book)