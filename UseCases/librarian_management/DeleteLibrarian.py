class DeleteLibrarian:
    def __init__(self, librarian_repository):
        self.librarian_repository = librarian_repository
    
    def execute(self, librarian_id):
        return self.librarian_repository.delete_librarian(librarian_id)