# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/ohjelmistotekniikka-hy/python-todo-app/releases) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:
```bash
python3 -m pipenv install
```
Nyt ohjelman voi käynnistää komennolla:
```
python3 -m pipenv run start
```

## Matriisin koon valinta

Sovellus käynnistyy näkymään, jossa on kaksi 3x3 matriisia ja useita painikkeita joilla voi suorittaa laskutoimituksia. Matriisin kokoa muutetaan + ja - painikkeista 2x2 matriisin ollessa pienin sallittu ja isoin mahdollinen on matriisi on 7x7.

![Perusnäkymä](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/perusnakyma.jpg)



## Laskutoimitukset matriiseleilla

Täytä matriisiin arvot ja paina haluttua laskutoimitusta esittävää painiketta. Tulos näytetään Result matriisissa.

![Perustoiminnallisuus](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/perustoiminto.jpg)

## Matriisien vaihtaminen

Matriisien paikkoja voi vaihtaa keskenään "Flip"- painikkeesta. Myös laskusta saatu vastaus on mahdollista siirtää A tai B matriisiksi.
