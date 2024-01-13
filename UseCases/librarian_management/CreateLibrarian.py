from core.entities.Librarian import Librarian
from core.use_cases.interfaces.ILibrarianRepository import ILibrarianRepository

class CreateLibrarian:

    def __init__(self, librarian_repo: ILibrarianRepository):
        self.librarian_repo = librarian_repo

    def execute(self, name: str, email: str, password: str) -> Librarian:
        new_librarian = Librarian(name=name, email=email, password=password)
        return self.librarian_repo.add(new_librarian)