import unittest
from datetime import datetime
from services.exercise_service import ExerciseService
from users.user import User
from storages.file_service import FileService
from storages.exercise_database import ExerciseDatabase

class TestExerciseDatabase(unittest.TestCase):
    def setUp(self):
        self.service = ExerciseService("test.txt")

    def test_adding_new_activity_returns_true(self):
        user=User("Hanna", "salasana2")
        add=self.service._exercises.add_new_activity(user.username, "running", datetime.now(), 60)
        self.assertTrue(add, "Test value is not true")
        self.service._exercises.delete(add)

    def test_getting_all_activities_returns_list(self):
        user=User("Pertti", "salasana2")
        type1 = type(self.service._exercises.activities_by_user(user.username))
        self.assertEqual(type1, list)

    def test_adding_new_activity_adds_activity_to_database(self):
        user=User("Hanna", "salasana2")
        date=datetime(2022, 12, 14, 00, 00)
        add=self.service._exercises.add_new_activity(user.username, "running", date, 60)
        self.assertEqual((self.service._exercises.search_by_id(add)), [(add, user.username, "running", '2022-12-14 00:00:00', 60)])
        self.service._exercises.delete(add)

    def test_current_week_activities_returns_current_week_activities_for_user(self):
        user=User("Hanna", "salasana2")
        add=self.service._exercises.add_new_activity(user.username, "running", datetime.now(), 60)
        add2=self.service._exercises.add_new_activity("Eddy", "running", datetime.now(), 60)
        self.assertEqual((self.service._exercises.current_week_activities_by_user(user.username))[0][0], add)
        self.assertEqual((self.service._exercises.current_week_activities_by_user("Eddy"))[0][0], add2)
        self.service._exercises.delete(add)
        self.service._exercises.delete(add2)