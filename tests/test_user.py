import unittest
from unittest.mock import patch
from models.user import User


class TestUser(unittest.TestCase):
    """
    This class contains unit tests for the User class.
    """

    def setUp(self):
        self.user = User()

    def tearDown(self):
        pass

    def test_email_default_value(self):
        self.assertEqual(self.user.email, "")

    def test_password_default_value(self):
        self.assertEqual(self.user.password, "")

    def test_first_name_default_value(self):
        self.assertEqual(self.user.first_name, "")

    def test_last_name_default_value(self):
        self.assertEqual(self.user.last_name, "")


if __name__ == '__main__':
    unittest.main()
