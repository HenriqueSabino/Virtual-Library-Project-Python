from Core.use_cases.interfaces.IBookRepository import IBookRepository
from Core.entities.Book import Book

class UpdateBook:
    def __init__(self, book_repository: IBookRepository):
        self.book_repository = book_repository

    def execute(self, book_id: str, title: str, author: str, isbn: str, status: str) -> Book:
        book_to_update = self.book_repository.get_by_id(book_id)
        if not book_to_update:
            raise ValueError(f"Book with ID {book_id} not found.")
        
        # Updating the book properties
        book_to_update.title = title
        book_to_update.author = author
        book_to_update.isbn = isbn
        book_to_update.status = status
        
        # Persisting the updated book
        updated_book = self.book_repository.update(book_to_update)
        return updated_book