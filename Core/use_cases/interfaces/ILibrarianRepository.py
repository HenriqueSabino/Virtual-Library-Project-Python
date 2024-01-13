from abc import ABC, abstractmethod
from typing import List

from core.entities.Librarian import Librarian

class ILibrarianRepository(ABC):

    @abstractmethod
    def add_librarian(self, librarian: Librarian) -> None:
        pass

    @abstractmethod
    def get_librarian(self, librarian_id: int) -> Librarian:
        pass

    @abstractmethod
    def get_all_librarians(self) -> List[Librarian]:
        pass

    @abstractmethod
    def update_librarian(self, librarian: Librarian) -> None:
        pass
    
    @abstractmethod
    def delete_librarian(self, librarian_id: int) -> None:
        pass