import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def tearDown(self):
        pass

    def test_name_default_value(self):
        self.assertEqual(self.amenity.name, "")

    def test_name_assignment(self):
        self.amenity.name = "Swimming Pool"
        self.assertEqual(self.amenity.name, "Swimming Pool")


if __name__ == '__main__':
    unittest.main()
