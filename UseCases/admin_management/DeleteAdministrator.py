class DeleteAdministrator:

    def __init__(self, admin_repository):
        self.admin_repository = admin_repository

    def execute(self, admin_id):
        return self.admin_repository.delete(administrator_id=admin_id)