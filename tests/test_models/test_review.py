import unittest
from models.review import Review

class TestReview(unittest.TestCase):
        def setUp(self):
                self.review = Review()

        def test_attributes_initialization(self):
                self.assertEqual(self.review.place_id, "")
                self.assertEqual(self.review.user_id, "")
                self.assertEqual(self.review.text, "")

        def test_attributes_assignment(self):
                self.review.place_id = "123"
                self.review.user_id = "456"
                self.review.text = "Great place!"
                self.assertEqual(self.review.place_id, "123")
                self.assertEqual(self.review.user_id, "456")
                self.assertEqual(self.review.text, "Great place!")

        def test_inheritance(self):
                self.assertIsInstance(self.review, BaseModel)

if __name__ == '__main__':
        unittest.main()
