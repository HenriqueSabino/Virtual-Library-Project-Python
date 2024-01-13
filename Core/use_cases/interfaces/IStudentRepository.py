from abc import ABC, abstractmethod
from typing import List, Optional
from entities.Student import Student

class IStudentRepository(ABC):

    @abstractmethod
    def add_student(self, student: Student) -> None:
        """Adds the student to the repository."""
        pass

    @abstractmethod
    def get_student_by_id(self, student_id: str) -> Optional[Student]:
        """Gets a student by their ID."""
        pass

    @abstractmethod
    def update_student(self, student: Student) -> None:
        """Updates the student in the repository."""
        pass

    @abstractmethod
    def delete_student(self, student_id: str) -> None:
        """Deletes the student from the repository."""
        pass

    @abstractmethod
    def get_all_students(self) -> List[Student]:
        """Gets all students."""
        pass

    @abstractmethod
    def get_rental_history(self, student_id: str) -> List:
        """Gets rental history for a student."""
        pass