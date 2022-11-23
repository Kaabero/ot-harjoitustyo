
import sys
from user import User
from file_service import FileService
from users import Users
from exercise_database import ExerciseDatabase
from datetime import datetime


class ExerciseApplication():
    #Käyttäjän kanssa kommunikoinnista vastaava luokka

    def __init__(self, file: str):
        self._users = Users()
        self._file = FileService(file)
        self._user = None
        self._exercises = ExerciseDatabase()
        

        for loaded_username, loaded_password in self._file.load().items():
            username = loaded_username
            password = loaded_password
            user = User(username, password)
            self._users.add_new_user(user)

    def login_instructions(self):
        print("")
        print("Instructions: ")
        print("Press 0 to finish")
        print("Press 1 to create a new user")
        print("Press 2 to login")

    def execute(self):
        self.login_instructions()
        while self._user is None:
            print("")
            command = input("What do you want to do? ")
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
        # Luo uuden käyttäjän ja kirjaa käyttäjän sisään.

        for user in self._users.get_all_users():
            if user.username == username:
                print(f"Username {username} already exists")
                return False

        if len(password) < 8:
            print("Minimum password length is eight characters. Please try again.")
            return False

        user = User(username, password)
        self._users.add_new_user(user)
        self._user = user
        self.logged_in(self._user)
        return True

    def login(self, username, password):
        # Kirjaa käyttäjän sisään

        for user in self._users.get_all_users():
            if user.username == username:
                if user.password == password:
                    self._user = user
                    print("Login successfully!")
                    return True
        return False

    def logout(self):
        # Kirjaa nykyisen käyttäjän ulos.
        self._user = None
        self._file.save(self._users.get_all_users())
        sys.exit()

    def logged_in(self, user: User):
        #Kirjautuneen käyttäjän toiminnot
        print("")
        print(f"Welcome {user.username}!")
        
        while True:
            print("")
            self.logged_in_instructions()
            print("")
            command=input("What do you want to do? ")

            if command == "0":
                self.logout()
            if command == "1":
                self.add_new_activity(user)
            if command == "2":
                # väliaikaisesti, poistetaan sovelluksen edetessä:
                self.logged_in_instructions()
            if command == "3":
                # väliaikaisesti, poistetaan sovelluksen edetessä:
                self.logged_in_instructions()
            if command == "4":
                # väliaikaisesti, poistetaan sovelluksen edetessä:
                self.get_all_activities(user)
            if command not in "01234":
                self.logged_in_instructions()

    def logged_in_instructions(self):
        print("")
        print("Instructions: ")
        print("Press 0 to logout")
        print("Press 1 to add a new activity")
        print("Press 2 to see your current week")
        print("Press 3 to add a weekly target")
        print("Press 4 for stats")

    def add_new_activity(self, user: User):

        activity=input("Type of exercise: ")
        dateinput=input("Date (YYYY-MM-DD): ")
        print("Duration: ")
        hours=int(input("hours: "))
        minutes=int(input("minutes: "))
        duration=60*hours+minutes
        try:
            parts=dateinput.split("-")
            date=datetime(int(parts[0]), int(parts[1]), int(parts[2]))
        except:
            print("Invalid date, please try again!")
            return
            
        try:
            id = self._exercises.add_new_activity(user.username, activity, date, duration)
            print(f"Activity added successfully! This is your {id}. note!")
        except:
            print("Invalid inputs, please try again!")
            return
            
        
    def get_all_activities(self, user: User):
        print(self._exercises.activities_by_user(user.username))
