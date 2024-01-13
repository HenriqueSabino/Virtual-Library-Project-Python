class ListBooks:
    def __init__(self, book_repository):
        self.book_repository = book_repository
    
    def execute(self):
        return self.book_repository.list_books()