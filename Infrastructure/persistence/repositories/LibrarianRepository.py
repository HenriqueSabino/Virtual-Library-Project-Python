from Core.use_cases.interfaces.ILibrarianRepository import ILibrarianRepository
from Infrastructure.persistence.models.LibrarianModel import LibrarianModel
from Infrastructure.persistence.database import get_db_session

class LibrarianRepository(ILibrarianRepository):
    def __init__(self):
        self.session = get_db_session()

    def add_librarian(self, librarian):
        new_librarian = LibrarianModel(
            name=librarian.name,
            email=librarian.email
        )
        self.session.add(new_librarian)
        self.session.commit()

    def get_librarian_by_id(self, librarian_id):
        return self.session.query(LibrarianModel).get(librarian_id)

    def remove_librarian(self, librarian_id):
        librarian = self.get_librarian_by_id(librarian_id)
        if librarian:
            self.session.delete(librarian)
            self.session.commit()

    def update_librarian(self, librarian_id, update_fields):
        librarian = self.get_librarian_by_id(librarian_id)
        if librarian:
            for field, value in update_fields.items():
                setattr(librarian, field, value)
            self.session.commit()

    def list_librarians(self):
        return self.session.query(LibrarianModel).all()