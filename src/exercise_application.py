from user import User
from exercise_service import ExerciseService


class ExerciseApplication():
    # Käyttäjän kanssa kommunikoinnista vastaava luokka

    def __init__(self):

        self._service = ExerciseService("users.txt")
        self._user = None

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
                self._user = None
                self._service.save()
                break

            if command == "1":
                username, password = self.get_username_and_password()
                self._user=self._service.create_user(username, password)
                if self._user is not None:
                    self.logged_in(self._user)

            if command == "2":
                username, password = self.get_username_and_password()
                if self._service.login(username, password):
                    print("Login successfully!")
                    self.logged_in(self._service.login(username, password))
                else:
                    print("Invalid username or password")
                    continue
            if command not in "012":
                self.login_instructions()

    def get_username_and_password(self):
        username = input("Username: ")
        password = input("Password: ")
        return username, password

    def logged_in(self, user: User):
        # Kirjautuneen käyttäjän toiminnot

        print("")
        print(f"Welcome {user.username}!")
        self.logged_in_instructions()

        while True:
            print("")
            command = input("What do you want to do? ")

            if command == "0":
                self._service.save()
                break
            if command == "1":
                self.add_new_activity(user)
            if command == "2":
                self._service.current_week(user)
            if command == "3":
                target = input("Give the target amount for weekly exercises: ")
                self._service.add_target(user, target)
            if command == "4":
                # väliaikaisesti, poistetaan sovelluksen edetessä:
                self._service.get_all_activities(user)
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

        activity = input("Type of exercise: ")

        if self._service.valid_activity(activity):
            dateinput = input("Date (YYYY-MM-DD): ")

            if self._service.valid_date(dateinput) is not False:
                print("Duration: ")
                hours = (input("hours: "))
                minutes = (input("minutes: "))

                if self._service.valid_duration(hours, minutes) is not False:
                    self._service.exercises.add_new_activity(user.username, activity,
                                                     self._service.valid_date(
                                                         dateinput),
                                                     self._service.valid_duration(hours, minutes))
                    print("Activity added successfully!")
                    return True
        return False
