
from user import User


class Users():
    """Luokka, joka kuvaa kaikkia käyttäjiä."""

    def __init__(self):
        """Luokan kontruktori."""

        self._users = []

    def get_all_users(self):
        """Palauttaa kaikki käyttäjät."""
        return self._users

    def add_new_user(self, user: User):
        """Lisää uuden käyttäjän käyttäjälistaan.

        Args:
            user: Lisättävää käyttäjää kuvaava User -olio.
        """

        self._users.append(user)
