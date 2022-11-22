import uuid
from datetime import datetime


class Activity:
    """Luokka, joka kuvaa yksittäistä liikuntasuoritusta

    Attributes:
        activity: merkkijonoarvo, joka kuvaa liikuntalajia
        date: Päivämäärä -olio, joka kuvaa suorituksen ajankohtaa
        duration: kokonaisluku, joka kuvaa suorituksen kestoa minuuteissa
        user: User-olio, joka kuvaa käyttäjää.
        activity_id: merkkijonoarvo, joka kuvaa tehtävän id:tä.
    """

    def __init__(self, activity: str, date: datetime, duration: int, user, activity_id=None):
        """Luokan konstruktori, joka luo uuden liikuntasuorituksen.
        Args:
            activity: merkkijonoarvo, joka kuvaa liikuntalajia
            date: Päivämäärä -olio, joka kuvaa suorituksen ajankohtaa
            duration: kokonaisluku, joka kuvaa suorituksen kestoa minuuteissa
            user: User-olio, joka kuvaa käyttäjää.
            activity_id:
                Vapaaehtoinen, oletusarvoltaan generoitu uuid.
                Merkkijonoarvo, joka kuvaa tehtävän id:tä.
        """

        self.activity = activity
        self.date = date
        self.duration = duration
        self.user = user
        self.id = activity_id or str(uuid.uuid4())
