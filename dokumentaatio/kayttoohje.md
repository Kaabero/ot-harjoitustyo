# Käyttöohje

Lataa projektin viimeisimmän releasen lähdekoodi valitsemalla _Assets_-osion alta _Source code_.:

- [Projektin releaset](https://github.com/Kaabero/ot-harjoitustyo/releases)

## Tietojen pysyväistallennus

Tietojen pysyväistallennus tapahtuu oletusarvoisesti seuraaviin tiedostoihin:

```
Käyttäjätietojen tallennus: users.txt

Liikuntasuoritusten tallennus: activities.db
```
Tiedostot luodaan automaattisesti käynnistyksen yhteydessä projektin juurihakemistoon, jos niitä ei siellä vielä ole.


## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet projektin juurihakemistossa komennolla:

```bash
poetry install
```

Käynnistä ohjelma komennolla:

```
poetry run invoke start
```

## Kirjautumisvalikko

Ohjelma käynnistyy valikkoon, josta voi valita haluaako luoda uuden käyttäjätunnuksen, kirjautua sisään vai lopettaa ohjelman.

### Kirjautuminen

Kirjautuminen onnistuu painamalla ohjeen mukaisesti painiketta "2" ja kirjoittamalla olemassaoleva käyttäjätunnus ja salasana syötekenttiin. Syötteet lähetetään painamalla "Enter" -näppäintä.

### Uuden käyttäjän luominen

Uuden käyttäjätunnuksen voi luoda painamalla ohjeen mukaisesti painiketta "1" ja kirjoittamalla uusi käyttäjätunnus ja salasana syötekenttiin.

Jos käyttäjän luominen onnistuu, siirrytään kirjautuneen käyttäjän toimintovalikkoon.

## Kirjautuneen käyttäjän toiminnot

Kirjautunut käyttäjä voi valita, haluaako lisätä liikuntasuorituksen, tarkastella kuluvan viikon liikuntasuorituksiaan, asettaa itselleen uuden tavoitteen, tarkastella tilastoja vai kirjautua ulos.

### Uuden liikuntasuorituksen lisääminen

Uuden liikuntasuorituksen voi lisätä painamalla ohjeen mukaisesti painiketta "1" ja kirjoittamalla liikuntasuorituksen tiedot syötekenttiin. Jos liikuntasuorituksen lisääminen onnistuu, ohjelma ilmoittaa tästä ja näkymässä palataan kirjautuneen käyttäjän valikkoon. Järjestelmä ilmoittaa, mikäli syötteet eivät kelpaa. 

### Kuluvan viikon liikuntasuoritusten tarkastelu

Kuluvan viikon liikuntasuorituksia voi tarkastella painamalla painiketta "2". Ohjelma listaa viikon suoritukset ja mikäli käyttäjä on asettanut itselleen tavoitteen, ohjelma näyttää tavoitteen täyttymisen tilanteen kuluvalla viikolla. Ohjelma palaa kirjautuneen käyttäjän valikkoon. 

### Tavoitteen asettaminen

Tavoitteen voi asettaa painamalla painiketta "3" ja antamalla tavoiteltavaa viikottaista liikuntamäärää kuvaavan kokonaisluvun syötekenttään. Järjestelmä ilmoittaa, mikäli syötteet eivät kelpaa. Jos tavoitteen lisääminen onnistuu, ohjelma ilmoittaa tästä ja näkymässä palataan kirjautuneen käyttäjän valikkoon.

### Tilastojen tarkastelu

Tilastoja voi tarkastella painamalla painiketta "4". Tämän jälkeen avautuu valikko, josta voi valita, mitä tietoja haluaa nähdä: Painamalla painiketta "1" voi tarkastella yhteenvetoa kaikista kirjautuneen käyttäjän liikuntasuorituksista, painamalla painiketta "2" voi hakea liikuntasuorituksia päivämäärien perusteella ja painamalla painiketta "3" voi hakea tietyn lajin kirjauksia. Ohjelma ilmoittaa, jos annetut syötteet eivät kelpaa. 

Toiminnon jälkeen palataan tilastovalikkoon. Tilastojen tarkastelun voi lopettaa painamalla painiketta "0", jolloin ohjelma palaa kirjautuneen käyttäjän valikkoon. 

## Lopetus

Ohjelman käytön voi lopettaa painamalla kirjautumisvalikossa tai kirjautuneen käyttäjän valikossa painiketta "0". 


