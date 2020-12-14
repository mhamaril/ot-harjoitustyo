import unittest
from entities.user import User
from services.user_service import (
    UserService,
    InvalidCredentials,
    UsernameExists
)

class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def find_all(self):
        return self.users

    def find_by_username(self, username):
        matching_users = filter(
            lambda user: user.username == username,
            self.users
        )

        matching_users_list = list(matching_users)

        return matching_users_list[0] if len(matching_users_list) > 0 else None

    def create(self, user):
        self.users.append(user)

        return user

    def delete_all(self):
        self.users = []


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService(
            FakeUserRepository()
        )
        self.user_kalle = User('kalle', 'kalle123')

    def login_user(self, user):
        self.user_service.create_user(user.username, user.password)

    def test_login_with_valid_username_and_password(self):
        self.user_service.create_user(
            self.user_kalle.username,
            self.user_kalle.password
        )

        user = self.user_service.login(
            self.user_kalle.username,
            self.user_kalle.password
        )

        self.assertEqual(user.username, self.user_kalle.username)

    def test_login_with_invalid_username_and_password(self):
        self.assertRaises(
            InvalidCredentials,
            lambda: self.user_service.login('testing', 'invalid')
        )

    def test_get_current_user(self):
        self.login_user(self.user_kalle)

        current_user = self.user_service.get_current_user()

        self.assertEqual(current_user.username, self.user_kalle.username)

    def test_create_user_with_non_existing_username(self):
        username = self.user_kalle.username
        password = self.user_kalle.password

        self.user_service.create_user(username, password)

        users = self.user_service.get_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, username)

    def test_create_user_with_existing_username(self):
        username = self.user_kalle.username

        self.user_service.create_user(username, 'something')

        self.assertRaises(
            UsernameExists,
            lambda: self.user_service.create_user(username, 'random')
        )
