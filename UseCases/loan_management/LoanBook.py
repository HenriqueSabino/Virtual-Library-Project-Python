from Core.use_cases.interfaces.IBookRepository import IBookRepository
from Core.use_cases.interfaces.IStudentRepository import IStudentRepository
from Core.entities.Book import BookStatus

class LoanBook:
    def __init__(self, book_repository: IBookRepository, student_repository: IStudentRepository):
        self.book_repository = book_repository
        self.student_repository = student_repository

    def execute(self, book_id: int, student_id: int):
        book = self.book_repository.get_by_id(book_id)
        student = self.student_repository.get_by_id(student_id)
        if book and book.status == BookStatus.AVAILABLE and student:
            self.book_repository.update_status(book_id, BookStatus.RENTED)
            self.student_repository.add_book_to_student_loan_records(student_id, book_id)
            return True
        return False