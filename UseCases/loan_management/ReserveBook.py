class ReserveBook:
    def __init__(self, book_repository, student_repository):
        self.book_repository = book_repository
        self.student_repository = student_repository

    def execute(self, book_id, student_id):
        book = self.book_repository.get_by_id(book_id)
        student = self.student_repository.get_by_id(student_id)

        if book is None or book.status != 'Available':
            raise Exception("Book is not available for reservation")

        if student is None:
            raise Exception("Student not found")

        book.reserve(student_id)
        self.book_repository.update(book)