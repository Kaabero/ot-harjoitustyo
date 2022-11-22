class FileService():
    def __init__(self, file):
        self.__file = file
        with open(self.__file, "a"):  # pylint: disable=unspecified-encoding
            pass

    def load(self):
        users = {}
        with open(self.__file, encoding="utf-8") as file:
            for row in file:
                parts = row.strip().split(";")
                users[parts[0]] = parts[1]

        return users

    def save(self, users: list):

        with open(self.__file, "w", encoding="utf-8") as file:
            for user in users:
                file.write(f"{user.username};{user.password}" + "\n")
