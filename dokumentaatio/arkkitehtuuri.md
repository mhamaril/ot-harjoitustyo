# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattelee kaksitasoista kerrosarkkitehtuuria, ja koodin pakkausrakenne on seuraava:

![Pakkausrakenne](./kuvat/arkkitehtuuri-pakkaus.png)

Pakkaus _gui_ sisältää käyttöliittymästä ja _services_ sovelluslogiikasta vastaavan koodin.

## Käyttöliittymä

Käyttöliittymä sisältää tällä hetkellä yhden näkymän:

- Päänäkymä, missä voi tehdä matriiseilla laskutoimituksia
- Aloitusnäkymä, jota ei vielä ole, missä valitaan matriisien koot

Jokainen näistä toteutetaan omana luokkanaan. Näkymistä yksi on aina kerrallaan näkyvänä. Näkymien näyttämisestä vastaa [GUI](../src/gui/gui.py)-luokka. Käyttöliittymä on pyritty eristämään täysin sovelluslogiikasta. Se ainoastaan kutsuu [MatrixService](../src/services/matrix_service.py)-luokan metodeja.

## Sovelluslogiikka

Toiminnallisista kokonaisuuksista vastaa luokka [MatrixService](../src/services/matrix_service.py) joka on ainoa olio. Luokka tarjoaa kaikille käyttäliittymän toiminnoille oman metodin. Näitä ovat esimerkiksi:

- `transpose_matrix_a()`
- `determinant_matrix_a()`
- `inverse_matrix_b()`
- `power_of_matrix_a()`

`MatrixService`-luokan ja ohjelman muiden osien suhdetta kuvaava luokka/pakkauskaavio:

![Pakkausrakenne ja luokat](./kuvat/arkkitehtuuri-pakkaus-luokat.png)

## Päätoiminnallisuudet

Kuvataan seuraavaksi sovelluksen toimintalogiikka muutaman päätoiminnallisuuden osalta sekvenssikaaviona.

### Syötteiden kirjaaminen sekä laskutoimitus

![](./kuvat/sekvenssi-kirjautuminen.png)

Painikkeen painamiseen reagoiva [tapahtumankäsittelijä](../src/gui/main_view.py#L90) kutsuu aluksi käyttöliittymästä metodia [transpose_a](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/gui/main_view.py#L165), joka kutsuu samassa luokassa olevaa metodia [get_values_from_matrix a](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/gui/main_view.py#L288). Tämän jälkeen lähetetään sovelluslogiikalle metodin [return_values_to_service_a(matrix)](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/services/matrix_service.py#L10) avulla äsken haetun matriisin arvo ja kutsutaan metodia [transpose_matrix_a](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/services/matrix_service.py#L18). Sovelluslogiikassa tehdään laskutoimitus ja palautetaan tulos [transpose_matrix_a](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/services/matrix_service.py#L19). Tämän jälkeen main_view.py metodi [show_results(matrix)](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/gui/main_view.py#L311) näyttää tuloksen.

### Muut toiminnallisuudet

## Ohjelman rakenteeseen jääneet heikkoudet

### Käyttöliittymä
