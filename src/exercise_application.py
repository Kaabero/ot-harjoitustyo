
import sys
from user import User
from activity import Activity
from file_service import FileService
from users import Users

class ExerciseApplication():
    """Sovelluslogiikasta vastaava luokka."""

    def __init__(self):
        self._users=Users()
        self._file=FileService("users.txt")
        self._user=None

        for loaded_username, loaded_password in self._file.load().items():
            username=loaded_username
            password=loaded_password
            user=User(username, password)
            self._users.add_new_user(user)

    def login_instructions(self):
        print("Commands: ")
        print("0 Finish")
        print("1 Create new user")
        print("2 Login")

    def execute(self):
        self.login_instructions()
        while self._user is None:
            print("")
            command=input("Command: ")
            if command == "0":
                self.logout()

            if command == "1":

                username = input("Username: ")
                password = input("Password: ")

                self.create_user(username, password)

            if command == "2":
                username = input("Username: ")
                password = input("Password: ")
                if self.login(username, password):
                    self.logged_in(self._user)
                else:
                    print("Invalid username or password")
                    continue
            if command not in "012":
                self.login_instructions()

    def create_user(self, username, password):

        #Luo uuden käyttäjän ja kirjaa käyttäjän sisään.

        for user in self._users.get_all_users():
            if user.username == username:
                print(f"Username {username} already exists")
                return False

        if len(password)<8:
            print("Minimum password length is eight characters. Please try again.")
            return False

        user=User(username, password)
        self._users.add_new_user(user)
        self._user=user
        self.logged_in(self._user)
        return True

    def login(self, username, password):

        #Kirjaa käyttäjän sisään

        for user in self._users.get_all_users():
            if user.username == username:
                if user.password == password:
                    self._user=user
                    print("Login successfully!")
                    return True

        return False

    def logout(self):
        #Kirjaa nykyisen käyttäjän ulos.
        self._user = None
        self._file.save(self._users.get_all_users())
        sys.exit()

    def logged_in(self, user: User):
        print(f"Tervetuloa {user.username}!")
        #väliaikaisesti, poistetaan sovelluksen edetessä:
        self._file.save(self._users.get_all_users())
