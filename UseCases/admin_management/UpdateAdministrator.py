class UpdateAdministrator:
    def __init__(self, admin_repository):
        self.admin_repository = admin_repository

    def execute(self, admin_id, **kwargs):
        administrator = self.admin_repository.find_by_id(admin_id)
        if not administrator:
            raise ValueError("Administrator not found")

        updated_fields = {k: v for k, v in kwargs.items() if v is not None}

        if updated_fields:
            self.admin_repository.update(admin_id, **updated_fields)
        
        return self.admin_repository.find_by_id(admin_id)