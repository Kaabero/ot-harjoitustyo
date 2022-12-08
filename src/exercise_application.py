import sys
from user import User
from exercise_service import ExerciseService


class ExerciseApplication():
    """Luokka, joka vastaa kommunikoinnista käyttäjän kanssa."""

    def __init__(self):
        """Luokan konstruktori, joka luo uuden käyttöliittymästä vastaavan luokan."""

        self._service = ExerciseService("users.txt")
        self._user = None

    def login_instructions(self):
        print("")
        print("Instructions: ")
        print("Press 0 to finish")
        print("Press 1 to create a new user")
        print("Press 2 to login")

    def execute(self):
        """Käyttöliittymän käynnistys."""

        self.login_instructions()
        while self._user is None:

            command=self.get_command()

            if command == "0":
                self.exit()

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

    def get_command(self):
        print("")
        command = input("What do you want to do? ")
        return command

    def get_username_and_password(self):
        """Palauttaa käyttäjän syöttämät tunnukset"""

        username = input("Username: ")
        password = input("Password: ")
        return username, password

    def logged_in(self, user: User):
        """Kirjautuneen käyttäjän toiminnot

        Args:
            user: Kirjautunut käyttäjä User -oliona
        """

        print("")
        print(f"Welcome {user.username}!")
        self.logged_in_instructions()

        while True:
            command = self.get_command()

            if command == "0":
                self.exit()
            if command == "1":
                self.add_new_activity(user)
            if command == "2":
                self._service.current_week(user)
            if command == "3":
                target = input("Give the target amount for weekly exercises: ")
                self._service.add_target(user, target)
            if command == "4":
                self.stats(user)
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
        """Kysyy käyttäjältä tiedot uudesta liikuntasuorituksesta

        Args:
            user: Kirjautunut käyttäjä User -oliona

        Returns:
            True, jos syötteet ovat kelvolliset, muussa tapauksessa False.
        """

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

    def stats(self, user: User):
        """Kysyy käyttäjältä tiedot halutuista tilastoista.

        Args:
            user: Kirjautunut käyttäjä User -oliona
        """

        print("")
        self.stats_instructions()

        while True:
            command = self.get_command()

            if command == "0":
                self.logged_in_instructions()
                break
            if command == "1":
                self._service.get_all_activities(user)
            if command == "2":
                print("Please, give the date range ")
                datefrom = input("From: ")
                if self._service.valid_date(datefrom):
                    dateto = input("To: ")
                    if self._service.valid_date(dateto):
                        self._service.activities_by_date(user, self._service.valid_date(datefrom), \
                        self._service.valid_date(dateto))

            if command == "3":
                activity = input("Please, give the type of exercise: ")
                if self._service.valid_activity(activity):
                    self._service.activities_by_activity(user, activity)

            if command not in "0123":
                self.stats_instructions()

    def stats_instructions(self):
        print("")
        print("Instructions: ")
        print("Press 0 to finish with stats")
        print("Press 1 to see all activities added")
        print("Press 2 to search by date")
        print("Press 3 to search by activity")

    def exit(self):
        """Lopettaa istunnon ja tallentaa käyttäjätiedot."""
        self._user=None
        self._service.save()
        sys.exit()
