class DeleteBook:
    def __init__(self, book_repository):
        self.book_repository = book_repository

    def execute(self, book_id):
        book = self.book_repository.find_by_id(book_id)
        if book:
            self.book_repository.delete(book)
            return True
        return False