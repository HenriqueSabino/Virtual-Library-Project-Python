class IAuthenticationService:
    def authenticate_user(self, username: str, password: str) -> bool:
        """Authenticate a user based on provided credentials.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            bool: True if authenticated, False otherwise.
        """
        raise NotImplementedError

    def update_credentials(self, user_id: int, new_password: str) -> None:
        """Updates the credentials for a user with a new password.

        Args:
            user_id (int): The ID of the user.
            new_password (str): The new password to set.
        """
        raise NotImplementedError