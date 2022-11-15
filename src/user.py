class User:
    """Luokka, joka kuvaa yksittäistä käyttäjää.
    Attributes:
        username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta.
        password: Merkkijonoarvo, joka kuvaa käyttäjän salasanaa.
        activities: Lista, joka pitää kirjaa käyttäjän lajeista
    """

    def __init__(self, username, password):
        """Luokan konstruktori, joka luo uuden käyttäjän.
        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa käyttäjän salasanaa.
            activities: Lista, joka pitää kirjaa käyttäjän lajeista.
        """

        self.username = username
        self.password = password
        self.activities = []

        