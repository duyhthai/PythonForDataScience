import unittest
from unittest.mock import patch
from . import basic
from . import stats

class TestNegativeScenarios(unittest.TestCase):

    @patch('basic.some_function')
    def test_invalid_input_type(self, mock_function):
        with self.assertRaises(TypeError):
            mock_function("invalid_input")

    @patch('stats.calculate_mean')
    def test_empty_list(self, mock_function):
        with self.assertRaises(ValueError):
            mock_function([])

    @patch('basic.validate_data')
    def test_rule_violation(self, mock_function):
        with self.assertRaises(Exception):
            mock_function([1, 2, 3], "invalid_rule")

if __name__ == '__main__':
    unittest.main()