from typing import Type
from Core.entities.Student import Student
from Core.use_cases.interfaces.IStudentRepository import IStudentRepository


class CreateStudent:
    def __init__(self, student_repository: Type[IStudentRepository]):
        self.student_repository = student_repository

    def execute(self, name: str, email: str, personal_identification: str):
        student = Student(name=name, email=email, personal_identification=personal_identification)
        return self.student_repository.add(student)