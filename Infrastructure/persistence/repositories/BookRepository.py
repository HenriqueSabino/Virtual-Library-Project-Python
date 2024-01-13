from Core.use_cases.interfaces.IBookRepository import IBookRepository
from Infrastructure.persistence.models.BookModel import BookModel
from Infrastructure.persistence.database import Session

class BookRepository(IBookRepository):
    def __init__(self, session: Session):
        self.session = session

    def add_book(self, book):
        book_model = BookModel(title=book.title, author=book.author, isbn=book.isbn, status=book.status)
        self.session.add(book_model)
        self.session.commit()
        return book_model.id

    def update_book(self, book):
        book_model = self.session.query(BookModel).get(book.id)
        if book_model:
            book_model.title = book.title
            book_model.author = book.author
            book_model.isbn = book.isbn
            book_model.status = book.status
            self.session.commit()
            return True
        return False

    def delete_book(self, book_id):
        book_model = self.session.query(BookModel).get(book_id)
        if book_model:
            self.session.delete(book_model)
            self.session.commit()
            return True
        return False

    def get_book(self, book_id):
        book_model = self.session.query(BookModel).get(book_id)
        return book_model

    def list_books(self):
        books = self.session.query(BookModel).all()
        return books