from entities.user import User


from repositories.user_repository import (
    user_repository as default_user_repository
)


class InvalidCredentials(Exception):
    pass


class UsernameExists(Exception):
    pass


class UserService:
    """Class responsible of user services

    Attributes:
        user: User-object, that represents logged user
        user_repository: Object that has methods of UserRepository class
    """

    def __init__(
        self,
        user_repository=default_user_repository
    ):
        """Constructor of the Class. Creates a service responsible of user logic

        Args:
            user_repository:
                Object that has methods of UserRepository class
        """
        self.user = None
        self.user_repository = user_repository

    def login(self, username, password):
        """Logs user in.

        Args:
            username (str): Username of the user
            password (str): Password of the user
        Returns:
            Logged user as a User-object
        Raises:
            InvalidCredentials:
                Raises exception if username and password don't match
        """

        user = self.user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentials('Invalid username or password')

        self.user = user

        return user

    def get_current_user(self):
        """Returns logged user

        Returns:
            Logged user as User object
        """
        return self.user

    def get_users(self):
        """Returns all users

        Returns:
            List of all users
        """
        return self.user_repository.find_all()

    def logout(self):
        """Logs out current user
        """
        self.user = None

    def create_user(self, username, password, login=True):
        """Creates new user and logs the user in if login is set True

        Args:
            username (str): Username of the user
            password (str): Password of the user
            login:
                Voluntary, default True.
                Boolean-value, that tells if the user logs in after succesfull creation
                of a new user

        Raises:
            UsernameExists: Raises exception if username is already taken

        Returns:
            New user as User-object
        """

        existing_user = self.user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExists(f'Username {username} already exists')

        user = self.user_repository.create(User(username, password))

        if login:
            self.user = user

        return user

user_service = UserService()
