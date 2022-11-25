# Luokkakaavio

```mermaid
 classDiagram
      ExerciseApplication --> FileService
      ExerciseApplication --> Users
      ExerciseApplication --> ExerciseDiary
      ExerciseApplication "1" --> "*" User
      Users ..> User
      ExerciseDatabase ..> User
      ExerciseDiary "1" --> "*" User
      ExerciseDiary --> ExerciseDatabase
      
      class ExerciseDiary {
        User user
        ExerciseDatabase exercises
        start()
        logged_in_instructions()
        add_new_activity()
        valid_activity()
        valid_date()
        valid_duration()
        get_all_activities()
        logout()
      }
        
      class ExerciseApplication {
        Users users
        FileService file
        User user
        login_instructions()
        execute()
        create_user()
        login()
        finish()
        logged_in()

      }

      class Users {
        list users
        get_all_users()
        add_new_user()
      }

      class User {
        string username
        string password
      }
      class FileService {
        string file
        load()
        save()
      }
      class ExerciseDatabase {
        add_new_activity()
        activities_by_user()
      }
     
```
