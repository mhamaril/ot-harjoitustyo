# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattelee kaksitasoista kerrosarkkitehtuuria, ja koodin pakkausrakenne on seuraava:

![Pakkausrakenne](./kuvat/arkkitehtuuri-pakkaus.png)

Pakkaus _gui_ sisältää käyttöliittymästä ja _services_ sovelluslogiikasta vastaavan koodin.

## Käyttöliittymä

Käyttöliittymä sisältää tällä hetkellä yhden näkymän:

- Päänäkymä, missä voi tehdä matriiseilla laskutoimituksia
- Aloitusnäkymä, missä valitaan matriisien koot

Jokainen näistä toteutetaan omana luokkanaan. Näkymistä yksi on aina kerrallaan näkyvänä. Näkymien näyttämisestä vastaa [GUI](../src/gui/gui.py)-luokka. Käyttöliittymä on pyritty eristämään täysin sovelluslogiikasta. Se ainoastaan kutsuu [MatrixService](../src/services/matrix_service.py)-luokan metodeja.

## Sovelluslogiikka

Toiminnallisista kokonaisuuksista vastaa luokkan [MatrixService](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/services/todo_service.py) ainoa olio. Luokka tarjoaa kaikille käyttäliittymän toiminnoille oman metodin. Näitä ovat esimerkiksi:

- `transpose_matrix_a()`
- `determinant_matrix_a()`
- `inverse_matrix_b()`
- `power_of_matrix_a()`

`MatrixService`-luokan ja ohjelman muiden osien suhdetta kuvaava luokka/pakkauskaavio:

![Pakkausrakenne ja luokat](./kuvat/arkkitehtuuri-pakkaus-luokat.png)

Luokat noudattavat [Repository](https://en.wikipedia.org/wiki/Data_access_object) -suunnittelumallia ja ne on tarvittaessa mahdollista korvata uusilla toteutuksilla, jos sovelluksen datan talletustapaa päätetään vaihtaa. Sovelluslogiikan testauksessa hyödynnetäänkin tätä siten, että testeissä käytetään tiedostoon ja tietokantaan tallentavien olioiden sijaan keskusmuistiin tallentavia toteutuksia.

## Päätoiminnallisuudet

Kuvataan seuraavaksi sovelluksen toimintalogiikka muutaman päätoiminnallisuuden osalta sekvenssikaaviona.

### Syötteiden kirjaaminen sekä laskutoimitus

![](./kuvat/sekvenssi-kirjautuminen.png)

Painikkeen painamiseen reagoiva [tapahtumankäsittelijä](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/ui/login_view.py#L18) kutsuu sovelluslogiikan `TodoService` metodia [login](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/services/todo_service.py#L87) antaen parametriksi käyttäjätunnuksen ja salasanan. Sovelluslogiikka selvittää `UserRepository`:n avulla onko käyttäjätunnus olemassa. Jos on, tarkastetaan täsmääkö salasanat. Jos salasanat täsmäävät, kirjautuminen onnistuu. Tämän seurauksena käyttöliittymä vaihtaa näkymäksi `TodosView`:n, eli sovelluksen varsinaisen päänäkymän ja renderöi näkymään kirjautuneen käyttäjän todot eli tekemättömät tehtävät.

### Muut toiminnallisuudet

## Ohjelman rakenteeseen jääneet heikkoudet

### Käyttöliittymä
