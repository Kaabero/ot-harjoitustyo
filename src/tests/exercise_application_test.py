import unittest
from exercise_application import ExerciseApplication
from user import User
from file_service import FileService

class TestExerciseApplication(unittest.TestCase):
    def setUp(self):
        self.application=ExerciseApplication()
        self.application.create_user("Eddy", "salasana1")
         

    def test_create_user_if_user_already_exists(self):
        
        self.assertFalse(self.application.create_user("Eddy", "salasana2"), "Test value is not false")
      
    def test_creating_new_user_too_short_password(self):
        self.assertFalse(self.application.create_user("Katri", "moi"), "Test value is not false")

    def test_login_return_true_with_correct_inputs(self):
        
        self.assertTrue(self.application.login("Eddy", "salasana1"), "Test value is not true")

    def test_login_return_false_with_incorrect_password(self):
        
        self.assertFalse(self.application.login("Eddy", "salasana2"), "Test value is not false")

    def test_login_return_false_with_incorrect_username(self):
        
        self.assertFalse(self.application.login("Katri", "salasana1"), "Test value is not false")

    def test_login_sets_self_user(self):
        self.application.create_user("Katri", "salasana2")
        self.application.login("Katri", "salasana2")
        self.assertEqual((self.application._user).username, "Katri")

   