import os # pylint: disable=unused-import
import sqlite3
from datetime import datetime


# poistaa tietokannan alussa
#os.remove("activities.db")

db = sqlite3.connect("activities.db")
db.isolation_level = None


class ExerciseDatabase():

    def __init__(self):

        try:
            db.execute(
                "CREATE TABLE Activities (id INTEGER PRIMARY KEY, username TEXT, activity TEXT, \
                date DATE, duration INTEGER)")
        except BaseException:
            return

    def add_new_activity(self, username, activity, date: datetime, duration):
        activity = db.execute("INSERT INTO Activities (username, activity, date, \
        duration) VALUES (?,?,?,?)", [username, activity, date, duration])
        return True

    def activities_by_user(self, username):
        activities = db.execute("SELECT * FROM Activities WHERE username=?", [username]).fetchall()
        return activities
