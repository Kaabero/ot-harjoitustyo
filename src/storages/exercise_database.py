import sqlite3
from datetime import datetime
from datetime import timedelta


db = sqlite3.connect("activities.db")
db.isolation_level = None


class ExerciseDatabase():
    """Vastaa liikuntasuoritusten tallentamisesta tietokantaan
    ja liikuntasuorituksiin liittyvistä tietokantaoperaatioista.
    """

    def __init__(self):
        """Luokan konstruktori."""

        try:
            db.execute("CREATE TABLE Activities (id INTEGER PRIMARY KEY, username TEXT, \
            activity TEXT, date DATE, duration INTEGER)")
        except:
            return

    def add_new_activity(self, username, activity, date: datetime, duration):
        """Lisää uuden liikuntasuorituksen tietokantaan.

        Args:
            username: Kirjautuneen käyttäjän käyttäjätunnus merkkijonona.
            activity: Merkkijonoarvo, joka kuvaa liikuntasuorituksen tyyppiä
            date: Päivämäärä -olio, joka kuvaa liikuntasuorituksen ajankohtaa
            duration: Kokonaislukuarvo, joka kuvaa liikuntasuorituksen kestoa minuuteissa

        Returns:
            Palauttaa True, kun liikuntasuoritus on lisätty tietokantaan
        """

        activity = db.execute("INSERT INTO Activities (username, activity, date, \
        duration) VALUES (?,?,?,?)", [username, activity, date, duration])
        return True

    def activities_by_user(self, username):
        """Palauttaa kaikki käyttäjän liikuntasuoritukset.

        Args:
            username: Käyttäjä, jonka suoritukset haetaan tietokannasta

        Returns:
            Palauttaa listan käyttäjän liikuntasuorituksista
        """

        activities = db.execute(
            "SELECT * FROM Activities WHERE username=?", [username]).fetchall()
        return activities

    def current_week_activities_by_user(self, username):
        """Palauttaa kaikki käyttäjän liikuntasuoritukset kuluvalta viikolta.

        Args:
            username: Käyttäjä, jonka suoritukset haetaan tietokannasta

        Returns:
            Palauttaa listan käyttäjän liikuntasuorituksista kuluvalla viikolla.
        """

        activities = db.execute("SELECT * FROM Activities WHERE username=? AND date BETWEEN \
        ? AND ? ORDER BY date", [username, get_monday_midnight(), datetime.now()]).fetchall()
        return activities

    def activities_by_date(self, username, datefrom: datetime, dateto: datetime):
        """Palauttaa kaikki käyttäjän liikuntasuoritukset kuluvalta viikolta.

        Args:
            username: Käyttäjä, jonka suoritukset haetaan tietokannasta
            datefrom: Päivämäärä -olio, joka kuvaa päivämäärää, josta alkaen tiedot haetaan.
            dateto: Päivämäärä -olio, joka kuvaa päivämäärää, johon asti tiedot haetaan.

        Returns:
            Palauttaa listan käyttäjän liikuntasuorituksista annetulla aikavälillä.
        """
        activities = db.execute("SELECT * FROM Activities WHERE username=? AND date BETWEEN \
        ? AND ? ORDER BY date", [username, datefrom, dateto]).fetchall()
        return activities

    def activities_by_activity(self, username, activity):
        """Palauttaa kaikki käyttäjän tietyn liikuntalajin liikuntasuoritukset.

        Args:
            username: Käyttäjä, jonka suoritukset haetaan tietokannasta
            activity: Merkkijono, joka kuvaa haettavaa liikuntalajia

        Returns:
            Palauttaa listan käyttäjän kyseisen lajin liikuntasuorituksista.
        """
        activities = db.execute("SELECT * FROM Activities WHERE username=? \
        AND activity = ? ORDER BY date", [username, activity]).fetchall()
        return activities

def get_monday_midnight():
    """Palauttaa kuluvan viikon maanantain keskiyön päivämäärä -oliona."""

    today = datetime.now()
    day_of_week = today.isoweekday()
    monday = today-timedelta(days=day_of_week-1)
    monday_midnight = datetime(monday.year, monday.month, monday.day)
    return monday_midnight
