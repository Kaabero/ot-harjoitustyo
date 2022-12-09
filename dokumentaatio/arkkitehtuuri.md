# Arkkitehtuurikuvaus

Sovelluksen kaikki koodi on samassa hakemistossa.  

## Luokkakaavio

Luokka ExerciseApplication vastaa käyttäjän kanssa kommunikoinnista ja luokka ExerciseService sovelluslogiikasta. Luokka ExerciseDatabase vastaa liikuntasuoritusten tallentamisesta tietokantaan ja liikuntasuorituksiin liittyvistä tietokantaoperaatioista. Luokka FileService vastaa tiedostonkäsittelystä eli käyttäjätietojen tallennuksesta tiedostoon ja näiden hakemisesta tiedostosta. Luokka User kuvaa yksittäistä käyttäjää ja luokka Users kuvaa kaikkia käyttäjiä.


```mermaid
 classDiagram
 
      Users ..> User
      ExerciseApplication --> ExerciseService
      ExerciseService --> FileService
      ExerciseService ..> User
      ExerciseApplication --> User
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
	stats()
	exit()
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
	get_all_activities()
	activities_by_date()
	activities_by_activity()
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
	activities_by_date()
	activities_by_activity()
      }
     
```
## Käyttöliittymä

Luokka ExerciseApplication vastaa kaikesta kommunikoinnista käyttäjän kanssa. Käyttöliittymä sisältää kaksi eri tilaa, joissa käyttäjä voi valita toimintonsa:

- Aloitustila, jossa käyttäjä valitsee haluaako luoda uuden käyttäjätunnuksen, kirjautua sisään vai lopettaa sovelluksen käytön.
- Kirjautumistila, jossa käyttäjä valitsee, haluaako lisätä liikuntasuorituksen, nähdä viikottaiset suorituksensa, asettaa tavoitteen, nähdä tilastoja vai kirjautua ulos. Tilastojen katselu avaa oman tilansa, jossa käyttäjä voi hakea tilastoja eri tavoin. 

Käyttöliittymä kysyy käyttäjältä tarvittavia tietoja ja toteuttaa toiminnot kutsumalla ExerciseService -luokan metodeja.

## Sovelluslogiikka

Sovelluksen luokka Users kuvaa kaikkia käyttäjiä, luokka User kuvaa yskittäistä käyttäjää ja luokka ExerciseDatabase vastaa kaikkien käyttäjien liikuntasuoritusten tallennuksesta tietokantaan ja tietokantaoperaatioista. Toiminnallisuuksista näiden välillä vastaa luokan ExerciseService olio, joka sisältää metodit käyttöliittymän toiminnoille. Näitä metodeja ovat esimerkiksi: 

create_user(username, password)
login(username, password)
current_week(user)
get_all_activities(user)
add_target(user, target)


## Sekvenssikaavio

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
