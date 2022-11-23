import os
import sqlite3
from datetime import datetime

db = sqlite3.connect("activities.db")
db.isolation_level = None
        

class ExerciseDatabase():
    
    def __init__(self):

        # poistaa tietokannan alussa
        # os.remove("activities.db")
        try:
            db.execute("CREATE TABLE Activities (id INTEGER PRIMARY KEY, username TEXT, activity TEXT, date DATE, duration INTEGER)")
        except:
            return

    def add_new_activity(self, username, activity, date, duration):
        print(f"{username} {activity} {date} {duration}")
        activity = db.execute("INSERT INTO Activities (username, activity, date, duration) VALUES (?,?,?,?)", [username, activity, date, duration])
        print(db.execute("SELECT * FROM Activities").fetchall())
        return activity.lastrowid
        
    def activities_by_user(self, username):
        activities = db.execute("SELECT * FROM Activities").fetchall()
        return activities


        