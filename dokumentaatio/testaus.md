# Testausdokumentti

Ohjelman yksikkö- ja integraatiotestit ovat automaattisia ja ne on testattu unittestilla.  Ohjelmaa on testattu myös järjestelmätasolla manuaalisesti. 

## Yksikkö- ja integraatiotestaus unittestilla

Suurin osa testeistä testaa sovelluslogiikasta vastaavaa ExerciseServise -luokkaa ja nämä testit on koottu [TestExerciseService](https://github.com/Kaabero/ot-harjoitustyo/blob/main/src/tests/exercise_service_test.py) -testiluokkaan. Testiluokassa alustetaan ExerciseService -olio parametrilla "test.txt", jolloin alustusmetodissa luotu käyttäjä tallentuu "test.txt" -nimiseen tiedostoon. 

Testeissä testataan myös tietokantaoperaatioista vastaavaa ExerciseDatabase -luokkaa [TestExerciseDatabase](https://github.com/Kaabero/ot-harjoitustyo/blob/main/src/tests/exercise_database_test.py) -testiluokalla. Mikäli testeissä lisätään yksi tai useampi uusi rivi tietokantatauluun, se myös poistetaan testimetodissa. 

### Testauskattavuus

Ohjelman testauksen haarautumiskattavuus on 77 %. Käyttöliittymään ja testeihin liittyvä koodi on jätetty testikattavuusraportin ulkopuolle.

![](https://github.com/Kaabero/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/Coverage%20report.png)

Testaatamatta jäi joitain osia ExerciseServise -luokan metodeista. Testaamatta jäi erityisesti tilanteita, joissa ohjelma tulostaa käyttäjälle tilastoja tämän liikuntasuorituksista. 

## Järjestelmätestaus

Ohjelmaa on testattu myös järjestelmätasolla manuaalisesti. Testauksessa on seurattu [käyttöohjeen](https://github.com/Kaabero/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md) ohjeita ja tämä on tehty sekä macOS- että Linux-ympäristössä. 

### Toiminnallisuudet

Kaikki [vaatimusmäärittelyssä](https://github.com/Kaabero/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md) kuvatut toiminnallisuudet on testattu manuaalisesti ja testauksen yhteydessä on pyritty antamaan myös mahdollisimman kattavasti virheellisiä syötteitä.

## Ohjelmaan jääneitä laatuongelmia

Ohjelman tiedostojen nimet annetaan ohjelman sisällä. Ohjelman toimivuus ei ole taattu tilanteissa, joissa tämän nimiset tiedostot on jo olemassa ja niissä on jo valmiiksi sisältöä, joita ohjelma itse ei ole luonut. 

