from core.use_cases.interfaces import IAdminRepository
from persistence.models.AdministratorModel import AdministratorModel

class AdminRepository(IAdminRepository):
    def __init__(self, db_session):
        self.db_session = db_session

    def create_admin(self, admin):
        new_admin = AdministratorModel(name=admin.name, role=admin.role)
        self.db_session.add(new_admin)
        self.db_session.commit()
        return new_admin

    def update_admin(self, admin_id, admin):
        existing_admin = self.db_session.query(AdministratorModel).filter(AdministratorModel.id == admin_id).first()
        if existing_admin is not None:
            existing_admin.name = admin.name
            existing_admin.role = admin.role
            self.db_session.commit()
        return existing_admin

    def delete_admin(self, admin_id):
        admin_to_delete = self.db_session.query(AdministratorModel).filter(AdministratorModel.id == admin_id).first()
        if admin_to_delete is not None:
            self.db_session.delete(admin_to_delete)
            self.db_session.commit()
            return True
        return False

    def get_admin(self, admin_id):
        return self.db_session.query(AdministratorModel).filter(AdministratorModel.id == admin_id).first()

    def list_admins(self):
        return self.db_session.query(AdministratorModel).all()