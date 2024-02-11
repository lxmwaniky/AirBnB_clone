import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    A test case for the Review class.
    """

    def setUp(self):
        self.review = Review()

    def tearDown(self):
        pass

    def test_attributes(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_set_attributes(self):
        self.review.place_id = "123"
        self.review.user_id = "456"
        self.review.text = "Great place!"
        self.assertEqual(self.review.place_id, "123")
        self.assertEqual(self.review.user_id, "456")
        self.assertEqual(self.review.text, "Great place!")


if __name__ == '__main__':
    unittest.main()
