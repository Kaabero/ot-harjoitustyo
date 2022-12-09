from datetime import datetime
from user import User
from file_service import FileService
from users import Users
from exercise_database import ExerciseDatabase


class ExerciseService():
    """Luokka, joka vastaa sovelluslogiikasta.

    Attributes:
        file: Merkkijonoarvo, joka kuvaa tiedoston nimeä, johon käyttäjien tiedot tallennetaan.
    """

    def __init__(self, file: str):
        """Luokan konstruktori, joka luo uuden sovelluslogiikasta vastaavan palvelun.

        Args:
            file: Merkkijonoarvo, joka kuvaa tiedoston nimeä, johon käyttäjien tiedot tallennetaan.
        """

        self._users = Users()
        self._file = FileService(file)
        self._exercises = ExerciseDatabase()

        for loaded_username, data in self._file.load().items():
            username = loaded_username
            password = data[0]
            user = User(username, password)
            if len(data)>1:
                user.weekly_target=data[1]
            self._users.add_new_user(user)

    def save(self):
        """Tallentaa käyttäjien tiedot tiedostoon."""
        self._file.save(self._users.get_all_users())


    def create_user(self, username, password):
        """Luo uuden käyttäjän.

        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjän syöttämää käyttäjätunnusta
            password: Merkkijonoarvo, joka kuvaa käyttäjän syöttämää salasanaa

        Returns:
            Palauttaa luodun käyttäjän user -oliona, jos käyttäjänimi ja salasana kelpaavat.
            Muuten palauttaa None.
        """

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
        """Kirjaa käyttäjän sisään.

        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjän syöttämää käyttäjätunnusta
            password: Merkkijonoarvo, joka kuvaa käyttäjän syöttämää salasanaa

        Returns:
            Palauttaa käyttäjän user -oliona, jos käyttäjätunnus ja salasana täsmäävät.
            Muuten palauttaa False.
        """

        for user in self._users.get_all_users():
            if user.username == username:
                if user.password == password:
                    return user
        return False

    def add_new_activity(self, user: User, activity, date: datetime, duration: int):
        """Lisää uuden liikuntasuorituksen.

        Args:
            user: Kirjautunut käyttäjä User -oliona.
            activity: Merkkijonoarvo, joka kuvaa liikuntasuorituksen tyyppiä
            date: Päivämäärä -olio, joka kuvaa liikuntasuorituksen ajankohtaa
            duration: Kokonaislukuarvo, joka kuvaa liikuntasuorituksen kestoa minuuteissa
        """

        self._exercises.add_new_activity(user.username, activity, date, duration)

    def valid_activity(self, activity: str):
        """Tarkastaa, kelpaako liikuntasuoritusen kuvaus.

        Args:
            activity: Liikuntasuorutuksen kuvaus merkkijonona.

        Returns:
            Palauttaa True, jos kuvaus kelpaa. Muutoin palauttaa False.
        """

        if len(activity) <= 1:
            print("The name of activity is incomplete, please try again!")
            return False

        return True

    def valid_date(self, dateinput: str):
        """Tarkastaa, kelpaako päivämäärä.

        Args:
            dateinput: Päivämäärä merkkijonona.

        Returns:
            Palauttaa päivämääräolion, jos päivämäärä kelpaa. Muutoin palauttaa False.
        """

        try:
            parts = dateinput.split("-")
            date = datetime(int(parts[0]), int(parts[1]), int(parts[2]))
            return date
        except:
            print("Invalid date, please try again!")
            return False

    def valid_duration(self, hours, minutes):
        """Tarkastaa, kelpaako liikuntasuoritusen kesto.

        Args:
            hours: Liikuntasuorutuksen kesto tunteina.
            minutes: Liikuntasuorituksen kesto minuutteina.

        Returns:
            Palauttaa liikuntasuorituksen keston minuutteina, jos syötteet kelpaavat.
            Muutoin palauttaa False.
        """
        try:
            hours = int(hours)
            minutes = int(minutes)
            duration = 60*hours+minutes
            return duration
        except ValueError:
            print("Please, give hours and minutes numerically")
            return False

    def current_week(self, user: User):
        """Tulostaa käyttäjän kuluvan viikon liikuntasuoritukset.

        Args:
            user: User -olio, joka kuvaa kirjautunutta käyttäjää.
        """

        activities = self._exercises.current_week_activities_by_user(
            user.username)
        if user.weekly_target !="None" and user.weekly_target is not None:
            target=user.weekly_target
            print(f"Weekly target: You have done {len(activities)}/{target} exercises :)")
        if len(activities) > 0:
            print("")
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

    def get_all_activities(self, user: User):
        """Tulostaa yhteenvedon käyttäjän kaikista liikuntasuorituksista.

        Args:
            user: User -olio, joka kuvaa kirjautunutta käyttäjää.
        """

        activities = self._exercises.activities_by_user(user.username)
        total_duration=0
        activity_types={}

        if len(activities) > 0:

            for activity in activities:
                total_duration+=activity[4]
                if activity[2] not in activity_types:
                    how_many_times=1
                    duration=activity[4]
                    activity_types[activity[2]]=[how_many_times, duration]
                else:
                    activity_types[activity[2]][0]+=1
                    activity_types[activity[2]][1]+=activity[4]

            duration=self.get_duration_in_hours_and_minutes(total_duration)

            print(f"Number of activities added: {len(activities)}, total duration: {duration}")
            print("")

            for activity, data in activity_types.items():
                duration_in_total=self.get_duration_in_hours_and_minutes(data[1])
                print(f"{activity}: {data[0]} time(s), total duration: {duration_in_total}")

        else:
            print("No activities added.")

    def activities_by_date(self, user: User, datefrom: datetime, dateto: datetime):
        """Tulostaa käyttäjän liikuntasuoritukset tietyllä aikavälillä.

        Args:
            user: User -olio, joka kuvaa kirjautunutta käyttäjää.
            datefrom: Päivämäärä -olio, joka kuvaa päivämäärää, josta alkaen tiedot haetaan.
            dateto: Päivämäärä -olio, joka kuvaa päivämäärää, johon asti tiedot haetaan.
        """

        activities = self._exercises.activities_by_date(user.username, datefrom, dateto)

        if len(activities) > 0:
            date_from=self.get_date(str(datefrom))
            date_to=self.get_date(str(dateto))
            print("")
            print(f"Your activities from {date_from} to {date_to}: ")

            for activity in activities:
                duration=self.get_duration_in_hours_and_minutes(activity[4])
                date=self.get_date(activity[3])
                print(
                    f"Activity: {activity[2]}, date: {date}, duration: {duration}")
        else:
            print("No activities in the given time range")
            return

    def activities_by_activity(self, user: User, activity: str):
        """Tulostaa käyttäjän tietyn lajin liikuntasuoritukset.

        Args:
            user: User -olio, joka kuvaa kirjautunutta käyttäjää.
            activity: Merkkijono, joka kuvaa haettavaa liikuntalajia
        """

        activities=self._exercises.activities_by_activity(user.username, activity)

        total_duration=0

        if len(activities) > 0:

            for record in activities:
                total_duration+=record[4]

            duration=self.get_duration_in_hours_and_minutes(total_duration)

            print("")
            print(f"You have done activity '{activity}' {len(activities)} time(s).")
            print(f"Total duration: {duration}")
            print("")

            for record in activities:
                duration=self.get_duration_in_hours_and_minutes(record[4])
                date=self.get_date(record[3])
                print(f"Activity: {record[2]}, date: {date}, duration: {duration}")

        else:
            print(f"No activities named '{activity}' added.")
            return

    def get_duration_in_hours_and_minutes(self, duration: int):
        """Palauttaa liikuntasuorituksen keston tunteina ja minuutteina.

        Args:
            duration: Kokonaislukuarvo, joka kuvaa liikuntasuorituksen kestoa minuutteina.

        Returns:
            Palauttaa liikuntasuorituksen kestoa kuvaavan merkkijonon.
        """

        hours = int(duration/60)
        minutes = duration % 60
        if hours > 0 and minutes > 0:
            return f"{hours} h and {minutes} min"
        if hours > 0 and minutes == 0:
            return f"{hours} h"
        return f"{minutes} min"

    def get_date(self, date):
        """Palauttaa päivämäärän muodossa dd.mm.vvvv.

        Args:
            date: päivämäärä -olio

        Returns:
            Palauttaa liikuntasuorituksen päivämäärää kuvaavan merkkijonon muodossa dd.mm.vvvv.
        """

        parts = date.split("-")
        year = parts[0]
        month = parts[1]
        day = parts[2][0]+parts[2][1]
        return f"{day}.{month}.{year}"

    def add_target(self, user: User, target: str):
        """Lisää käyttäjälle viikottaisen liikuntatavoitteen.

        Args:
            user: User -olio, joka kuvaa kirjautunutta käyttäjää.
            target: kokonaislukuarvo, joka kuvaa tavoiteltavaa liikuntasuoritusten määrää.
        """

        try:
            target=int(target)

        except ValueError:
            print("Please, give target numerically")
            return
        if target>=0:
            user.set_target(target)
            print("Target added successfully.")
        else:
            print("Please, give positive target number")
            return
