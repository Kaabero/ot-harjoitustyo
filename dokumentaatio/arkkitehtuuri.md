# Luokkakaavio

```mermaid
 classDiagram
 
      Users ..> User
      ExerciseDatabase ..> User
      ExerciseApplication --> ExerciseService
      ExerciseService --> FileService
      ExerciseApplication ..> User
      ExerciseService --> Users
      ExerciseService --> ExerciseDatabase
      
      
      class ExerciseApplication {
        ExerciseService service
        User user
	login_instructions()
	execute()
	get_username_and_password()
	logged_in()
	logged_in_instructions()
	add_new_activity()
      }
      
      class ExerciseService {
        Users users
	ExerciseDatabase exercises
        FileService file
	save()
	create_user()
	login()
	current_week()
	add_target()
      }

      class Users {
        list users
        get_all_users()
        add_new_user()
      }

      class User {
        string username
        string password
        int weekly_target
        set_target()

      }
      class FileService {
        string file
        load()
        save()
      }
      class ExerciseDatabase {
        add_new_activity()
        activities_by_user()
        current_week_activities_by_user()
      }
     
```


# Sekvenssikaavio

Kun käyttäjä painaa ohjelman käynnistyksen jälkeen painiketta "2" kirjautuakseen sisään jo luoduilla käyttäjätunnuksilla, kirjautuminen etenee seuraavasti:

```mermaid
sequenceDiagram
  actor Person
  participant ExerciseApplication
  participant ExerciseService
  participant Users
  participant User
  Person->>ExerciseApplication: Press "2" button for login
  ExerciseApplication->>ExerciseService: login("Katri", "salasana")
  ExerciseService->>Users: get_all_users()
  Users->>User: username()
  User-->>Users: Katri
  Users->>User: password()
  User-->>Users: salasana
  Users-->>ExerciseService: user
  ExerciseService-->>ExerciseApplication: user
  ExerciseApplication->ExerciseApplication: logged_in(user)
```
