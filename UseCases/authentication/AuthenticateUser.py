class AuthenticateUser:
    def __init__(self, authentication_service):
        self._authentication_service = authentication_service

    def execute(self, username, password):
        return self._authentication_service.authenticate(username, password)