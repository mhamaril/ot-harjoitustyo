# Matriisilaskin

Sovelluksen avulla voi tehdä matriisien välisiä laskutoimituksia. Tällä hetkellä sillä ei voi laskea kuin 3x3 matriiseilla, mutta pyrin jatkokehittämään sovellusta niin että sillä pystyy laskemaan n x m kokoisia matriiseja kun n,m < 9. 

## Huomio Python-versiosta

Sovelluksen toiminta on testattu Python-versiolla `3.9.0`. Etenkin vanhempien Python-versioiden kanssa saattaa ilmentyä ongelmia.

## Dokumentaatio

[Vaativuusmäärittely](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/Vaativuusmaarittely.md)
[Arkkitehtuurikuvaus](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Tuntikirjanpito](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
python3 -m pipenv install
```

2. Käynnistä sovellus komennolla:

```bash
python3 -m pipenv run start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
python3 -m pipenv run start
```

### Testaus

Testit suoritetaan komennolla:

```bash
python3 -m pipenv run test
```

### Testikattavuus

Testikattavuus kerätään kommenolla:

```bash
python3 -m pipenv run coverage
```

Tämän jälkeen raportin voi generoida komennolla:

```bash
python3 -m pipenv run coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.
