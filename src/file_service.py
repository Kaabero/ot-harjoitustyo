class FileService():
    def __init__(self, file):
        self.__file=file
        with open(self.__file, "a") as tiedosto:
            pass

    def load(self):
        users={}
        with open(self.__file) as file:
            for row in file:
                parts = row.strip().split(";")
                users[parts[0]] = parts[1]

        return users
