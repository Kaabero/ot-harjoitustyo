from datetime import datetime
from user import User
from file_service import FileService
from users import Users
from exercise_database import ExerciseDatabase


class ExerciseApplication():
    # Käyttäjän kanssa kommunikoinnista vastaava luokka

    def __init__(self, file: str):
        self._users = Users()
        self._file = FileService(file)
        self._user = None
        self._exercises = ExerciseDatabase()

        for loaded_username, data in self._file.load().items():
            username = loaded_username
            password = data[0]
            user = User(username, password)
            if len(data)>1:
                user.weekly_target=data[1]
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
                self._user = None
                self._file.save(self._users.get_all_users())
                break

            if command == "1":
                username, password = self.get_username_and_password()
                self.create_user(username, password)

            if command == "2":
                username, password = self.get_username_and_password()
                if self.login(username, password):
                    self.logged_in(self._user)
                else:
                    print("Invalid username or password")
                    continue
            if command not in "012":
                self.login_instructions()

    def get_username_and_password(self):
        username = input("Username: ")
        password = input("Password: ")
        return username, password

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

    def logged_in(self, user: User):
        # Kirjautuneen käyttäjän toiminnot
        #ExerciseDiary(user, self._users.get_all_users(), self._file_name).start()

        print("")
        print(f"Welcome {user.username}!")
        self.logged_in_instructions()

        while True:
            print("")
            command = input("What do you want to do? ")

            if command == "0":
                self._file.save(self._users.get_all_users())
                break
            if command == "1":
                self.add_new_activity()
            if command == "2":
                self.current_week()
            if command == "3":
                self.add_target()
            if command == "4":
                # väliaikaisesti, poistetaan sovelluksen edetessä:
                self.get_all_activities()
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

    def add_new_activity(self):

        activity = input("Type of exercise: ")

        if self.valid_activity(activity):
            dateinput = input("Date (YYYY-MM-DD): ")

            if self.valid_date(dateinput) is not False:
                print("Duration: ")
                hours = (input("hours: "))
                minutes = (input("minutes: "))

                if self.valid_duration(hours, minutes) is not False:
                    self._exercises.add_new_activity(self._user.username, activity,
                                                     self.valid_date(
                                                         dateinput),
                                                     self.valid_duration(hours, minutes))
                    print("Activity added successfully!")
                    return True
        return False

    def valid_activity(self, activity: str):

        if len(activity) <= 1:
            print("The name of activity is incomplete, please try again!")
            return False

        return True

    def valid_date(self, dateinput: str):
        try:
            parts = dateinput.split("-")
            date = datetime(int(parts[0]), int(parts[1]), int(parts[2]))
            return date
        except:
            print("Invalid date, please try again!")
            return False

    def valid_duration(self, hours, minutes):

        try:
            hours = int(hours)
            minutes = int(minutes)
            duration = 60*hours+minutes
            return duration
        except ValueError:
            print("Please, give hours and minutes numerically")
            return False

    def get_all_activities(self):
        print(self._exercises.activities_by_user(self._user.username))

    def current_week(self):
        activities = self._exercises.current_week_activities_by_user(
            self._user.username)
        if self._user.weekly_target is not None:
            print("")
            target=self._user.weekly_target
            print(f"Weekly target: You have done {len(activities)}/{target} exercises :)")
        if len(activities) > 0:
            print("")
            print("Your current week")
            if len(activities) == 1:
                print(f"You have added {len(activities)} activity:")
            else:
                print(f"You have added {len(activities)} activities:")
            for activity in activities:
                duration=self.get_duration_in_hours_and_minutes(activity[4])
                date=self.get_date(activity[3])
                print(
                    f"Activity: {activity[2]}, date: {date}, duration: {duration}")
        else:
            print("You haven't added any activity to this week yet")

    def get_duration_in_hours_and_minutes(self, duration: int):
        hours = int(duration/60)
        minutes = duration % 60
        if hours > 0 and minutes > 0:
            return f"{hours} h and {minutes} min"
        if hours > 0 and minutes == 0:
            return f"{hours} h"
        return f"{minutes} min"

    def get_date(self, date):
        parts = date.split("-")
        year = parts[0]
        month = parts[1]
        day = parts[2][0]+parts[2][1]
        return f"{day}.{month}.{year}"

    def add_target(self):
        target = int(input("Give the target amount for weekly exercises: "))
        self._user.set_target(target)
