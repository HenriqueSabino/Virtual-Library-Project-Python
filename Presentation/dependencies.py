from typing import Generator

from fastapi import Depends

from infrastructure.persistence.database import SessionLocal
from infrastructure.persistence.repositories import (
    BookRepository,
    StudentRepository,
    LibrarianRepository,
    AdminRepository,
    UserRepository
)
from infrastructure.security.authentication_service import AuthenticationService


# Dependency
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# Dependency
def get_book_repository(db: SessionLocal = Depends(get_db)) -> BookRepository:
    return BookRepository(db)


# Dependency
def get_student_repository(db: SessionLocal = Depends(get_db)) -> StudentRepository:
    return StudentRepository(db)


# Dependency
def get_librarian_repository(db: SessionLocal = Depends(get_db)) -> LibrarianRepository:
    return LibrarianRepository(db)


# Dependency
def get_admin_repository(db: SessionLocal = Depends(get_db)) -> AdminRepository:
    return AdminRepository(db)


# Dependency
def get_user_repository(db: SessionLocal = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


# Dependency
def get_authentication_service(user_repo: UserRepository = Depends(get_user_repository)) -> AuthenticationService:
    return AuthenticationService(user_repo)