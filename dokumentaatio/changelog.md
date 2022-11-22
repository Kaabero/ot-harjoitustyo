# Changelog

## Viikko 2

- Käyttäjä voi luoda uuden käyttäjätunnuksen
- Käyttäjä voi kirjautua sisään
- Lisätty ExerciseApplication -luokka, joka vastaa sovelluslogiikasta
- Lisätty User -luokka, joka vastaa yksittäisistä käyttäjistä
- Lisätty Activity -luokka, joka vastaa yksittäisistä liikuntasuorituksista
- Testattu, että jo olemassaolevan käyttäjätunnuksen luonti ei onnistu

## Viikko 3

- Lisätty Users -luokka, joka vastaa kaikista käyttäjistä
- Lisätty FileService -luokka, joka vastaa tiedostonkäsittelystä
- Käyttäjätunnusten ja salasanojen tallennus tiedostoon
- Testattu, että liian lyhyen salasanan asettaminen ei onnistu ja palauttaa False
- Testattu, että väärä salasana tai käyttäjätunnus kirjautuessa palauttaa False ja oikeat kirjautumistiedot True
- Testattu, että sisäänkirjautuminen asettaa kirjautuneen käyttäjän käyttäjäksi

