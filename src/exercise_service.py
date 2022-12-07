from datetime import datetime
from user import User
from file_service import FileService
from users import Users
from exercise_database import ExerciseDatabase


class ExerciseService():

    def __init__(self, file: str):
        self._users = Users()
        self._file = FileService(file)
        self.exercises = ExerciseDatabase()

        for loaded_username, data in self._file.load().items():
            username = loaded_username
            password = data[0]
            user = User(username, password)
            if len(data)>1:
                user.weekly_target=data[1]
            self._users.add_new_user(user)

    def save(self):
        self._file.save(self._users.get_all_users())


    def create_user(self, username, password):
        # Luo uuden käyttäjän ja kirjaa käyttäjän sisään.

        if len(username) < 2:
            print("Minimum username length is two characters. Please try again.")
            return None

        if len(password) < 8:
            print("Minimum password length is eight characters. Please try again.")
            return None

        for user in self._users.get_all_users():
            if user.username == username:
                print(f"Username {username} already exists")
                return None

        user = User(username, password)
        self._users.add_new_user(user)
        return user

    def login(self, username, password):
        # Kirjaa käyttäjän sisään

        for user in self._users.get_all_users():
            if user.username == username:
                if user.password == password:
                    return user
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

    def current_week(self, user: User):
        activities = self.exercises.current_week_activities_by_user(
            user.username)
        if user.weekly_target !="None" and user.weekly_target is not None:
            print("")
            target=user.weekly_target
            print(f"Weekly target: You have done {len(activities)}/{target} exercises :)")
        if len(activities) > 0:
            print("")
            print("Your current week:")
            if len(activities) == 1:
                print(f"You have added {len(activities)} activity")
            else:
                print(f"You have added {len(activities)} activities")
            for activity in activities:
                duration=self.get_duration_in_hours_and_minutes(activity[4])
                date=self.get_date(activity[3])
                print(
                    f"Activity: {activity[2]}, date: {date}, duration: {duration}")
        else:
            print("You haven't added any activity to this week yet")

    def get_all_activities(self, user: User):
        print(self.exercises.activities_by_user(user.username))


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

    def add_target(self, user: User, target: str):
        try:
            target=int(target)

        except ValueError:
            print("Please, give target numerically")
            return
        if target>=0:
            user.set_target(target)
        else:
            print("Please, give positive target number")
            return
