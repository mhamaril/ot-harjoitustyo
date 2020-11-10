# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla voidaan tehdä erilaisia laskutoimituksia matriiseilla. Sovellus ei vaadi rekisteröitymistä.

## Käyttäjät

Sovelluksella ei ole erillisiä käyttäjärooleja, ainoastaan yksi käyttäjärooli eli _normaali käyttäjä_.

## Käyttöliittymäluonnos

Sovellus koostuu yhdestä näkymästä

![](./dokumentaatio/kayttoliittymaluonnos.jpg)

Sovellus aukeaa perusnäkymään, jossa on mahdollista tehdä erilaisia laskutoimituksia matriiseilla.

## Perusversion tarjoama toiminnallisuus

- Käyttäjä voi luoda yhden tai kaksi n x n kokoista matriisia, missä n < 6
	- Matriisin kokoa voi muuttaa "+" ja "-" napeista
- Käyttäjä voi tehdä kerto-, yhteen- ja vähennyslaskuja matriiseilla
- Saatu tulos näkyy result laatikossa

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:

- Lisätään muita matriisien laskutoimituksia, kuten esimerkiksi determinantin tai käänteismatriisin laskeminen
- Lisätään mahdollisuus tehdä erikokoisia matriiseja esim. 3x4 matriiseja
	- Tästä seuraa että sovelluksen on tarkistettava voiko laskutoimituksia suorittaa
- Pyritään kasvattamaan suurimman sallitun matriisin kokoa
- Lisätään mahdollisuus laskea saadulla tuloksella uusia laskutoimituksia
