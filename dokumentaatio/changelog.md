# Changelog

## Viikko 2

- Käyttäjä voi luoda uuden käyttäjätunnuksen
- Käyttäjä voi kirjautua sisään
- Lisätty ExerciseApplication -luokka, joka vastaa kommunikoinnista käyttäjän kanssa ennen kirjautumista
- Lisätty User -luokka, joka vastaa yksittäisistä käyttäjistä
- Testattu, että jo olemassaolevan käyttäjätunnuksen luonti ei onnistu

## Viikko 3

- Lisätty Users -luokka, joka vastaa kaikista käyttäjistä
- Lisätty FileService -luokka, joka vastaa tiedostonkäsittelystä
- Käyttäjätunnusten ja salasanojen tallennus tiedostoon
- Testattu, että liian lyhyen salasanan asettaminen ei onnistu ja palauttaa False
- Testattu, että väärä salasana tai käyttäjätunnus kirjautuessa palauttaa False ja oikeat kirjautumistiedot True

## Viikko 4

- Lisätty ExerciseDatabase -luokka, joka vastaa liikuntasuorituksista ja niiden tallentamisesta
- Lisätty ExerciseDiary -luokka, joka vastaa kirjautuneen käyttäjän toiminnoista
- Käyttäjä voi kirjata uuden liikuntasuorituksen
- Testattu, että epäkelvot syötteet liikuntasuorituksen lisäämisessä palauttavat False
- Testattu, että oikein syötetty päivämäärä palauttaa päivämääräolion
- Testattu, että oikein syötetyt liikuntasuorituksen kestoa kuvaavat syötteet palauttavat keston minuuteissa
- Testattu, että liikuntasuorituksen onnistunut lisääminen tietokantaan palauttaa True
- Testattu, että tietyn käyttäjän kaikkien liikuntasuoritusten haku palauttaa tässä vaiheessa listan
- Testattu, että sys.exit() toimii

