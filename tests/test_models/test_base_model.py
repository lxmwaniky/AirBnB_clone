import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    This class contains unit tests for the BaseModel class.
    """

    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        pass

    def test_init(self):
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        expected_str = "[BaseModel] ({}) {}"
        .format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
            }
        self.assertDictEqual(self.base_model.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
