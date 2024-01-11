import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
import time
from texttyper import typingPrint, typingInput, clearScreen


class TestTypingEffect(unittest.TestCase):
    def test_typingPrint(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            typingPrint("Test typingPrint")
            self.assertEqual(mock_stdout.getvalue(), "Test typingPrint")

    def test_typingInput(self):
        with patch('builtins.input', return_value='Test Input'), patch('sys.stdout',
                                                                       new_callable=StringIO) as mock_stdout:
            user_input = typingInput("Test typingInput\n")
            self.assertEqual(mock_stdout.getvalue(), "Test typingInput\n")
            self.assertEqual(user_input, "Test Input")

    def test_clearScreen(self):
        with patch('os.system') as mock_system:
            clearScreen()
            mock_system.assert_called_with("clear")


if __name__ == '__main__':
    unittest.main()
