class FileService():
    """Käyttäjätietojen tallennuksesta vastaava luokka."""

    def __init__(self, file):
        """Luokan konstruktori.

        Args:
            file: Merkkijonoarvo, joka kuvaa tiedoston nimeä, johon tiedot tallennetaan.
        """

        self._file = file
        with open(self._file, "a"):  # pylint: disable=unspecified-encoding
            pass

    def load(self):
        """Lataa tiedostossa olevat tiedot ja vie ne sanakirjaan.

        Returns:
            Palauttaa käyttäjien tiedot sanakirjana.
        """

        users = {}
        with open(self._file, encoding="utf-8") as file:
            for row in file:
                parts = row.strip().split(";")
                username, *data = parts
                users[username] = data

        return users

    def save(self, users: list):
        """Tallentaa käyttäjien tiedot tiedostoon.

        Args:
            users: Lista käyttäjiestä user -olioina, joiden tiedot tallennetaan tiedostoon.
        """
        with open(self._file, "w", encoding="utf-8") as file:
            for user in users:
                file.write(f"{user.username};{user.password};{user.weekly_target}" + "\n")
                