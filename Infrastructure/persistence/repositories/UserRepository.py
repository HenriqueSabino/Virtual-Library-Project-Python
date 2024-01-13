from Core.use_cases.interfaces.IUserRepository import IUserRepository
from Infrastructure.persistence.models.UserModel import UserModel
from Infrastructure.persistence.database import SessionLocal


class UserRepository(IUserRepository):
    def __init__(self):
        self.session = SessionLocal()

    def find_user_by_credentials(self, username, hashed_password):
        return self.session.query(UserModel).filter_by(
            username=username, 
            hashed_password=hashed_password
        ).first()

    def find_user_by_id(self, user_id):
        return self.session.query(UserModel).filter_by(id=user_id).first()
    
    def add_user(self, user_entity):
        new_user = UserModel(
            username=user_entity.username,
            hashed_password=user_entity.hashed_password,
            role=user_entity.role
        )
        self.session.add(new_user)
        self.session.commit()
        return new_user
    
    def remove_user(self, user_id):
        user_to_delete = self.session.query(UserModel).filter_by(id=user_id).first()
        if user_to_delete:
            self.session.delete(user_to_delete)
            self.session.commit()
            return True
        return False
    
    def update_user(self, user_id, updated_user_entity):
        user_to_update = self.session.query(UserModel).filter_by(id=user_id).first()
        if user_to_update:
            user_to_update.username = updated_user_entity.username
            user_to_update.hashed_password = updated_user_entity.hashed_password
            user_to_update.role = updated_user_entity.role
            self.session.commit()
            return True
        return False