import unittest
from datetime import datetime
from services.exercise_service import ExerciseService
from users.user import User
from storages.file_service import FileService
from storages.exercise_database import ExerciseDatabase

class TestExerciseService(unittest.TestCase):
    def setUp(self):
        self.service = ExerciseService("test.txt")
        self.service.create_user("Eddy", "salasana1")

    def test_create_user_if_user_already_exists(self):

        self.assertEqual(self.service.create_user("Eddy", "salasana2"), None)

    def test_creating_new_user_too_short_password(self):
        self.assertEqual(self.service.create_user(
            "Katri", "moi"), None)

    def test_creating_new_user_too_short_username(self):
        self.assertEqual(self.service.create_user(
            "K", "salasana1"), None)

    def test_creating_new_user_with_correct_inputs_returns_user(self):
        self.assertEqual((self.service.create_user("Katri", "salasana")).username, "Katri")

    def test_login_return_true_with_correct_inputs(self):

        self.assertTrue(self.service.login(
            "Eddy", "salasana1"), "Test value is not true")

    def test_login_return_false_with_incorrect_password(self):

        self.assertFalse(self.service.login(
            "Eddy", "salasana2"), "Test value is not false")

    def test_login_return_false_with_incorrect_username(self):

        self.assertFalse(self.service.login(
            "Katri", "salasana1"), "Test value is not false")

    def test_invalid_activity_returns_false(self):
        self.assertFalse(self.service.valid_activity(
            "r"), "Test value is not false")

    def test_valid_activity_returns_true(self):
        self.assertTrue(self.service.valid_activity(
            "running"), "Test value is not true")

    def test_invalid_date_returns_false(self):
        self.assertFalse(self.service.valid_date(
            "2022-34-11"), "Test value is not false")

    def test_valid_date_returns_date(self):
        self.assertEqual(self.service.valid_date(
            "2022-11-25"), datetime(2022, 11, 25))

    def test_invalid_duration_inputs_returns_false(self):
        self.assertFalse(self.service.valid_duration(
            "1", ""), "Test value is not false")

    def test_valid_duration_returns_duration_in_minutes(self):
        self.assertEqual(self.service.valid_duration("1", "0"), 60)

    def test_adding_target_sets_weekly_target_for_user(self):
        user=User("Pertti", "salasana2")
        self.service.add_target(user, "3")
        self.assertEqual(user.weekly_target, 3)

    def test_adding_negative_target_returns_none(self):
        user=User("Pertti", "salasana2")
        self.service.add_target(user, "-1")
        self.assertEqual(user.weekly_target, None)

    def test_adding_alphabetical_target_returns_none(self):
        user=User("Pertti", "salasana2")
        self.service.add_target(user, "a")
        self.assertEqual(user.weekly_target, None)

    def test_getting_date_returns_formated_date(self):
        date=str(datetime(2022, 11, 30))
        self.assertEqual(self.service.get_date(date), "30.11.2022")

    def test_getting_duration_in_hours_and_minutes_returns_formated_duration(self):
        self.assertEqual(self.service.get_duration_in_hours_and_minutes(90), "1 h and 30 min")

    def test_getting_duration_in_hours_returns_formated_duration(self):
        self.assertEqual(self.service.get_duration_in_hours_and_minutes(60), "1 h")

    def test_getting_duration_in_minutes_returns_formated_duration(self):
        self.assertEqual(self.service.get_duration_in_hours_and_minutes(30), "30 min")

    def test_getting_activities_by_date_no_activities(self):
        user=User("Irmeli", "salasana2")
        
        self.assertEqual(self.service.activities_by_date(user, datetime.now(), datetime.now()), None)

    def test_getting_activities_by_activity_no_activities(self):
        user=User("Irmeli", "salasana2")
        
        self.assertEqual(self.service.activities_by_activity(user, "golf"), None)

    def test_getting_all_activities_no_activities(self):
        user=User("Irmeli", "salasana2")
        
        self.assertEqual(self.service.get_all_activities(user), None)

    def test_getting_current_week_no_activities(self):
        user=User("Irmeli", "salasana2")
        
        self.assertEqual(self.service.current_week(user), None)

    def test_exit_raises_system_exit(self):
        with self.assertRaises(SystemExit):
            self.service.exit()

    