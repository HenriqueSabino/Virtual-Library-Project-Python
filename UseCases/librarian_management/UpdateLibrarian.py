from typing import Optional

from Core.use_cases.interfaces.ILibrarianRepository import ILibrarianRepository
from Core.entities.Librarian import Librarian

class UpdateLibrarian:
    def __init__(self, librarian_repo: ILibrarianRepository):
        self.librarian_repo = librarian_repo
    
    def execute(self, librarian_id: int, name: Optional[str], email: Optional[str], password: Optional[str]) -> Librarian:
        librarian = self.librarian_repo.get_by_id(librarian_id)

        if not librarian:
            raise ValueError("Librarian with the given ID does not exist")

        if name:
            librarian.name = name
        
        if email:
            librarian.email = email
        
        if password:
            # Here you should hash the password before storing it
            librarian.password = password

        return self.librarian_repo.update(librarian)