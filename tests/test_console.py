import unittest
from unittest.mock import patch
from console import HBNBConsole

class TestHBNBConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBConsole()

    def tearDown(self):
        pass

    def test_prompt(self):
        self.assertEqual(self.console.prompt, '(hbnb) ')

    def test_do_EOF(self):
        with patch('builtins.input', return_value='EOF'):
            self.assertTrue(self.console.do_EOF(''))

    def test_do_help(self):
        with patch('builtins.input', return_value='help'):
            self.assertTrue(self.console.do_help(''))

    def test_do_quit(self):
        with patch('builtins.input', return_value='quit'):
            self.assertTrue(self.console.do_quit(''))

    def test_emptyline(self):
        self.assertIsNone(self.console.emptyline())

if __name__ == '__main__':
    unittest.main()