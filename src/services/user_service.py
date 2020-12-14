from entities.user import User


from repositories.user_repository import (
    user_repository as default_user_repository
)


class InvalidCredentials(Exception):
    pass


class UsernameExists(Exception):
    pass


class UserService:
    """Sovelluslogiikasta vastaa luokka.

    Attributes:
        user: User-olio, joka kuvaa soovellukseen kirjautunutta käyttäjää.
        todo_repository: Olio, jolla on TodoRepository-luokkaa vastaavat metodit.
        user_repository: Olio, jolla on UserRepository-luokkaa vastaavat metodit.
    """

    def __init__(
        self,
        user_repository=default_user_repository
    ):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.

        Args:
            todo_repository:
                Vapaaehtoinen, oletusarvoltaan TodoRepository-olio.
                Olio, jolla on TodoRepository-luokkaa vastaavat metodit.
            user_repository:
                Vapaaehtoinen, oletusarvoltaan UserRepository-olio.
                Olio, jolla on UserRepository-luokkaa vastaavat metodit.
        """
        self.user = None
        self.user_repository = user_repository

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.

        Args:
            username: Merkkijonoarvo, joka kuvaa kirjautuvan käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa kirjautuvan käyttäjän salasanaa.
        Returns:
            Kirjautunut käyttäjä User-olion muodossa.
        Raises:
            InvalidCredentials:
                Virhe, joka tapahtuu, kun käyttäjätunnus ja salasana eivät täsmää.
        """

        user = self.user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentials('Invalid username or password')

        self.user = user

        return user

    def get_current_user(self):
        """Paluttaa kirjautuunen käyttäjän.

        Returns:
            Kirjautunut käyttäjä User-olion muodossa.
        """
        return self.user

    def get_users(self):
        """Palauttaa kaikki käyttäjät.

        Returns:
            User-oliota sisältä lista kaikista käyttäjistä.
        """
        return self.user_repository.find_all()

    def logout(self):
        """Kirjaa nykyisen käyttäjän ulos.
        """
        self.user = None

    def create_user(self, username, password, login=True):
        """Luo uuden käyttäjän ja tarvittaessa kirjaa sen sisään.

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvastaa käyttäjän salasanaa.
            login:
                Vapaahtoinen, oletusarvo True.
                Boolean-arvo, joka kertoo kirjataanko käyttäjä sisään onnistuneen luonnin jälkeen.

        Raises:
            UsernameExists: Virhe, joka tapahtuu, kun käyttäjätunnus on jo käytössä.

        Returns:
            Luotu käyttäjä User-olion muodossa.
        """

        existing_user = self.user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExists(f'Username {username} already exists')

        user = self.user_repository.create(User(username, password))

        if login:
            self.user = user

        return user

user_service = UserService()
