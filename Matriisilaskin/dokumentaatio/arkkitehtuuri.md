# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattelee kolmitasoista kerrosarkkitehtuuria, ja koodin pakkausrakenne on seuraava:

![Pakkausrakenne](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/pakkausrakenne.jpg)

Pakkaus _gui_ sisältää käyttöliittymästä, _services_ sovelluslogiikasta ja _repositories_ tietojen pysyväistallennuksesta vastaavan koodin. Pakkaus _entities_ sisältää luokan, joka kuvastaa sovelluksen käyttämiä tietokohteita.

## Käyttöliittymä

Käyttöliittymä sisältää kolme erillistä näkymää:

- Matriisilaskimen näkymä, jossa on rajoitettu tai täysversio laskimesta
- Kirjautuminen
- Uuden käyttäjän luominen

Jokainen näistä toteutetaan omana luokkanaan. Näkymistä yksi on aina kerrallaan näkyvänä. Näkymien näyttämisestä vastaa [GUI](../src/gui/gui.py)-luokka. Käyttöliittymä on pyritty eristämään täysin sovelluslogiikasta. Se ainoastaan kutsuu [MatrixService](../src/services/matrix_service.py)- tai [UserService](../src/services/user_service.py)-luokan metodeja.

## Sovelluslogiikka

Laskentaan liittyvistä kokonaisuuksista vastaa luokka [MatrixService](../src/services/matrix_service.py) joka on ainoa olio. Luokka tarjoaa kaikille käyttäliittymän toiminnoille oman metodin. Näitä ovat esimerkiksi:

- `transpose_matrix_a()`
- `determinant_matrix_a()`
- `inverse_matrix_b()`
- `power_of_matrix_a()`

Käyttäjien kirjaamisesta ja lisäämisestä vastaa luokan [UserService] ainoa olio. Luokka tarjoaa kaikille toiminnoille oman metodin, joita ovat esimerkiksi:

- `login(username, password)`
- `create_user(username, password, login=True)`
- `logout()`

_UserService_ pääsee käsiksi käyttäjiin tietojen tallennuksesta vastaavan pakkauksessa repositories sijaitsevan luokkan UserRepository kautta. Luokan toteutus injektoidaan sovelluslogiikalle konstruktorikutsun yhteydessä.

Ohjelman luokkakaavio on seuraavanlainen:

![Luokkakaavio](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/luokka_pakkauskaavio.jpg)

## Tietojen pysyväistallennus

Pakkauksen _repositories_ luokka `UserRepository` huolehtii käyttäjätietojen tallettamisesta. `UserRepository`-luokka tallettaa tiedot SQLite-tietokantaan.

Luokka noudattaa [Repository](https://en.wikipedia.org/wiki/Data_access_object) -suunnittelumallia ja se on tarvittaessa mahdollista korvata uudella toteutuksella, jos sovelluksen datan talletustapaa päätetään vaihtaa. Sovelluslogiikan testauksessa hyödynnetäänkin tätä siten, että testeissä käytetään tietokantaan tallentavien olioiden sijaan keskusmuistiin tallentavia toteutuksia.

### Tiedostot

Sovellus tallettaa käyttäjien tiedot erilliseen tiedostoon.

Sovelluksen juureen sijoitettu [konfiguraatiotiedosto](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md#konfigurointi) [.env](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/data/.env) määrittelee tiedoston nimen.

Käyttäjät tallennetaan SQLite-tietokannan tauluun `users`, joka alustetaan [initialize_database.py](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/initialize_database.py)-tiedostossa.


## Päätoiminnallisuudet

Kuvataan seuraavaksi sovelluksen toimintalogiikka kahden päätoiminnallisuuden osalta sekvenssikaaviona.

### Käyttäjän kirjaantuminen

Kun kirjautumisnäkymän syötekenttiin kirjoitetetataan käyttäjätunnus ja salasana, jonka jälkeen klikataan painiketta _Login_, etenee sovelluksen kontrolli seuraavasti:

![](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sekvenssikaavio_kirjautuminen.jpg)

Painikkeen painamiseen reagoiva [tapahtumankäsittelijä](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/gui/login_view.py#L19) kutsuu sovelluslogiikan `UserService` metodia [login](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/services/user_service.py#L43) antaen parametriksi käyttäjätunnuksen ja salasanan. Sovelluslogiikka selvittää `UserRepository`:n avulla onko käyttäjätunnus olemassa. Jos on, tarkastetaan täsmääkö salasanat. Jos salasanat täsmäävät, kirjautuminen onnistuu. Tämän seurauksena käyttöliittymä vaihtaa näkymäksi rajoittamattoman `MainView`:n, eli sovelluksen varsinaisen päänäkymän.

### Syötteiden kirjaaminen sekä laskutoimitus

![](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sekvenssikaavio.jpg)

Painikkeen painamiseen reagoiva [tapahtumankäsittelijä](../src/gui/main_view.py#L90) kutsuu aluksi käyttöliittymästä metodia [transpose_a](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/gui/main_view.py#L218), joka kutsuu samassa luokassa olevaa metodia [get_values_from_matrix a](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/gui/main_view.py#L384). Tämän jälkeen lähetetään sovelluslogiikalle metodin [return_values_to_service_a(matrix)](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/services/matrix_service.py#L12) avulla äsken haetun matriisin arvo ja kutsutaan metodia [transpose_matrix_a](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/services/matrix_service.py#L36). Sovelluslogiikassa tehdään laskutoimitus ja palautetaan tulos [transpose_matrix_a](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/services/matrix_service.py#L42). Tämän jälkeen main_view.py metodi [show_results(matrix)](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/gui/main_view.py#L430) näyttää tuloksen.

### Muut toiminnallisuudet

Sama periaate toistuu sovelluksen kaikissa laskutoiminnallisuuksissa, käyttöliittymän tapahtumakäsittelijä kutsuu sopivaa sovelluslogiikan metodia, sovelluslogiikka laskee tuloksen ja palauttaa käyttöliittymään.
