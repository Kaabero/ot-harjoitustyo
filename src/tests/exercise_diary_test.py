import unittest
from datetime import datetime
from user import User
from exercise_database import ExerciseDatabase
from exercise_diary import ExerciseDiary


class TestExerciseDiary(unittest.TestCase):
    def setUp(self):
        self._user=User("testi", "salasana1")
        self._exercisediary=ExerciseDiary(self._user)

    def test_adding_new_activity_returns_true(self):
        self.assertTrue(self._exercisediary._exercises.add_new_activity(self._user.username, "running", datetime.now(), 60), "Test value is not true")

    def test_invalid_activity_returns_false(self):
        self.assertFalse(self._exercisediary.valid_activity("r"), "Test value is not false")

    def test_valid_activity_returns_true(self):
        self.assertTrue(self._exercisediary.valid_activity("running"), "Test value is not true")

    def test_invalid_date_returns_false(self):
        self.assertFalse(self._exercisediary.valid_date("2022-34-11"), "Test value is not false")

    def test_valid_date_returns_date(self):
        self.assertEqual(self._exercisediary.valid_date("2022-11-25"), datetime(2022, 11, 25))

    def test_invalid_duration_inputs_returns_false(self):
        self.assertFalse(self._exercisediary.valid_duration("1",""), "Test value is not false")

    def test_valid_duration_returns_duration_in_minutes(self):
        self.assertEqual(self._exercisediary.valid_duration("1", "0"), 60)

    def test_getting_all_activities_returns_list(self):
        type1=type(self._exercisediary._exercises.activities_by_user(self._user.username))
        self.assertEqual(type1, list)


    def test_logout_raises_system_exit(self):
        with self.assertRaises(SystemExit):
            self._exercisediary.logout()

        

