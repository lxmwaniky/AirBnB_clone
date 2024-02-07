import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
        def setUp(self):
                self.base_model = BaseModel()

        def test_init(self):
                self.assertIsInstance(self.base_model, BaseModel)
                self.assertIsNotNone(self.base_model.id)
                self.assertIsInstance(self.base_model.created_at, datetime.datetime)
                self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

        def test_str(self):
                expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
                self.assertEqual(str(self.base_model), expected_str)

        def test_save(self):
                old_updated_at = self.base_model.updated_at
                self.base_model.save()
                self.assertNotEqual(old_updated_at, self.base_model.updated_at)

        def test_to_dict(self):
                base_model_dict = self.base_model.to_dict()
                self.assertIsInstance(base_model_dict, dict)
                self.assertEqual(base_model_dict['__class__'], 'BaseModel')
                self.assertEqual(base_model_dict['id'], self.base_model.id)
                self.assertEqual(base_model_dict['created_at'], self.base_model.created_at.isoformat())
                self.assertEqual(base_model_dict['updated_at'], self.base_model.updated_at.isoformat())

if __name__ == '__main__':
        unittest.main()