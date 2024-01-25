class User: # Used to initialise User objects with login credentials
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

