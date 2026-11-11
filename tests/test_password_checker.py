'''tests for the password_checker file'''

import unittest
from src.password_checker import (
    check_lenght,
    check_character_types,
    is_common_password,
    score_to_level,
    evaluate_password,
)



class TestCheckLength(unittest.TestCase):
    """Tests for check_length"""

    def test_short_password(self):
        self.assertEqual(check_length("abc"), (0, ["shorter than 8 characters"]))

    def test_exactly_8_characters(self):
        self.assertEqual(check_length("abcdefgh"), (1, ["shorter than 12 characters"]))

    def test_exactly_12_characters(self):
        self.assertEqual(check_length("abcdefghijkl"), (2, []))
