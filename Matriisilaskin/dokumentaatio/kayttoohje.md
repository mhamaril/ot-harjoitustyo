# Käyttöohje
PÄIVITÄ RELEASE
Lataa projektin viimeisimmän [releasen](https://github.com/ohjelmistotekniikka-hy/python-todo-app/releases) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Konfigurointi

Tallennukseen käytettävän tiedoston nimen voi halutessaan konfiguroida käynnistyshakemistossa _.env_-tiedostossa. Tiedosto luodaan automaattisesti _data_-hakemistoon, jos sitä ei siellä vielä ole. Tiedoston muoto on seuraava:
```bash
DATABASE_FILENAME=database.sqlite
```

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:
```bash
python3 -m pipenv install
```
Jonka jälkeen suorita alustustoimenpiteet komennolla:
```bash
python3 -m pipenv run build
```
Nyt ohjelman voi käynnistää komennolla:
```
python3 -m pipenv run start
```

## Matriisilaskurin versio

Sovellus käynnistyy rajoitettuun versioon, jossa on yksi 3x3 matriisi ja useita painikkeita joilla voi suorittaa laskutoimituksia. Vasemmalla alhaalla on "Full Version"- painike, josta pääsee kirjautumaan tai rekisteröitymään rajoittamattomaan versioon.

![](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/aloitusn%C3%A4kym%C3%A4.jpg)

## Kirjautuminen

"Full Version"- painikkeesta pääsee kirjautumisnäkymään:

![](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kirjautumisn%C3%A4kym%C3%A4.jpg)

Kirjautuminen onnistuu kirjoittamalla olemassa oleva käyttäjätunnus sekä oikea salasana syötekenttään ja painamalla "Login"- painiketta. Voi myös palata takaisin kirjautumatta "Limited Version"- painikkeesta.

![](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/luok%C3%A4ytt%C3%A4j%C3%A4n%C3%A4kym%C3%A4.jpg)

## Uuden käyttäjän luominen

Kirjautumisnäkymästä on mahdollista siirtyä uuden käyttäjän luomisnäkymään panikkeella "Create user".

Uusi käyttäjä luodaan syöttämällä tiedot syötekenttiin ja painamalla "Create"-painiketta:

![](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/luok%C3%A4ytt%C3%A4j%C3%A4n%C3%A4kym%C3%A4.jpg)

Jos käyttäjän luominen onnistuu, siirrytään täyden version näkymään.

![](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/fullversionn%C3%A4kym%C3%A4.jpg)

## Matriisin koon muuttaminen

Matriisin kokoa muutetaan + ja - painikkeista 2x2 matriisin ollessa pienin sallittu ja isoin mahdollinen on matriisi on 7x7.

![Perusnäkymä](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/fullversionn%C3%A4kym%C3%A4.jpg)


## Laskutoimitukset matriiseleilla

Täytä matriisiin arvot ja paina haluttua laskutoimitusta esittävää painiketta. Tulos näytetään Result matriisissa.

![Perustoiminnallisuus](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/laskutoimitusn%C3%A4kym%C3%A4.jpg)

## Matriisien vaihtaminen

Matriisien paikkoja voi vaihtaa keskenään "Flip"- painikkeesta. Myös laskusta saatu vastaus on mahdollista siirtää A tai B matriisiksi.
