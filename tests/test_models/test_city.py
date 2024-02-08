import unittest

class TestCity(unittest.TestCase):
        def test_city_inherits_from_base_model(self):
                city = City()
                self.assertIsInstance(city, BaseModel)

        def test_city_attributes(self):
                city = City()
                self.assertEqual(city.state_id, "")
                self.assertEqual(city.name, "")

        def test_city_attributes_assignment(self):
                city = City()
                city.state_id = "CA"
                city.name = "San Francisco"
                self.assertEqual(city.state_id, "CA")
                self.assertEqual(city.name, "San Francisco")

if __name__ == '__main__':
        unittest.main()
