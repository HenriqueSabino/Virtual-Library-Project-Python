from abc import ABC, abstractmethod
from entities.Librarian import Librarian
from entities.Administrator import Administrator

class IUserRepository(ABC):

    @abstractmethod
    def add_librarian(self, librarian: Librarian) -> Librarian:
        pass

    @abstractmethod
    def get_librarian_by_id(self, librarian_id: int) -> Librarian:
        pass

    @abstractmethod
    def remove_librarian(self, librarian_id: int) -> None:
        pass

    @abstractmethod
    def update_librarian(self, librarian: Librarian) -> Librarian:
        pass

    @abstractmethod
    def add_administrator(self, administrator: Administrator) -> Administrator:
      pass

    @abstractmethod
    def get_administrator_by_id(self, administrator_id: int) -> Administrator:
        pass

    @abstractmethod
    def remove_administrator(self, administrator_id: int) -> None:
        pass

    @abstractmethod
    def update_administrator(self, administrator: Administrator) -> Administrator:
        pass