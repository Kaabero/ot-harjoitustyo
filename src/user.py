class User:

    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.weekly_target = None

    def set_target(self, target):
        self.weekly_target = target
