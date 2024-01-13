class ReturnBook:
    def __init__(self, book_repository, loan_repository):
        self.book_repository = book_repository
        self.loan_repository = loan_repository

    def execute(self, book_id, librarian_id):
        book = self.book_repository.get_by_id(book_id)
        if not book:
            raise ValueError("Book not found")

        if book.status != 'Rented':
            raise ValueError("Book is not rented")

        loan_record = self.loan_repository.get_active_loan_by_book_id(book_id)
        if not loan_record:
            raise ValueError("Active loan record not found")

        if loan_record.librarian_id != librarian_id:
            raise PermissionError("Only the librarian who loaned the book can return it")

        book.status = 'Available'  # Update the book's status to available.
        self.book_repository.update(book)  # Persist changes to the database.

        loan_record.returned = True  # Mark the loan as returned.
        self.loan_repository.update(loan_record)  # Persist changes to the database.

        # Optionally: Check the book condition and set to 'Under Maintenance' if needed.

        return book