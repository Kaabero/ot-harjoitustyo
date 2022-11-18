import unittest
from exercise_application import ExerciseApplication
from user import User
from file_service import FileService

class TestExerciseApplication(unittest.TestCase):
    def setUp(self):
        self.application=ExerciseApplication()
            

    def test_create_user_if_user_already_exists(self):
        self.application.create_user("Eddy", "salasana1")
        
        self.assertFalse(self.application.create_user("Eddy", "salasana2"), "Test value is not false")
      

    def test_creating_new_user_too_short_password(self):
        self.assertFalse(self.application.create_user("Eddy", "moi"), "Test value is not false")
   