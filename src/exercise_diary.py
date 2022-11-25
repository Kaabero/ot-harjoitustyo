import sys
from datetime import datetime
from user import User
from exercise_database import ExerciseDatabase


class ExerciseDiary():

    def __init__(self, user: User):
        self._user=user
        self._exercises = ExerciseDatabase()

    def start(self):
        # Kirjautuneen käyttäjän toiminnot
        print("")
        print(f"Welcome {self._user.username}!")
        self.logged_in_instructions()

        while True:
            print("")
            command = input("What do you want to do? ")

            if command == "0":
                self.logout()
            if command == "1":
                self.add_new_activity()
            if command == "2":
                # väliaikaisesti, poistetaan sovelluksen edetessä:
                self.logged_in_instructions()
            if command == "3":
                # väliaikaisesti, poistetaan sovelluksen edetessä:
                self.logged_in_instructions()
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
                    self._exercises.add_new_activity(self._user.username, activity, \
                        self.valid_date(dateinput), self.valid_duration(hours, minutes))
                    print("Activity added successfully!")
                    return True
        return False

    def valid_activity(self, activity:str):

        if len(activity)<=1:
            print("The name of activity is incomplete, please try again!")
            return False

        return True

    def valid_date(self, dateinput: str):
        try:
            parts = dateinput.split("-")
            date = datetime(int(parts[0]), int(parts[1]), int(parts[2]))
            return date
        except BaseException:
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

    def logout(self):
        sys.exit()
