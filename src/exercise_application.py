
from user import User
from activity import Activity
from users import Users

class ExerciseApplication():
    #Sovelluslogiikasta vastaava luokka
    
    def __init__(self):
        self._users=Users()
        self.user=None
    

    def login_instructions(self):
        print("Commands: ")
        print("0 Finish")
        print("1 Create new user")
        print("2 Login")

    def execute(self):
        self.login_instructions()
        while True:
            print("")
            command=input("Command: ")
            if command == "0":
                break
            elif command == "1":
                while True:
                    username = input("Username: ")
                    password = input("Password: ")
                    
                    self.create_user(username, password)
                    break

            elif command == "2":
                if self.login():
                    print("Login -toiminnot")
                    break
                else:
                    print("Invalid username or password")
                    continue
            else:
                self.login_instructions()

    def create_user(self, username, password):

        #Luo uuden käyttäjän ja kirjaa käyttäjän sisään.

        for user in self._users.get_all_users():
            if user.username == username:
                raise ValueError (f"Username {username} already exists")

        if len(password)<8:
                raise ValueError ("Minimum password length is eight characters. Please try again.")

        user=User(username, password)
        self._users.add_new_user(user)

        self_user=user
        return user


    def login(self):

        #Kirjaa käyttäjän sisään
        
        username = input("Username: ")
        password = input("Password: ")


        for user in self._users.get_all_users():
            if user.username == username:
                if user.password == password:
                    self_user=user
                    print("Login successfully!")
                    return True

        return False

    def logout(self):
        #Kirjaa nykyisen käyttäjän ulos.
        self._user = None
        

    def add_new_activity(self):
        pass
    


