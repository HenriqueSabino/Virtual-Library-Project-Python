from core.use_cases.interfaces import IAuthenticationService
from persistence.repositories import UserRepository

class AuthenticationService(IAuthenticationService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def authenticate(self, username: str, password: str) -> bool:
        user = self.user_repository.find_by_username(username)
        if user and user.password == password:
            # Ideally, password should be hashed and checked against the hash stored in the database.
            # For simplicity, we're checking plaintext passwords here.
            return True
        return False

    def deauthenticate(self, user_id: int) -> None:
        # This method would handle logic to deauthenticate a user, which may involve
        # invalidating tokens or sessions.
        pass