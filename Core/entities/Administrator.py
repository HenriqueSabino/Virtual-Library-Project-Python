class Administrator:
    def __init__(self, identifier, name, email, hashed_password):
        self.id = identifier
        self.name = name
        self.email = email
        self.hashed_password = hashed_password

    def set_password(self, new_password):
        # Logic to hash new_password and set to hashed_password
        pass

    def check_password(self, password):
        # Logic to verify if a given password matches hashed_password
        pass