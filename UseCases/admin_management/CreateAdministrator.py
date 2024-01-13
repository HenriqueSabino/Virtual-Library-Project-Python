from Core.entities.Administrator import Administrator
from Core.use_cases.interfaces.IAdminRepository import IAdminRepository

class CreateAdministrator:
    def __init__(self, admin_repository: IAdminRepository):
        self.admin_repository = admin_repository
        
    def execute(self, name: str, email: str, hashed_password: str):
        new_admin = Administrator(name=name, email=email, hashed_password=hashed_password)
        return self.admin_repository.add(new_admin)