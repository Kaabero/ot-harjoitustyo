import unittest
from exercise_application import ExerciseApplication
from user import User

class TestExerciseApplication(unittest.TestCase):
    def setUp(self):
        self.application=ExerciseApplication()
        user1=User("Eddy", "salasana1")
        self.application._users.add_new_user(user1)
        

    def test_create_user_if_user_already_exists(self):
        
        with self.assertRaises(ValueError):
            self.application.create_user("Eddy", "salasana2")

    def test_creating_new_user_returns_new_user(self):
        application=ExerciseApplication()
        
        self.assertEqual(application.create_user("Lily", "salasana1").username, "Lily")

    def test_creating_new_user_too_short_password(self):
        with self.assertRaises(ValueError):
            self.application.create_user("Eddy", "moi")
   