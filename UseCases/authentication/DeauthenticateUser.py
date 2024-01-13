class DeauthenticateUser:
    def __init__(self, auth_service):
        self.auth_service = auth_service

    def execute(self, user_id):
        return self.auth_service.deauthenticate(user_id)