# Ohjelmistotekniikka harjoitustyö

## ExerciseDiary

ExerciseDiary on Helsingin yliopiston Tietojenkäsittelytieteen kurssin *Ohjelmistotekniikka* harjoitustyö. 

Sovelluksen avulla käyttäjien on mahdollista pitää liikuntapäiväkirjaa, asettaa liikuntatavoitteita ja seurata näiden tavoitteiden toteutumista. Sovellusta voi käyttää useampi rekisteröitynyt käyttäjä, joilla on kaikilla oma yksilöllinen päiväkirjansa ja omat tavoitteet.

## Harjoitustyön dokumentaatio

[Vaatimusmäärittely](https://github.com/Kaabero/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/Kaabero/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/Kaabero/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/Kaabero/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[Viikon 5 release](https://github.com/Kaabero/ot-harjoitustyo/releases/tag/viikko5)
[Viikon 6 release](https://github.com/Kaabero/ot-harjoitustyo/releases/tag/viikko6)

## Python -versio

Suositellaan käytettäväksi vähintään Python-versiota 3.8.

## Asennus

- Aseta riippuvuudet komennolla: *poetry install*

- Käynnistä ohjelma komennolla: *poetry run invoke start*

## Komentorivikomennot

- Käynnistä ohjelma komennolla: *poetry run invoke start*

- Suorita testit komennolla: *poetry run invoke test*

- Luo testikattavuusraportti komennolla (raportti generoituu htmlcov-hakemistoon): *poetry run invoke coverage-report*

- Suorita tiedoston [.pylintrc](https://github.com/Kaabero/ot-harjoitustyo/blob/main/.pylintrc) määrittelemät tarkistukset komennolla: *poetry run invoke lint*






