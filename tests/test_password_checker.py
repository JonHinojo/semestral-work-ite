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


class TestCheckCharacterTypes(unittest.TestCase):
    """Tests for check_character_types."""

    def test_all_types(self):
        self.assertEqual(check_character_types("Tr0pical!Sun"), (4, []))

    def test_only_lowercase(self):
        self.assertEqual(
            check_character_types("hello"),
            (1, ["no uppercase letters", "no digits", "no symbols"]),
        )

class TestIsCommonPassword(unittest.TestCase):
    """Tests for is_common_password."""

    def test_common_password(self):
        self.assertTrue(is_common_password("password"))

    def test_common_password_uppercase(self):
        self.assertTrue(is_common_password("PASSWORD"))

    def test_uncommon_password(self):
        self.assertFalse(is_common_password("Tr0pical!Sun"))
        
        
class TestScoreToLevel(unittest.TestCase):
    """Tests for score_to_level."""

    def test_levels(self):
        self.assertEqual(score_to_level(2), "Weak")
        self.assertEqual(score_to_level(3), "Medium")
        self.assertEqual(score_to_level(5), "Strong")


class TestEvaluatePassword(unittest.TestCase):
    """Tests for evaluate_password."""

    def test_empty_password(self):
        with self.assertRaises(ValueError):
            evaluate_password("")

    def test_only_spaces(self):
        with self.assertRaises(ValueError):
            evaluate_password("   ")

    def test_strong_password(self):
        self.assertEqual(evaluate_password("Tr0pical!Sun"), ("Strong", []))


if __name__ == "__main__":
    unittest.main()