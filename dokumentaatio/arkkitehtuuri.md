# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattelee kolmitasoista kerrosarkkitehtuuria, ja koodin pakkausrakenne on seuraava:

![Pakkausrakenne](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/pakkausrakenne.jpg)

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

![Luokkakaavio](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/luokka_pakkauskaavio.jpg)

## Tietojen pysyväistallennus

Pakkauksen _repositories_ luokka `UserRepository` huolehtii käyttäjätietojen tallettamisesta. `UserRepository`-luokka tallettaa tiedot SQLite-tietokantaan.

Luokka noudattaa [Repository](https://en.wikipedia.org/wiki/Data_access_object) -suunnittelumallia ja se on tarvittaessa mahdollista korvata uudella toteutuksella, jos sovelluksen datan talletustapaa päätetään vaihtaa. Sovelluslogiikan testauksessa hyödynnetäänkin tätä siten, että testeissä käytetään tietokantaan tallentavien olioiden sijaan keskusmuistiin tallentavia toteutuksia.

### Tiedostot

Sovellus tallettaa käyttäjien tiedot erillisiin tiedostoihin.

Sovelluksen juureen sijoitettu [konfiguraatiotiedosto](./kayttoohje.md#konfiguraatiotiedosto) [.env](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/data/.env) määrittelee tiedostojen nimet.

Käyttäjät tallennetaan SQLite-tietokannan tauluun `users`, joka alustetaan [initialize_database.py](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/initialize_database.py)-tiedostossa.


## Päätoiminnallisuudet

Kuvataan seuraavaksi sovelluksen toimintalogiikka yhden päätoiminnallisuuden osalta sekvenssikaaviona.

### Syötteiden kirjaaminen sekä laskutoimitus

![](https://github.com/mhamaril/ot-harjoitustyo/blob/master/dokumentaatio/sekvenssikaavio.jpg)

Painikkeen painamiseen reagoiva [tapahtumankäsittelijä](../src/gui/main_view.py#L90) kutsuu aluksi käyttöliittymästä metodia [transpose_a](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/gui/main_view.py#L165), joka kutsuu samassa luokassa olevaa metodia [get_values_from_matrix a](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/gui/main_view.py#L288). Tämän jälkeen lähetetään sovelluslogiikalle metodin [return_values_to_service_a(matrix)](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/services/matrix_service.py#L10) avulla äsken haetun matriisin arvo ja kutsutaan metodia [transpose_matrix_a](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/services/matrix_service.py#L18). Sovelluslogiikassa tehdään laskutoimitus ja palautetaan tulos [transpose_matrix_a](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/services/matrix_service.py#L19). Tämän jälkeen main_view.py metodi [show_results(matrix)](https://github.com/mhamaril/ot-harjoitustyo/blob/master/src/gui/main_view.py#L311) näyttää tuloksen.

### Muut toiminnallisuudet

Sama periaate toistoo sovelluksen kaikissa toiminnallisuuksissa, käyttöliittymän tapahtumakäsittelijä kutsuu sopivaa sovelluslogiikan metodia, sovelluslogiikka päivittää kirjautuneen käyttäjän tilaa. Kontrollin palatessa käyttäliittymään, päivitetään tarvittaessa todojen lista sekä aktiivinen näkymä.


## Ohjelman rakenteeseen jääneet heikkoudet

### Käyttöliittymä
