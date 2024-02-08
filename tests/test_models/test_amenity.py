import unittest

class TestAmenity(unittest.TestCase):
        def test_name_attribute(self):
                amenity = Amenity()
                self.assertEqual(amenity.name, "")

        def test_name_assignment(self):
                amenity = Amenity()
                amenity.name = "Swimming Pool"
                self.assertEqual(amenity.name, "Swimming Pool")


if __name__ == '__main__':
        unittest.main()
