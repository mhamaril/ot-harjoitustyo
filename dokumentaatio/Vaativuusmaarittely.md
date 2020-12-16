# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla voidaan tehdä erilaisia laskutoimituksia matriiseilla. Rekisteröitymällä saa sovellukseen käyttöönsä lisää ominaisuuksia.

## Käyttäjät

Sovellusta voi käyttää sekä kirjautuneena että kirjautumattomana käyttäjänä. Kirjautuneella käyttäjällä on ainoastaan yksi käyttäjärooli eli _normaali käyttäjä_.

## Käyttöliittymäluonnos

Sovellus koostuu neljästä eri näkymästä. Aloitusnäkymästä, kirjautumisnäkymästä, käyttäjänluontinäkymästä ja täysversionäkymästä.

![Aloitusnäkymä](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/aloitusn%C3%A4kym%C3%A4.jpg)

![Kirjautumisnäkymä](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/kirjautumisn%C3%A4kym%C3%A4.jpg)

![Käyttäjänluontinäkymä](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/luok%C3%A4ytt%C3%A4j%C3%A4n%C3%A4kym%C3%A4.jpg)

![Täysversionäkymä](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/fullversionn%C3%A4kym%C3%A4.jpg)

## Kirjautumattoman käyttäjän version tarjoama toiminnallisuus

- Käyttäjä voi luoda yhden 3 x 3 kokoisen matriisin
- Käyttäjä voi ottaa A matriisista determinantin, käänteismatriisin tai transpoosin
- Käyttäjä voi kertoa matriisin luvulla tai korottaa matriisin kokonaisluvulla potenssiin
- Käyttäjä voi tyhjätä matriisin "Clear"-napilla
- Saatu tulos näkyy sovelluksessa
- Käyttäjä voi siirtyä "Full Version"- napista reksiteröitymiseen/sisäänkirjautumiseen
- Käyttäjätunnuksen luonti
- Sisäänkirjautuminen

## Kirjautuneen käyttäjän version tarjoama toiminnallisuus

- Käyttäjä voi luoda yhden tai kaksi neliö matriisia joiden sivun pituus voi vaihdella kahdesta seitsemään
- Käyttäjä voi vaihtaa matriisien paikkoja keskenään
- Käyttäjä voi tehdä luoduilla matriiseilla kerto-, yhteen- ja vähennyslaskuja 
- Käyttäjä voi ottaa molemmista matriiseista determinantin, käänteismatriisin tai transpoosin
- Käyttäjä voi kertoa matriisin luvulla tai korottaa matriisin kokonaisluvulla potenssiin
- Käyttäjä voi tyhjätä matriisit "Clear"-napeilla
- Saatu tulos näkyy sovelluksessa
- Matriisin kokoa voi muuttaa + ja - napeista
- Tuloksen voi siirtää matriisin A ja/tai B paikalle
- Uloskirjautuminen "Logout"-napista


## Jatkokehitysideoita

Perusversion jälkeen sovellusta voisi kehittää esim. seuraavilla toiminnallisuuksilla:

- Lisätään mahdollisuus tehdä erikokoisia matriiseja esim. 3x4 matriiseja
- Lisätään mahdollisuus laskea yhtälöryhmillä eri laskutoimituksia, tämä lisäisi yhden näkymän lisää
- Pyritään kasvattamaan suurimman sallitun matriisin kokoa

