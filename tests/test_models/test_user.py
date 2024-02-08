import unittest
from models.user import User

class TestUser(unittest.TestCase):
        def test_user_attributes(self):
                user = User()
                self.assertEqual(user.email, "")
                self.assertEqual(user.password, "")
                self.assertEqual(user.first_name, "")
                self.assertEqual(user.last_name, "")

        def test_user_inherits_from_base_model(self):
                user = User()
                self.assertIsInstance(user, BaseModel)

if __name__ == '__main__':
        unittest.main()
