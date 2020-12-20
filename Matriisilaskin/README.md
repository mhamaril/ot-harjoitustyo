# Matriisilaskin

Sovelluksen avulla voi tehdä matriisien välisiä laskutoimituksia. Kirjautuneena sillä voi laskea kahdella neliömatriisilla, joiden sivun pituus on kahdesta seitsemään. Kirjautumattomassa versiossa voi laskea ainoastaan yhdellä 3x3-kokoisella matriisilla.

## Huomio Python-versiosta

Sovelluksen toiminta on testattu Python-versiolla `3.9.0`. Etenkin vanhempien Python-versioiden kanssa saattaa ilmentyä ongelmia.

## Versiot

[Toinen release](https://github.com/mhamaril/ot-harjoitustyo/releases/tag/viikko6)

## Dokumentaatio

[Käyttöohje](https://github.com/mhamaril/ot-harjoitustyo/blob/master/Matriisilaskin/dokumentaatio/kayttoohje.md)

[Vaativuusmäärittely](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/Vaativuusmaarittely.md)

[Arkkitehtuurikuvaus](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/mhamaril/ot-harjoitustyo/blob/master/Matriisilaskin/dokumentaatio/testaus.md)

[Tuntikirjanpito](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Asenna riippuvuut komennolla:

```bash
python3 -m pipenv install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
python3 -m pipenv run build
```

3. Käynnistä sovellus komennolla:

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

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
python3 -m pipenv run lint
```
