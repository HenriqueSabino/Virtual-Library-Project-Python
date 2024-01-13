class UpdateStudentUseCase:
    def __init__(self, student_repository):
        self.student_repository = student_repository

    def execute(self, student_id, student_data):
        student = self.student_repository.get_by_id(student_id)
        if not student:
            raise Exception('Student not found')

        updated_student = self.student_repository.update(student_id, student_data)
        return updated_student