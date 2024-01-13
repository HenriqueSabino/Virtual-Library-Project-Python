from typing import List
from core.use_cases.interfaces import IStudentRepository
from core.entities.Student import Student

class ListStudents:
    def __init__(self, student_repository: IStudentRepository):
        self.student_repository = student_repository

    def list_all_students(self) -> List[Student]:
        return self.student_repository.get_all_students()