from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .Base import Base

class LibrarianModel(Base):
    __tablename__ = 'librarians'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)

    # Relationship with other tables if necessary, for example:
    # books_managed = relationship("BookModel", back_populates="librarian")
```
