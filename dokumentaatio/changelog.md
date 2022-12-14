# Changelog

## Viikko 2

- Käyttäjä voi luoda uuden käyttäjätunnuksen
- Käyttäjä voi kirjautua sisään
- Lisätty ExerciseApplication -luokka, joka vastaa kommunikoinnista käyttäjän kanssa
- Lisätty User -luokka, joka vastaa yksittäisistä käyttäjistä
- Testattu, että jo olemassaolevan käyttäjätunnuksen luonti ei onnistu

## Viikko 3

- Lisätty Users -luokka, joka vastaa kaikista käyttäjistä
- Lisätty FileService -luokka, joka vastaa tiedostonkäsittelystä
- Käyttäjätunnusten ja salasanojen tallennus tiedostoon
- Testattu, että liian lyhyen salasanan asettaminen ei onnistu
- Testattu, että väärä salasana tai käyttäjätunnus kirjautuessa palauttaa False ja oikeat kirjautumistiedot True

## Viikko 4

- Lisätty ExerciseDatabase -luokka, joka vastaa liikuntasuorituksista ja niiden tallentamisesta
- Lisätty ExerciseDiary -luokka, joka vastaa kirjautuneen käyttäjän toiminnoista (poistettu myöhemmin)
- Käyttäjä voi kirjata uuden liikuntasuorituksen
- Testattu, että epäkelvot syötteet liikuntasuorituksen lisäämisessä palauttavat False
- Testattu, että oikein syötetty päivämäärä palauttaa päivämääräolion
- Testattu, että oikein syötetyt liikuntasuorituksen kestoa kuvaavat syötteet palauttavat keston minuuteissa
- Testattu, että liikuntasuorituksen onnistunut lisääminen tietokantaan palauttaa True
- Testattu, että tietyn käyttäjän kaikkien liikuntasuoritusten haku palauttaa tässä vaiheessa listan

## Viikko 5

- Käyttäjä voi nähdä kuluvan viikon liikuntasuorituksensa
- Käyttäjä voi asettaa itselleen viikottaisen liikuntatavoitteen
- Liikuntatavoite tallentuu samaan tiedostoon käyttäjänimen ja salasanan kanssa
- Testattu, että tavoitteen lisääminen asettaa tavoitteen arvon user -olion muuttujaan 

## Viikko 6

- Eriytetty käyttöliittymää ja sovelluslogiikkaa
- Luotu luokka ExerciseService, joka vastaa sovelluslogiikasta
- Korjattu testejä niin, etteivät testit kysy käyttäjältä syötteitä ja ovat automaattisia
- Käyttäjä voi hakea tilastot kaikista liikuntasuorituksistaan: eri lajien määrä ja kokonaiskesto
- Käyttäjä voi hakea liikuntasuorituksiaan päivämäärien tai lajin perusteella
- Testattu, että kelvolliset syötteet käyttäjää luodessa palauttavat käyttäjän
- Testattu, että liikuntasuorituksen keston muokkaus tunneiksi ja minuuteiksi toimii
- Testattu, että päivämäärän muokkaus muotoon dd.mm.vvvv toimii
- Testattu, että tavoitteen asettaminen epäkelvoilla syötteillä ei onnistu
- Testattu, ettei ohjelma palauta mitään, jos tilastoja hakee päivämäärillä, joiden sisällä ei ole kirjauksia
- Testattu, ettei ohjelma palauta mitään, jos tilastoja hakee liikuntalajilla, jolle ei ole tehty kirjauksia

## Viikko 7

- Testattu, että liikuntasuoritusten lisäys tietokantaan onnistuu
- Testattu, että liikuntasuoritusten haku tietokannasta kuluvalle viikolle toimii
- Testattu, että ohjelman lopetus aiheuttaa SystemExitin
- Testattu, ettei ohjelma palauta mitään, jos kuluvan viikon liikuntasuorituksia hakee, eikä viikolle ole lisätty aktiviteetteja 
- Testattu, ettei ohjelma palauta mitään, jos tilastoja haetaan kaikista liikuntasuorituksista, eikä kirjauksia ole vielä tehty
