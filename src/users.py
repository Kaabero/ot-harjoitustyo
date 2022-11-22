
from user import User

class Users():

    def __init__(self):
        self._users=[]

    def get_all_users(self):
        return self._users

    def add_new_user(self, user: User):
        self._users.append(user)
