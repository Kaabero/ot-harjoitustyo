class FileService():
    def __init__(self, file):
        self._file = file
        with open(self._file, "a"):  # pylint: disable=unspecified-encoding
            pass

    def load(self):
        users = {}
        with open(self._file, encoding="utf-8") as file:
            for row in file:
                parts = row.strip().split(";")
                username, *data = parts
                users[username] = data

        return users

    def save(self, users: list):

        with open(self._file, "w", encoding="utf-8") as file:
            for user in users:
                file.write(f"{user.username};{user.password};{user.weekly_target}" + "\n")
                