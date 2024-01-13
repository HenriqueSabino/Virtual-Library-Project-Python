from abc import ABC, abstractmethod
from typing import List
from core.entities.Book import Book

class IBookRepository(ABC):

    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def get_book_by_isbn(self, isbn: str) -> Book:
        pass

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        pass

    @abstractmethod
    def update_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def delete_book(self, isbn: str) -> None:
        pass