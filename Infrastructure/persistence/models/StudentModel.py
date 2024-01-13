from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.persistence.database import Base
from infrastructure.persistence.models.BookModel import BookModel

class StudentModel(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    rental_history = relationship('BookModel', secondary='student_book_association')

student_book_association = Table(
    'student_book_association', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('book_id', Integer, ForeignKey('books.id'))
)