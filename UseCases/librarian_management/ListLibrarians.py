class ListLibrarians:
    def __init__(self, librarian_repository):
        self.librarian_repository = librarian_repository

    def execute(self):
        return self.librarian_repository.get_all_librarians()