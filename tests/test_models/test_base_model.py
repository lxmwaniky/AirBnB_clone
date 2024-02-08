import unittest

class TestBaseModel(unittest.TestCase):
        def test_init(self):
                # Test initialization of BaseModel instance
                base_model = BaseModel()
                self.assertIsInstance(base_model, BaseModel)
                self.assertIsNotNone(base_model.id)
                self.assertIsNotNone(base_model.created_at)
                self.assertIsNotNone(base_model.updated_at)

        def test_str(self):
                # Test string representation of BaseModel instance
                base_model = BaseModel()
                string = str(base_model)
                self.assertEqual(string, "[BaseModel] ({}) {}".format(base_model.id, base_model.__dict__))

        def test_save(self):
                # Test saving BaseModel instance
                base_model = BaseModel()
                base_model.save()
                self.assertIsNotNone(base_model.updated_at)

        def test_to_dict(self):
                # Test conversion of BaseModel instance to dictionary
                base_model = BaseModel()
                base_model_dict = base_model.to_dict()
                self.assertIsInstance(base_model_dict, dict)
                self.assertEqual(base_model_dict['__class__'], 'BaseModel')
                self.assertEqual(base_model_dict['created_at'], base_model.created_at.isoformat())
                self.assertEqual(base_model_dict['updated_at'], base_model.updated_at.isoformat())

if __name__ == '__main__':
        unittest.main()
