# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjien on mahdollista pitää liikuntapäiväkirjaa, 
asettaa liikuntatavoitteita ja seurata näiden tavoitteiden toteutumista. 
Sovellusta voi käyttää useampi rekisteröitynyt käyttäjä, joilla on 
kaikilla oma yksilöllinen päiväkirjansa ja omat tavoitteet.

## Käyttäjät

Sovelluksella on ainoastaan yksi käyttäjärooli eli *normaali* käyttäjä. 

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen
	- Käyttäjätunnuksen on oltava uniikki
- Käyttäjä voi kirjautua järjestelmään 
	- Kirjautuminen onnistuu syötettäessä olemassaoleva käyttäjätunnus 
ja salasana 
	- Jos käyttäjätunnus tai salasana ovat väärin, järjestelmä 
ilmoittaa tästä

### Kirjautumisen jälkeen

- Käyttäjä näkee kuluvan viikon liikuntasuorituksensa
- Käyttäjä voi kirjata uuden liikuntasuorituksen tietoineen
	- Käyttäjä kirjaa liikuntalajin, keston, päivämäärän, rankkuusasteen annetulla 
asteikolla ja fiilksen annetulla asteikolla 
- Käyttäjä voi kirjautua ulos istunnosta

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla 
toiminnallisuuksilla:

- Käyttäjä voi asettaa itselleen viikottaisen liikuntatavoitteen keston tai liikuntamäärän 
perusteella
- Kirjautumisen jälkeen käyttäjä näkee viikottaisen liikuntasuorituksensa lisäksi tavoitteensa 
täyttymisen tilanteen kuluvalla viikolla
- Käyttäjä voi hakea tilastoja päivämäärien, lajien, rankkuusasteen ja fiilisasteen 
perusteella (eri lajien suorituskertojen määrä ja 
kesto tiettynä ajanjaksona)
- Käyttäjä voi poistaa liikuntasuorituksen
  
