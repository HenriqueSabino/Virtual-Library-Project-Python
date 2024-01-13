from Core.use_cases.interfaces import IStudentRepository
from Infrastructure.persistence.models import StudentModel
from typing import List, Optional


class StudentRepository(IStudentRepository):
    def __init__(self, session):
        self.session = session

    def create_student(self, student):
        student_model = StudentModel.from_entity(student)
        self.session.add(student_model)
        self.session.commit()

    def update_student(self, student_id, student):
        student_model = self.session.query(StudentModel).filter(StudentModel.id == student_id).first()
        if student_model:
            student_model.update_from_entity(student)
            self.session.commit()

    def delete_student(self, student_id):
        student_model = self.session.query(StudentModel).filter(StudentModel.id == student_id).first()
        if student_model:
            self.session.delete(student_model)
            self.session.commit()

    def get_student_by_id(self, student_id) -> Optional[StudentModel]:
        student_model = self.session.query(StudentModel).filter(StudentModel.id == student_id).first()
        return student_model

    def list_students(self) -> List[StudentModel]:
        students = self.session.query(StudentModel).all()
        return students