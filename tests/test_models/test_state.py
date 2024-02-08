import unittest
from models.state import State

class TestState(unittest.TestCase):

        def test_state_name(self):
                state = State()
                self.assertEqual(state.name, "")

if __name__ == '__main__':
        unittest.main()
