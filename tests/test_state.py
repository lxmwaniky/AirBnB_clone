import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Unit tests for the State class.
    """

    def setUp(self):
        self.state = State()

    def tearDown(self):
        pass

    def test_name_default_value(self):
        self.assertEqual(self.state.name, "")

    def test_name_assignment(self):
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")


if __name__ == '__main__':
    unittest.main()
