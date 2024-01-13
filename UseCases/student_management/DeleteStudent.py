class DeleteStudent:
    def __init__(self, student_repository):
        self.student_repository = student_repository

    def execute(self, student_id):
        return self.student_repository.delete(student_id)