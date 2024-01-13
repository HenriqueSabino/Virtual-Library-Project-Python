from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from .database import Base

class BookStatus(str, Enum):
    AVAILABLE = "Available"
    RENTED = "Rented"
    RESERVED = "Reserved"
    UNDER_MAINTENANCE = "Under Maintenance"

class BookModel(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    isbn = Column(String, unique=True, index=True)
    status = Column(Enum(BookStatus), default=BookStatus.AVAILABLE)

    # Relationships
    rentals = relationship("RentalModel", back_populates="book")