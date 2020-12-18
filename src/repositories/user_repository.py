from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    return User(row['username'], row['password']) if row else None


class UserRepository:
    """Class resposible of user data
    """
    def __init__(self, connection):
        """Constructor of the Class.

        Args:
            connection (sqlite3): Sqlite3 dtabase connection
        """
        self.connection = connection

    def find_all(self):
        """Returns all users from database

        Returns:
            list: list of users
        """
        cursor = self.connection.cursor()

        cursor.execute('select * from users')

        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def find_by_username(self, username):
        """[summary]

        Args:
            username (str): Username of the user

        Returns:
            User-object: User-object
        """
        cursor = self.connection.cursor()

        cursor.execute(
            'select * from users where username = ?',
            (username,)
        )

        row = cursor.fetchone()

        return get_user_by_row(row)

    def create(self, user):
        """Creates new user

        Args:
            user (User-object): User-object

        Returns:
            User-object: User-object
        """
        cursor = self.connection.cursor()

        cursor.execute(
            'insert into users (username, password) values (?, ?)',
            (user.username, user.password)
        )

        self.connection.commit()

        return user

    def delete_all(self):
        """Deletes all user from database
        """
        cursor = self.connection.cursor()

        cursor.execute('delete from users')

        self.connection.commit()


user_repository = UserRepository(get_database_connection())
