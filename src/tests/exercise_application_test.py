import unittest
from datetime import datetime
from exercise_application import ExerciseApplication
from user import User
from file_service import FileService
from exercise_database import ExerciseDatabase


class TestExerciseApplication(unittest.TestCase):
    def setUp(self):
        self.application = ExerciseApplication("test.txt")
        self.application.create_user("Eddy", "salasana1")

    def test_create_user_if_user_already_exists(self):

        self.assertFalse(self.application.create_user("Eddy", "salasana2"), "Test value is not false")

    def test_creating_new_user_too_short_password(self):
        self.assertFalse(self.application.create_user(
            "Katri", "moi"), "Test value is not false")

    def test_creating_new_user_too_short_username(self):
        self.assertFalse(self.application.create_user(
            "K", "salasana1"), "Test value is not false")

    def test_login_return_true_with_correct_inputs(self):

        self.assertTrue(self.application.login(
            "Eddy", "salasana1"), "Test value is not true")

    def test_login_return_false_with_incorrect_password(self):

        self.assertFalse(self.application.login(
            "Eddy", "salasana2"), "Test value is not false")

    def test_login_return_false_with_incorrect_username(self):

        self.assertFalse(self.application.login(
            "Katri", "salasana1"), "Test value is not false")

    def test_adding_new_activity_returns_true(self):
        user=User("Pertti", "salasana2")
        self.assertTrue(self.application._exercises.add_new_activity(user.username, "running", datetime.now(), 60), "Test value is not true")

    def test_invalid_activity_returns_false(self):
        self.assertFalse(self.application.valid_activity(
            "r"), "Test value is not false")

    def test_valid_activity_returns_true(self):
        self.assertTrue(self.application.valid_activity(
            "running"), "Test value is not true")

    def test_invalid_date_returns_false(self):
        self.assertFalse(self.application.valid_date(
            "2022-34-11"), "Test value is not false")

    def test_valid_date_returns_date(self):
        self.assertEqual(self.application.valid_date(
            "2022-11-25"), datetime(2022, 11, 25))

    def test_invalid_duration_inputs_returns_false(self):
        self.assertFalse(self.application.valid_duration(
            "1", ""), "Test value is not false")

    def test_valid_duration_returns_duration_in_minutes(self):
        self.assertEqual(self.application.valid_duration("1", "0"), 60)

    def test_getting_all_activities_returns_list(self):
        user=User("Pertti", "salasana2")
        type1 = type(self.application._exercises.activities_by_user(
            user.username))
        self.assertEqual(type1, list)

    def test_adding_target_sets_weekly_target_for_user(self):
        user=User("Pertti", "salasana2")
        self.application._user=user
        self.application._user.set_target(3)
        self.assertEqual(user.weekly_target, 3)

    