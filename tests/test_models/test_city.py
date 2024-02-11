import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    A test case for the City class.
    """

    def setUp(self):
        self.city = City()

    def tearDown(self):
        pass

    def test_state_id_default_value(self):
        self.assertEqual(self.city.state_id, "")

    def test_name_default_value(self):
        self.assertEqual(self.city.name, "")


if __name__ == '__main__':
    unittest.main()
